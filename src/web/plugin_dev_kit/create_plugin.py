"""
Plugin scaffold generator.

Creates a fully-functional plugin directory from templates, with all
placeholder values substituted.  The generated plugin is immediately
loadable by the PluginRegistry.

Usage::

    # Programmatic
    from src.web.plugin_dev_kit.create_plugin import create_plugin
    path = create_plugin("my_plugin", display_name="My Plugin")

    # CLI
    python -m src.web.plugin_dev_kit.create_plugin my_plugin --display-name "My Plugin"
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path
from string import Template

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Where the templates live
# ---------------------------------------------------------------------------
_TEMPLATE_DIR = Path(__file__).parent / "template_plugin"

# ---------------------------------------------------------------------------
# Workflow stage mapping
# ---------------------------------------------------------------------------
_GROUP_TO_STAGE = {
    "CONFIGURE": "configure",
    "DESIGN": "design",
    "TRANSFORM": "transform",
    "ANALYZE": "analyze",
    "TEST": "test",
    "EVALUATE": "evaluate",
    "EXPORT": "export",
}


def create_plugin(
    name: str,
    *,
    display_name: str = "",
    api_prefix: str = "",
    nav_group: str = "DESIGN",
    order: int = 800,
    output_dir: Path | None = None,
) -> Path:
    """Generate a new plugin scaffold from the template.

    Parameters:
        name:         Plugin slug, e.g. ``my_custom_attack``.
        display_name: Human-readable name.  Defaults to title-cased slug.
        api_prefix:   API route prefix.  Defaults to ``/name`` with
                      underscores replaced by hyphens.
        nav_group:    Sidebar group (CONFIGURE, DESIGN, TRANSFORM, etc.)
        order:        Sort order within the nav group.
        output_dir:   Where to write the plugin.  Defaults to
                      ``src/web/plugins/{name}/``.

    Returns:
        Path to the generated plugin directory.
    """
    if not display_name:
        display_name = name.replace("_", " ").title()
    if not api_prefix:
        api_prefix = "/" + name.replace("_", "-")
    workflow_stage = _GROUP_TO_STAGE.get(nav_group.upper(), "design")

    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "plugins" / name

    if output_dir.exists():
        raise FileExistsError(f"Plugin directory already exists: {output_dir}")

    # Substitution context
    ctx = {
        "PLUGIN_ID": name,
        "DISPLAY_NAME": display_name,
        "API_PREFIX": api_prefix,
        "NAV_GROUP": nav_group.upper(),
        "WORKFLOW_STAGE": workflow_stage,
        "ORDER": str(order),
    }

    # Walk template_plugin/ and copy with substitution
    static_dir = output_dir / "static"
    static_dir.mkdir(parents=True, exist_ok=True)

    _render_template(_TEMPLATE_DIR / "__init__.py.tmpl", output_dir / "__init__.py", ctx)
    _render_template(_TEMPLATE_DIR / "routes.py.tmpl", output_dir / "routes.py", ctx)
    _render_template(_TEMPLATE_DIR / "static" / "fragment.html.tmpl", static_dir / "fragment.html", ctx)
    _render_template(_TEMPLATE_DIR / "static" / "fragment.js.tmpl", static_dir / "fragment.js", ctx)

    logger.info("Created plugin scaffold at %s", output_dir)
    return output_dir


def _render_template(src: Path, dst: Path, ctx: dict[str, str]) -> None:
    """Read a .tmpl file, substitute $PLACEHOLDERS, write to dst."""
    text = src.read_text(encoding="utf-8")
    rendered = Template(text).safe_substitute(ctx)
    dst.write_text(rendered, encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a new LLM Safety Framework plugin scaffold."
    )
    parser.add_argument("name", help="Plugin slug (e.g. my_custom_attack)")
    parser.add_argument("--display-name", default="", help="Human-readable name")
    parser.add_argument("--api-prefix", default="", help="API route prefix")
    parser.add_argument("--nav-group", default="DESIGN",
                        choices=list(_GROUP_TO_STAGE.keys()),
                        help="Sidebar navigation group")
    parser.add_argument("--order", type=int, default=800, help="Sort order")
    parser.add_argument("--output-dir", type=Path, default=None,
                        help="Output directory (default: src/web/plugins/<name>)")
    args = parser.parse_args()

    path = create_plugin(
        args.name,
        display_name=args.display_name,
        api_prefix=args.api_prefix,
        nav_group=args.nav_group,
        order=args.order,
        output_dir=args.output_dir,
    )
    print(f"Plugin created at: {path}")


if __name__ == "__main__":
    main()
