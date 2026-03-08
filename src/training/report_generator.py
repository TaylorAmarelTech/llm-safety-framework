"""
HTML and JSON report generation for the training pipeline.

Produces self-contained HTML files (no external CSS/JS dependencies) that
visualise feedback-loop progress, model comparisons, attack effectiveness,
and curriculum learning stages.  All charts are inline SVG; all styles are
embedded.  Reports can be opened directly in any browser.
"""

from __future__ import annotations

import html
import json
import math
import time
from pathlib import Path
from typing import Any

from pydantic import BaseModel


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

class ReportConfig(BaseModel):
    """Settings for report generation."""
    output_dir: Path = Path("data/reports")
    title_prefix: str = "LLM Safety Training"
    include_raw_data: bool = False
    max_chart_points: int = 50


# ---------------------------------------------------------------------------
# Colour helpers
# ---------------------------------------------------------------------------

_PALETTE = [
    "#2563eb", "#dc2626", "#16a34a", "#d97706", "#7c3aed",
    "#0891b2", "#be185d", "#4d7c0f", "#b45309", "#6d28d9",
]

_GREEN = "#16a34a"
_RED = "#dc2626"
_AMBER = "#d97706"
_GREY = "#64748b"


def _rate_colour(value: float, *, invert: bool = False) -> str:
    """Return green/amber/red based on a 0-1 rate.

    By default high = bad (bypass succeeded = red).
    Pass ``invert=True`` when high = good (refusal rate).
    """
    if invert:
        value = 1.0 - value
    if value < 0.15:
        return _GREEN
    if value < 0.40:
        return _AMBER
    return _RED


def _heatmap_colour(value: float) -> str:
    """Continuous red intensity for a 0-1 value (higher = more red)."""
    clamped = max(0.0, min(1.0, value))
    r = 220 + int(35 * clamped)
    g = int(240 * (1 - clamped))
    b = int(240 * (1 - clamped))
    return f"rgb({r},{g},{b})"


def _pct(value: float) -> str:
    """Format a 0-1 float as a percentage string."""
    return f"{value * 100:.1f}%"


# ---------------------------------------------------------------------------
# SVG chart helpers
# ---------------------------------------------------------------------------

def _svg_bar_chart(
    data: list[tuple[str, float]],
    width: int = 500,
    height: int = 260,
    *,
    colour_fn: Any | None = None,
) -> str:
    """Render a horizontal bar chart as inline SVG.

    *data* is a list of ``(label, value)`` tuples where values are in [0, 1].
    """
    if not data:
        return "<p>No data available.</p>"

    bar_h = 22
    gap = 6
    label_w = 160
    chart_w = width - label_w - 60
    needed_h = max(height, len(data) * (bar_h + gap) + 40)
    lines: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
        f'height="{needed_h}" style="font-family:monospace;font-size:12px;">'
    ]
    for i, (label, val) in enumerate(data):
        y = 20 + i * (bar_h + gap)
        bw = max(1, int(chart_w * min(val, 1.0)))
        fill = colour_fn(val) if colour_fn else _rate_colour(val)
        esc = html.escape(label[:22])
        lines.append(
            f'<text x="{label_w - 6}" y="{y + 15}" text-anchor="end" '
            f'fill="#334155">{esc}</text>'
        )
        lines.append(
            f'<rect x="{label_w}" y="{y}" width="{bw}" height="{bar_h}" '
            f'rx="3" fill="{fill}" />'
        )
        lines.append(
            f'<text x="{label_w + bw + 6}" y="{y + 15}" '
            f'fill="#334155">{_pct(val)}</text>'
        )
    lines.append("</svg>")
    return "\n".join(lines)


def _svg_line_chart(
    points: list[float],
    width: int = 520,
    height: int = 200,
    *,
    label: str = "",
    colour: str = "#2563eb",
) -> str:
    """Render a simple line chart as inline SVG.

    *points* is a list of y-values in [0, 1].
    """
    if len(points) < 2:
        return "<p>Not enough data for a line chart.</p>"

    pad_l, pad_r, pad_t, pad_b = 50, 20, 20, 30
    plot_w = width - pad_l - pad_r
    plot_h = height - pad_t - pad_b
    n = len(points)
    step = plot_w / max(n - 1, 1)
    y_max = max(max(points), 0.01)

    lines: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
        f'height="{height}" style="font-family:monospace;font-size:11px;">'
    ]

    # Y-axis ticks
    for tick in (0, 0.25, 0.5, 0.75, 1.0):
        ty = pad_t + plot_h * (1 - tick / y_max) if y_max >= tick else pad_t
        lines.append(
            f'<line x1="{pad_l}" y1="{ty}" x2="{pad_l + plot_w}" y2="{ty}" '
            f'stroke="#e2e8f0" />'
        )
        lines.append(
            f'<text x="{pad_l - 6}" y="{ty + 4}" text-anchor="end" '
            f'fill="#94a3b8">{_pct(tick)}</text>'
        )

    # Data line
    pts: list[str] = []
    for i, v in enumerate(points):
        px = pad_l + i * step
        py = pad_t + plot_h * (1 - v / y_max)
        pts.append(f"{px:.1f},{py:.1f}")

    lines.append(
        f'<polyline points="{" ".join(pts)}" fill="none" '
        f'stroke="{colour}" stroke-width="2" />'
    )

    # Dots
    for i, v in enumerate(points):
        px = pad_l + i * step
        py = pad_t + plot_h * (1 - v / y_max)
        lines.append(
            f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3" fill="{colour}" />'
        )

    # X-axis label
    if label:
        lines.append(
            f'<text x="{width // 2}" y="{height - 4}" text-anchor="middle" '
            f'fill="#64748b">{html.escape(label)}</text>'
        )

    lines.append("</svg>")
    return "\n".join(lines)


def _heatmap_table(
    rows: list[str],
    cols: list[str],
    values: dict[tuple[str, str], float],
) -> str:
    """Render a colour-coded HTML table.

    *values* maps ``(row_label, col_label)`` to a 0-1 float.
    """
    parts: list[str] = ['<table class="hm"><tr><th></th>']
    for c in cols:
        parts.append(f"<th>{html.escape(c)}</th>")
    parts.append("</tr>")

    for r in rows:
        parts.append(f"<tr><td class='rl'>{html.escape(r)}</td>")
        for c in cols:
            v = values.get((r, c), 0.0)
            bg = _heatmap_colour(v)
            fg = "#fff" if v > 0.55 else "#1e293b"
            parts.append(
                f'<td style="background:{bg};color:{fg};text-align:center">'
                f"{_pct(v)}</td>"
            )
        parts.append("</tr>")

    parts.append("</table>")
    return "\n".join(parts)


def _progress_badge(value: float, threshold: float) -> str:
    """Return a small pass/fail badge span."""
    passed = value >= threshold
    bg = _GREEN if passed else _RED
    txt = "PASS" if passed else "FAIL"
    return (
        f'<span style="background:{bg};color:#fff;padding:2px 8px;'
        f'border-radius:4px;font-size:12px;font-weight:600">{txt} '
        f"{_pct(value)}</span>"
    )


# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------

_CSS = """
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',
     Roboto,sans-serif;background:#f1f5f9;color:#1e293b}
.hdr{background:#0f172a;color:#f8fafc;padding:24px 32px}
.hdr h1{margin:0;font-size:22px;font-weight:600}
.hdr p{margin:4px 0 0;color:#94a3b8;font-size:13px}
.body{max-width:960px;margin:0 auto;padding:24px}
.card{background:#fff;border-radius:8px;box-shadow:0 1px 3px rgba(0,0,0,.1);
      padding:20px 24px;margin-bottom:20px}
.card h2{margin:0 0 12px;font-size:17px;border-bottom:1px solid #e2e8f0;
         padding-bottom:8px;color:#0f172a}
table{border-collapse:collapse;width:100%}
th,td{padding:6px 10px;text-align:left;border-bottom:1px solid #e2e8f0;
      font-size:13px;font-family:monospace}
th{background:#f8fafc;font-weight:600;color:#475569}
td{color:#334155}
.hm td,.hm th{padding:4px 8px;font-size:12px}
.hm th{background:#f8fafc}
.rl{font-weight:600;text-align:right;padding-right:8px}
.metric{display:inline-block;background:#f1f5f9;border-radius:6px;
        padding:10px 18px;margin:4px;text-align:center}
.metric .val{font-size:22px;font-weight:700;font-family:monospace}
.metric .lbl{font-size:11px;color:#64748b;margin-top:2px}
.badge-green{background:#16a34a;color:#fff;padding:2px 8px;border-radius:4px;
             font-size:12px;font-weight:600}
.badge-red{background:#dc2626;color:#fff;padding:2px 8px;border-radius:4px;
           font-size:12px;font-weight:600}
.badge-amber{background:#d97706;color:#fff;padding:2px 8px;border-radius:4px;
             font-size:12px;font-weight:600}
ul.recs{padding-left:18px}
ul.recs li{margin-bottom:6px;font-size:14px;line-height:1.5}
.ts{color:#94a3b8;font-size:12px;margin-top:24px;text-align:center}
"""


def _render_html(title: str, sections: list[tuple[str, str]]) -> str:
    """Assemble a full self-contained HTML page.

    *sections* is a list of ``(heading, body_html)`` tuples rendered as
    cards in order.
    """
    cards = []
    for heading, body in sections:
        cards.append(
            f'<div class="card"><h2>{html.escape(heading)}</h2>{body}</div>'
        )
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())

    return (
        "<!DOCTYPE html>\n<html lang='en'><head>"
        "<meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        f"<title>{html.escape(title)}</title>"
        f"<style>{_CSS}</style></head><body>"
        f'<div class="hdr"><h1>{html.escape(title)}</h1>'
        f"<p>Generated {timestamp}</p></div>"
        f'<div class="body">{"".join(cards)}</div>'
        f'<p class="ts">LLM Safety Training Pipeline &mdash; {timestamp}</p>'
        "</body></html>"
    )


# ---------------------------------------------------------------------------
# ReportGenerator
# ---------------------------------------------------------------------------

class ReportGenerator:
    """Generate self-contained HTML and JSON reports for the training pipeline."""

    def __init__(self, config: ReportConfig | None = None) -> None:
        self.config = config or ReportConfig()

    # -- helpers --

    def _ensure_dir(self, path: Path) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        return path

    def _write(self, path: Path, content: str) -> Path:
        self._ensure_dir(path)
        path.write_text(content, encoding="utf-8")
        return path

    def _downsample(self, values: list[Any]) -> list[Any]:
        """Keep at most *max_chart_points* evenly spaced items."""
        mx = self.config.max_chart_points
        if len(values) <= mx:
            return list(values)
        step = len(values) / mx
        return [values[int(i * step)] for i in range(mx)]

    # -----------------------------------------------------------------
    # 1. Training / feedback-loop report
    # -----------------------------------------------------------------

    def generate_training_report(
        self,
        progress_data: dict[str, Any],
        output_path: Path | None = None,
    ) -> Path:
        """Create an HTML report on feedback-loop progress.

        *progress_data* is expected to match the dict returned by
        ``ProgressTracker.get_summary()``.
        """
        out = output_path or (self.config.output_dir / "training_report.html")
        sections: list[tuple[str, str]] = []

        iterations = progress_data.get("total_iterations", 0)
        trend = progress_data.get("overall_trend", {})
        plateau = progress_data.get("plateau_detected", False)
        cat_trends = progress_data.get("category_trends", {})
        gen_eff = progress_data.get("generator_effectiveness", {})

        # -- summary metrics --
        direction = trend.get("direction", "unknown")
        slope = trend.get("slope", 0)
        latest = trend.get("latest", 0)
        dir_badge = {
            "improving": "badge-red",
            "degrading": "badge-green",
            "stable": "badge-amber",
        }.get(direction, "badge-amber")

        metrics_html = (
            f'<div class="metric"><div class="val">{iterations}</div>'
            f'<div class="lbl">Iterations</div></div>'
            f'<div class="metric"><div class="val">{_pct(latest)}</div>'
            f'<div class="lbl">Current Bypass Rate</div></div>'
            f'<div class="metric"><div class="val">'
            f'<span class="{dir_badge}">{direction.upper()}</span></div>'
            f'<div class="lbl">Trend (slope {slope:+.4f})</div></div>'
            f'<div class="metric"><div class="val">'
            f'{"YES" if plateau else "No"}</div>'
            f'<div class="lbl">Plateau Detected</div></div>'
        )
        sections.append(("Overview", metrics_html))

        # -- bypass rate trend line --
        values = trend.get("values", [])
        if values:
            chart = _svg_line_chart(
                self._downsample(values),
                label="Bypass rate over iterations",
                colour=_RED,
            )
            sections.append(("Bypass Rate Trend", chart))

        # -- category effectiveness table + bar chart --
        if cat_trends:
            rows: list[str] = []
            bar_data: list[tuple[str, float]] = []
            for cat, info in sorted(
                cat_trends.items(), key=lambda x: -x[1].get("latest_rate", 0)
            ):
                lr = info.get("latest_rate", 0)
                delta = info.get("delta", 0)
                d_sign = "+" if delta >= 0 else ""
                colour = _rate_colour(lr)
                rows.append(
                    f"<tr><td>{html.escape(cat)}</td>"
                    f'<td style="color:{colour};font-weight:600">{_pct(lr)}</td>'
                    f"<td>{d_sign}{_pct(delta)}</td>"
                    f"<td>{info.get('direction', '')}</td></tr>"
                )
                bar_data.append((cat, lr))

            table = (
                "<table><tr><th>Category</th><th>Bypass Rate</th>"
                "<th>Delta</th><th>Trend</th></tr>"
                + "".join(rows) + "</table>"
            )
            chart = _svg_bar_chart(bar_data)
            sections.append(("Per-Category Attack Effectiveness", table + chart))

        # -- generator quality --
        eff_data = gen_eff.get("data", [])
        if eff_data:
            rows_g: list[str] = []
            for e in eff_data:
                rows_g.append(
                    f"<tr><td>{e.get('iteration', '?')}</td>"
                    f"<td>{_pct(e.get('quality_pass_rate', 0))}</td>"
                    f"<td>{_pct(e.get('bypass_rate', 0))}</td>"
                    f"<td>{e.get('effective_attacks', 0)}</td></tr>"
                )
            table_g = (
                "<table><tr><th>Iteration</th><th>Quality Pass Rate</th>"
                "<th>Bypass Rate</th><th>Effective Attacks</th></tr>"
                + "".join(rows_g) + "</table>"
            )
            sections.append(("Generator Quality Metrics", table_g))

        # -- plateau status --
        if plateau:
            plateau_html = (
                '<p style="color:#dc2626;font-weight:600">'
                "Plateau detected &mdash; recent iterations show minimal change "
                "in bypass rate. Consider:</p>"
                '<ul class="recs">'
                "<li>Switching mutation strategies or adding new categories</li>"
                "<li>Re-seeding the population with novel attack templates</li>"
                "<li>Increasing crossover/mutation rates in the evolutionary engine</li>"
                "<li>Targeting under-explored migration corridors or categories</li>"
                "</ul>"
            )
        else:
            plateau_html = (
                '<p style="color:#16a34a;font-weight:600">'
                "No plateau detected &mdash; the feedback loop is still making "
                "progress.</p>"
            )
        sections.append(("Plateau Detection", plateau_html))

        # -- recommendations --
        recs = self._training_recommendations(progress_data)
        recs_html = '<ul class="recs">' + "".join(
            f"<li>{html.escape(r)}</li>" for r in recs
        ) + "</ul>"
        sections.append(("Recommendations", recs_html))

        title = f"{self.config.title_prefix} \u2014 Training Report"
        return self._write(out, _render_html(title, sections))

    def _training_recommendations(
        self, data: dict[str, Any]
    ) -> list[str]:
        recs: list[str] = []
        cat_trends = data.get("category_trends", {})
        plateau = data.get("plateau_detected", False)
        gen_eff = data.get("generator_effectiveness", {})

        if plateau:
            recs.append(
                "Bypass rate has plateaued. Introduce new mutation categories "
                "or increase evolutionary diversity."
            )

        # Identify weak categories
        weak = [
            c for c, v in cat_trends.items()
            if v.get("latest_rate", 0) < 0.05
        ]
        if weak:
            recs.append(
                f"Categories with near-zero bypass: {', '.join(weak)}. "
                "Focus generation on these to improve coverage."
            )

        # Identify strong categories
        strong = [
            c for c, v in cat_trends.items()
            if v.get("latest_rate", 0) > 0.50
        ]
        if strong:
            recs.append(
                f"High-bypass categories: {', '.join(strong)}. "
                "These reveal significant model vulnerabilities — "
                "prioritise for DPO/ORPO hardening."
            )

        eff_list = gen_eff.get("data", [])
        if eff_list:
            latest = eff_list[-1]
            if latest.get("quality_pass_rate", 1) < 0.30:
                recs.append(
                    "Generator quality pass rate is below 30%. Consider "
                    "fine-tuning the generator model or adjusting scoring "
                    "thresholds."
                )

        if not recs:
            recs.append("Pipeline is progressing well. Continue iterating.")

        return recs

    # -----------------------------------------------------------------
    # 2. Model comparison report
    # -----------------------------------------------------------------

    def generate_model_comparison_report(
        self,
        results_by_model: dict[str, dict[str, Any]],
        output_path: Path | None = None,
    ) -> Path:
        """Create an HTML report comparing multiple target models.

        *results_by_model* maps model names to dicts with keys:
        ``bypass_rate`` (float), ``by_category`` (dict[str, float]).
        """
        out = output_path or (self.config.output_dir / "model_comparison.html")
        sections: list[tuple[str, str]] = []
        models = sorted(results_by_model.keys())

        # -- overall bypass rates --
        bar_data = [
            (m, results_by_model[m].get("bypass_rate", 0)) for m in models
        ]
        table_rows = "".join(
            f"<tr><td>{html.escape(m)}</td>"
            f'<td style="color:{_rate_colour(v)};font-weight:600">'
            f"{_pct(v)}</td></tr>"
            for m, v in bar_data
        )
        table = (
            "<table><tr><th>Model</th><th>Bypass Rate</th></tr>"
            + table_rows + "</table>"
        )
        chart = _svg_bar_chart(bar_data)
        sections.append(("Overall Bypass Rates", table + chart))

        # -- per-model category breakdown --
        all_cats: set[str] = set()
        for info in results_by_model.values():
            all_cats.update(info.get("by_category", {}).keys())
        cats = sorted(all_cats)

        if cats:
            for m in models:
                by_cat = results_by_model[m].get("by_category", {})
                rows = [(c, by_cat.get(c, 0.0)) for c in cats]
                chart_m = _svg_bar_chart(rows, width=540)
                sections.append(
                    (f"Category Breakdown \u2014 {m}", chart_m)
                )

        # -- vulnerability heatmap --
        if cats and len(models) > 1:
            values: dict[tuple[str, str], float] = {}
            for m in models:
                by_cat = results_by_model[m].get("by_category", {})
                for c in cats:
                    values[(m, c)] = by_cat.get(c, 0.0)
            hmap = _heatmap_table(models, cats, values)
            sections.append(("Vulnerability Heatmap (Models x Categories)", hmap))

        title = f"{self.config.title_prefix} \u2014 Model Comparison"
        return self._write(out, _render_html(title, sections))

    # -----------------------------------------------------------------
    # 3. Attack effectiveness report
    # -----------------------------------------------------------------

    def generate_attack_effectiveness_report(
        self,
        token_analysis: dict[str, Any],
        evolution_stats: dict[str, Any],
        output_path: Path | None = None,
    ) -> Path:
        """Create an HTML report on attack strategy effectiveness.

        *token_analysis* mirrors ``AnalysisReport`` fields.
        *evolution_stats* contains keys like ``generations``,
        ``best_fitness``, ``population_diversity``, ``by_category``.
        """
        out = output_path or (
            self.config.output_dir / "attack_effectiveness.html"
        )
        sections: list[tuple[str, str]] = []

        # -- token / n-gram analysis --
        top_tokens = token_analysis.get("top_success_tokens", [])
        if top_tokens:
            rows = "".join(
                f"<tr><td><code>{html.escape(str(t.get('token', '')))}</code></td>"
                f"<td>{t.get('success_count', 0)}</td>"
                f"<td>{t.get('total_count', 0)}</td>"
                f"<td>{_pct(t.get('success_rate', 0))}</td>"
                f"<td>{t.get('log_odds', 0):+.2f}</td></tr>"
                for t in top_tokens[:20]
            )
            table = (
                "<table><tr><th>Token</th><th>Success</th><th>Total</th>"
                "<th>Rate</th><th>Log-Odds</th></tr>" + rows + "</table>"
            )
            sections.append(("Top Success Tokens", table))

        bigrams = token_analysis.get("top_success_bigrams", [])
        if bigrams:
            rows_b = "".join(
                f"<tr><td><code>{html.escape(str(b.get('token', '')))}</code></td>"
                f"<td>{_pct(b.get('success_rate', 0))}</td></tr>"
                for b in bigrams[:15]
            )
            sections.append((
                "Top Success Bigrams",
                "<table><tr><th>Bigram</th><th>Success Rate</th></tr>"
                + rows_b + "</table>",
            ))

        # -- obfuscation effectiveness --
        obf = token_analysis.get("obfuscation_effectiveness", {})
        if obf:
            obf_data = sorted(obf.items(), key=lambda x: -x[1])
            chart = _svg_bar_chart(
                [(k, v) for k, v in obf_data],
                colour_fn=lambda v: _PALETTE[0],
            )
            sections.append(("Obfuscation Technique Rankings", chart))

        # -- evolutionary engine progress --
        gens = evolution_stats.get("generations", 0)
        best_fit = evolution_stats.get("best_fitness", 0)
        diversity = evolution_stats.get("population_diversity", 0)

        evo_metrics = (
            f'<div class="metric"><div class="val">{gens}</div>'
            f'<div class="lbl">Generations</div></div>'
            f'<div class="metric"><div class="val">{best_fit:.3f}</div>'
            f'<div class="lbl">Best Fitness</div></div>'
            f'<div class="metric"><div class="val">{_pct(diversity)}</div>'
            f'<div class="lbl">Population Diversity</div></div>'
        )
        sections.append(("Evolutionary Engine", evo_metrics))

        fitness_history = evolution_stats.get("fitness_history", [])
        if fitness_history:
            chart_f = _svg_line_chart(
                self._downsample(fitness_history),
                label="Best fitness per generation",
                colour=_PALETTE[4],
            )
            sections.append(("Fitness Over Generations", chart_f))

        # -- mutation category effectiveness --
        mut_cats = evolution_stats.get("by_category", {})
        if mut_cats:
            cat_data = sorted(mut_cats.items(), key=lambda x: -x[1])
            chart_c = _svg_bar_chart(
                cat_data,
                colour_fn=lambda v: _PALETTE[2] if v > 0.3 else _PALETTE[0],
            )
            sections.append(("Mutation Category Effectiveness", chart_c))

        title = f"{self.config.title_prefix} \u2014 Attack Effectiveness"
        return self._write(out, _render_html(title, sections))

    # -----------------------------------------------------------------
    # 4. Curriculum learning report
    # -----------------------------------------------------------------

    def generate_curriculum_report(
        self,
        curriculum_summary: dict[str, Any],
        output_path: Path | None = None,
    ) -> Path:
        """Create an HTML report on curriculum learning progress.

        *curriculum_summary* should contain ``stages`` (list of dicts with
        ``name``, ``description``, ``format``, ``examples_count``,
        ``passed_progression``, ``metrics``, ``learning_rate``, ``epochs``).
        """
        out = output_path or (
            self.config.output_dir / "curriculum_report.html"
        )
        sections: list[tuple[str, str]] = []
        stages = curriculum_summary.get("stages", [])

        # -- stage completion overview --
        completed = sum(1 for s in stages if s.get("passed_progression"))
        total = len(stages)
        overview = (
            f'<div class="metric"><div class="val">{completed}/{total}</div>'
            f'<div class="lbl">Stages Passed</div></div>'
        )
        sections.append(("Curriculum Progress", overview))

        # -- per-stage table --
        if stages:
            rows: list[str] = []
            for i, st in enumerate(stages, 1):
                name = st.get("name", f"stage_{i}")
                fmt = st.get("format", "?").upper()
                count = st.get("examples_count", 0)
                passed = st.get("passed_progression", False)
                desc = st.get("description", "")
                metrics = st.get("metrics", {})
                metric_str = ", ".join(
                    f"{k}={v:.3f}" for k, v in metrics.items()
                ) if metrics else "\u2014"

                badge_cls = "badge-green" if passed else "badge-red"
                badge_txt = "PASSED" if passed else "PENDING"
                rows.append(
                    f"<tr><td>{i}</td><td><strong>{html.escape(name)}</strong>"
                    f"<br><small>{html.escape(desc)}</small></td>"
                    f"<td>{fmt}</td><td>{count:,}</td>"
                    f"<td><code>{metric_str}</code></td>"
                    f'<td><span class="{badge_cls}">{badge_txt}</span></td></tr>'
                )
            table = (
                "<table><tr><th>#</th><th>Stage</th><th>Format</th>"
                "<th>Examples</th><th>Metrics</th><th>Status</th></tr>"
                + "".join(rows) + "</table>"
            )
            sections.append(("Stage Details", table))

        # -- dataset size bar chart --
        if stages:
            size_data = [
                (s.get("name", "?"), min(s.get("examples_count", 0) / max(
                    max(st.get("examples_count", 1) for st in stages), 1
                ), 1.0))
                for s in stages
            ]
            chart = _svg_bar_chart(
                size_data, colour_fn=lambda v: _PALETTE[0]
            )
            # Add raw counts below
            count_note = " | ".join(
                f"{s.get('name', '?')}: {s.get('examples_count', 0):,}"
                for s in stages
            )
            sections.append((
                "Dataset Sizes per Stage",
                chart + f'<p style="font-size:12px;color:#64748b">{count_note}</p>',
            ))

        # -- learning rate schedule --
        lr_points: list[float] = []
        lr_labels: list[str] = []
        for s in stages:
            lr = s.get("learning_rate", 0)
            epochs = s.get("epochs", 1)
            lr_labels.append(s.get("name", "?"))
            for _ in range(epochs):
                lr_points.append(lr)

        if len(lr_points) >= 2:
            # Normalise to [0, 1] for the chart
            lr_max = max(lr_points) or 1e-6
            normalised = [v / lr_max for v in lr_points]
            chart_lr = _svg_line_chart(
                normalised,
                label="Learning rate schedule (normalised)",
                colour=_PALETTE[3],
            )
            # Annotate actual values
            lr_note = " &rarr; ".join(
                f"{s.get('name', '?')}: {s.get('learning_rate', 0):.1e}"
                for s in stages
            )
            sections.append((
                "Learning Rate Schedule",
                chart_lr + f'<p style="font-size:12px;color:#64748b">{lr_note}</p>',
            ))

        # -- progression criteria --
        if stages:
            crit_rows: list[str] = []
            for s in stages:
                metric_name = s.get("progression_metric", "loss")
                threshold = s.get("progression_threshold", 0)
                metrics = s.get("metrics", {})
                actual = metrics.get(metric_name, None)
                if actual is not None:
                    badge = _progress_badge(actual, threshold)
                else:
                    badge = '<span style="color:#94a3b8">not evaluated</span>'
                crit_rows.append(
                    f"<tr><td>{html.escape(s.get('name', '?'))}</td>"
                    f"<td>{html.escape(metric_name)}</td>"
                    f"<td>{threshold}</td><td>{badge}</td></tr>"
                )
            crit_table = (
                "<table><tr><th>Stage</th><th>Metric</th>"
                "<th>Threshold</th><th>Status</th></tr>"
                + "".join(crit_rows) + "</table>"
            )
            sections.append(("Progression Criteria", crit_table))

        title = f"{self.config.title_prefix} \u2014 Curriculum Report"
        return self._write(out, _render_html(title, sections))

    # -----------------------------------------------------------------
    # 5. JSON report
    # -----------------------------------------------------------------

    def generate_json_report(
        self,
        data: dict[str, Any],
        output_path: Path | None = None,
    ) -> Path:
        """Write a structured JSON report to disk.

        Adds a ``_meta`` key with generation timestamp and config.
        """
        out = output_path or (self.config.output_dir / "report.json")
        payload = {
            "_meta": {
                "generated_at": time.strftime(
                    "%Y-%m-%dT%H:%M:%SZ", time.gmtime()
                ),
                "title_prefix": self.config.title_prefix,
                "include_raw_data": self.config.include_raw_data,
            },
            **data,
        }
        self._ensure_dir(out)
        out.write_text(
            json.dumps(payload, indent=2, default=str), encoding="utf-8"
        )
        return out
