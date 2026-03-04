/* ================================================================
   Dimensional Matrix Plugin — JavaScript
   ================================================================ */
(function () {
  "use strict";

  const API = "/api/dimensional-matrix";

  /* ---- helpers ---- */
  const escHtml = (s) =>
    String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");

  async function api(path, opts) {
    const url = API + path;
    const res = await fetch(url, opts);
    if (!res.ok) {
      const text = await res.text();
      throw new Error(`${res.status}: ${text}`);
    }
    return res.json();
  }

  function riskColor(level) {
    const m = {
      minimal: "#4caf50",
      low: "#2196f3",
      moderate: "#ff9800",
      high: "#f44336",
      critical: "#d32f2f",
    };
    return m[level] || "#888";
  }

  function riskBadge(level) {
    return `<span style="background:${riskColor(level)};color:#fff;padding:4px 10px;border-radius:4px;font-weight:600;text-transform:uppercase;">${escHtml(level)}</span>`;
  }

  function assessmentColor(a) {
    if (a === "SAFE") return "#4caf50";
    if (a === "UNSAFE") return "#f44336";
    return "#ff9800";
  }

  /* Populate endpoint selectors from /api/endpoints/all/enabled */
  async function populateEndpointSelectors(selectors) {
    try {
      const data = await fetch("/api/endpoints/all/enabled").then((r) => r.json());
      const endpoints = data.endpoints || data || [];
      for (const sel of selectors) {
        const el = document.getElementById(sel.id);
        if (!el) continue;
        const first = el.options[0]?.text || "Endpoint...";
        el.innerHTML = `<option value="">${escHtml(first)}</option>`;
        for (const ep of endpoints) {
          el.innerHTML += `<option value="${escHtml(ep.id)}">${escHtml(ep.name || ep.id)}</option>`;
        }
        // Wire up model population on change
        if (sel.modelId) {
          el.addEventListener("change", () => {
            populateModels(el.value, sel.modelId, endpoints);
          });
        }
      }
    } catch (e) {
      console.warn("Failed to load endpoints:", e);
    }
  }

  function populateModels(endpointId, modelSelectId, endpoints) {
    const modelEl = document.getElementById(modelSelectId);
    if (!modelEl) return;
    modelEl.innerHTML = '<option value="">Model...</option>';
    if (!endpointId) return;
    const ep = endpoints.find((e) => e.id === endpointId);
    if (!ep || !ep.models) return;
    for (const m of ep.models) {
      if (m.enabled !== false) {
        modelEl.innerHTML += `<option value="${escHtml(m.model_id)}">${escHtml(m.model_id)}</option>`;
      }
    }
  }

  /* ================================================================
     1. Dimension Explorer
     ================================================================ */
  let _allDimensions = null;

  async function loadDimensions() {
    if (!_allDimensions) {
      _allDimensions = await api("/dimensions");
    }
    return _allDimensions;
  }

  async function renderDimensionExplorer() {
    const dims = await loadDimensions();
    const catFilter = document.getElementById("dim-exp-category").value;
    const search = (document.getElementById("dim-exp-search").value || "").toLowerCase();

    let filtered = dims;
    if (catFilter) filtered = filtered.filter((d) => d.category === catFilter);
    if (search) filtered = filtered.filter((d) => (d.id + " " + d.name + " " + d.description).toLowerCase().includes(search));

    document.getElementById("dim-exp-count").textContent = `${filtered.length} of ${dims.length} dimensions`;

    const catColors = { prompt: "#42a5f5", response: "#66bb6a", scenario: "#ffa726", systemic: "#ab47bc" };
    let html = "";
    for (const d of filtered) {
      const color = catColors[d.category] || "#888";
      html += `<div class="dim-card" onclick="showDimDetail('${d.id}')" style="border:1px solid #444;border-left:4px solid ${color};border-radius:6px;padding:12px;cursor:pointer;background:#1a1a1a;transition:background .15s;" onmouseover="this.style.background='#252525'" onmouseout="this.style.background='#1a1a1a'">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
          <span style="font-weight:700;font-size:1.05em;color:${color};">${escHtml(d.id)}</span>
          <span style="font-size:0.8em;background:#333;padding:2px 8px;border-radius:3px;color:#bbb;">${escHtml(d.category)}</span>
        </div>
        <div style="font-weight:600;margin-bottom:4px;">${escHtml(d.name)}</div>
        <div style="color:#aaa;font-size:0.9em;">${escHtml(d.description)}</div>
        ${d.ilo_indicator ? `<div style="margin-top:6px;font-size:0.8em;color:#ffa726;">ILO: ${escHtml(d.ilo_indicator)}</div>` : ""}
      </div>`;
    }
    document.getElementById("dim-exp-grid").innerHTML = html || '<p style="color:#888;">No dimensions match your filter.</p>';
  }

  window.showDimDetail = async function (dimId) {
    try {
      const d = await api(`/dimensions/${dimId}`);
      let levels = "";
      for (let i = 1; i <= 5; i++) {
        const desc = d.levels[String(i)] || "";
        const bg = `hsl(${120 - (i - 1) * 30}, 50%, 18%)`;
        levels += `<div style="display:flex;gap:8px;padding:6px 8px;border-radius:4px;margin-bottom:4px;background:${bg};">
          <span style="font-weight:700;min-width:20px;color:#fff;">${i}</span>
          <span style="color:#ddd;">${escHtml(desc)}</span>
        </div>`;
      }
      document.getElementById("dim-exp-modal-body").innerHTML = `
        <h3 style="color:#64b5f6;">${escHtml(d.id)}: ${escHtml(d.name)}</h3>
        <p style="color:#aaa;">${escHtml(d.description)}</p>
        ${d.ilo_indicator ? `<p style="color:#ffa726;">ILO Indicator: ${escHtml(d.ilo_indicator)}</p>` : ""}
        <h4 style="margin-top:16px;">Severity Rubric</h4>
        ${levels}`;
      document.getElementById("dim-exp-modal").style.display = "block";
    } catch (e) {
      console.error("Failed to load dimension:", e);
    }
  };

  /* ================================================================
     2. Dimensional Rater
     ================================================================ */
  let _raterEndpoints = null;

  async function initRater() {
    _raterEndpoints = [];
    try {
      const data = await fetch("/api/endpoints/all/enabled").then((r) => r.json());
      _raterEndpoints = data.endpoints || data || [];
    } catch (e) { /* no endpoints */ }

    await populateEndpointSelectors([
      { id: "rater-endpoint", modelId: "rater-model" },
    ]);
  }

  async function runRating() {
    const prompt = document.getElementById("rater-prompt").value.trim();
    const response = document.getElementById("rater-response").value.trim();
    const epId = document.getElementById("rater-endpoint").value;
    const modelId = document.getElementById("rater-model").value;

    if (!prompt || !response) return alert("Enter both prompt and response.");
    if (!epId) return alert("Select an endpoint.");

    const categories = [];
    if (document.getElementById("rater-cat-prompt").checked) categories.push("prompt");
    if (document.getElementById("rater-cat-response").checked) categories.push("response");
    if (document.getElementById("rater-cat-scenario").checked) categories.push("scenario");
    if (document.getElementById("rater-cat-systemic").checked) categories.push("systemic");

    document.getElementById("rater-status").textContent = "Rating in progress...";
    document.getElementById("rater-results").style.display = "none";

    try {
      const data = await api("/rate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt, response, endpoint_id: epId, model_id: modelId, categories }),
      });
      renderRatingResults(data);
    } catch (e) {
      document.getElementById("rater-status").textContent = "Error: " + e.message;
    }
  }

  function renderRatingResults(data) {
    document.getElementById("rater-status").textContent = `Rated ${data.score_count} dimensions.`;
    document.getElementById("rater-results").style.display = "block";

    document.getElementById("rater-risk-badge").innerHTML = riskBadge(data.risk_level);
    document.getElementById("rater-risk-score").textContent = `Overall risk: ${(data.overall_risk * 100).toFixed(1)}%`;

    // Score bars
    let bars = "";
    const scores = (data.scores || []).sort((a, b) => b.score - a.score);
    for (const s of scores) {
      const pct = (s.score / 5) * 100;
      const hue = 120 - (s.score - 1) * 30;
      bars += `<div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">
        <span style="min-width:30px;font-weight:600;color:#aaa;">${escHtml(s.dimension_id)}</span>
        <div style="flex:1;max-width:250px;height:16px;background:#333;border-radius:3px;overflow:hidden;">
          <div style="width:${pct}%;height:100%;background:hsl(${hue},60%,45%);border-radius:3px;"></div>
        </div>
        <span style="min-width:18px;font-weight:600;">${s.score}</span>
        <span style="color:#888;font-size:0.8em;max-width:250px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">${escHtml(s.justification || "")}</span>
      </div>`;
    }
    document.getElementById("rater-scores-chart").innerHTML = bars || "<p>No scores returned.</p>";

    // Category summary cards
    document.getElementById("rater-category-cards").innerHTML = "";
  }

  /* ================================================================
     3. Boundary Prober
     ================================================================ */
  async function initProber() {
    await populateEndpointSelectors([
      { id: "prober-endpoint", modelId: "prober-model" },
      { id: "prober-judge-endpoint", modelId: "prober-judge-model" },
    ]);
  }

  async function runProber() {
    const prompt = document.getElementById("prober-prompt").value.trim();
    const epId = document.getElementById("prober-endpoint").value;
    const modelId = document.getElementById("prober-model").value;
    const judgeEpId = document.getElementById("prober-judge-endpoint").value;
    const judgeModelId = document.getElementById("prober-judge-model").value;
    const dimsRaw = document.getElementById("prober-dims").value.trim();

    if (!prompt) return alert("Enter a probe prompt.");
    if (!epId) return alert("Select a target endpoint.");

    const body = { prompt, endpoint_id: epId, model_id: modelId };
    if (judgeEpId) body.judge_endpoint_id = judgeEpId;
    if (judgeModelId) body.judge_model_id = judgeModelId;
    if (dimsRaw) body.dimensions = dimsRaw.split(",").map((s) => s.trim()).filter(Boolean);

    document.getElementById("prober-status").textContent = "Probing boundaries...";
    document.getElementById("prober-results").style.display = "none";

    try {
      const data = await api("/probe", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });
      renderProbeResults(data);
    } catch (e) {
      document.getElementById("prober-status").textContent = "Error: " + e.message;
    }
  }

  function renderProbeResults(data) {
    document.getElementById("prober-status").textContent = "";
    document.getElementById("prober-results").style.display = "block";

    // Summary
    const weak = data.weakest_dimensions || [];
    const strong = data.strongest_dimensions || [];
    document.getElementById("prober-summary").innerHTML = `
      <div style="border:1px solid #f44336;border-radius:6px;padding:10px;flex:1;">
        <div style="font-weight:600;color:#f44336;margin-bottom:4px;">Weakest (most permissive)</div>
        <div style="color:#ddd;">${weak.map(escHtml).join(", ") || "—"}</div>
      </div>
      <div style="border:1px solid #4caf50;border-radius:6px;padding:10px;flex:1;">
        <div style="font-weight:600;color:#4caf50;margin-bottom:4px;">Strongest (strictest)</div>
        <div style="color:#ddd;">${strong.map(escHtml).join(", ") || "—"}</div>
      </div>`;

    // Boundary chart
    const summary = data.boundary_summary || {};
    let chart = "";
    for (const [dimId, threshold] of Object.entries(summary).sort((a, b) => (b[1] || 0) - (a[1] || 0))) {
      const level = threshold || 0;
      const pct = (level / 5) * 100;
      const hue = 120 - (level - 1) * 30;
      chart += `<div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">
        <span style="min-width:30px;font-weight:600;color:#aaa;">${escHtml(dimId)}</span>
        <div style="flex:1;max-width:300px;height:18px;background:#333;border-radius:3px;overflow:hidden;">
          <div style="width:${pct}%;height:100%;background:hsl(${hue},55%,45%);border-radius:3px;"></div>
        </div>
        <span style="font-weight:600;">${threshold !== null ? threshold : "?"}</span>
      </div>`;
    }
    document.getElementById("prober-chart").innerHTML = chart || "<p>No boundary data.</p>";
  }

  /* ================================================================
     4. Debate Arena
     ================================================================ */
  let _debateEndpoints = [];

  async function initDebate() {
    try {
      const data = await fetch("/api/endpoints/all/enabled").then((r) => r.json());
      _debateEndpoints = data.endpoints || data || [];
    } catch (e) { /* */ }

    await populateEndpointSelectors([
      { id: "debate-pros-endpoint", modelId: "debate-pros-model" },
      { id: "debate-def-endpoint", modelId: "debate-def-model" },
      { id: "debate-judge-endpoint", modelId: "debate-judge-model" },
    ]);
  }

  async function runDebate() {
    const prompt = document.getElementById("debate-prompt").value.trim();
    const response = document.getElementById("debate-response").value.trim();
    if (!prompt || !response) return alert("Enter both prompt and response.");

    const prosEp = document.getElementById("debate-pros-endpoint").value;
    const defEp = document.getElementById("debate-def-endpoint").value;
    const judgeEp = document.getElementById("debate-judge-endpoint").value;
    if (!prosEp || !defEp || !judgeEp) return alert("Select all three endpoints.");

    const body = {
      prompt,
      response,
      prosecutor_endpoint_id: prosEp,
      prosecutor_model_id: document.getElementById("debate-pros-model").value,
      defender_endpoint_id: defEp,
      defender_model_id: document.getElementById("debate-def-model").value,
      judge_endpoint_id: judgeEp,
      judge_model_id: document.getElementById("debate-judge-model").value,
      rounds: parseInt(document.getElementById("debate-rounds").value) || 1,
    };

    const dimIds = document.getElementById("debate-dim-ids").value.trim();
    if (dimIds) body.dimension_ids = dimIds.split(",").map((s) => s.trim()).filter(Boolean);

    document.getElementById("debate-status").textContent = "Debate in progress...";
    document.getElementById("debate-results").style.display = "none";

    try {
      const data = await api("/debate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });
      renderDebateResults(data);
    } catch (e) {
      document.getElementById("debate-status").textContent = "Error: " + e.message;
    }
  }

  function renderDebateResults(data) {
    document.getElementById("debate-status").textContent = "";
    document.getElementById("debate-results").style.display = "block";

    const v = data.verdict || {};
    const ac = assessmentColor(v.safety_assessment);
    const vulns = (v.vulnerabilities || []).map((x) => `<span style="background:#333;padding:2px 8px;border-radius:3px;font-size:0.85em;">${escHtml(x)}</span>`).join(" ");
    const dimFlags = Object.entries(v.dimensional_flags || {}).map(([k, val]) => `<span style="background:#333;padding:2px 8px;border-radius:3px;font-size:0.85em;">${escHtml(k)}: ${val}</span>`).join(" ");
    const recs = (v.recommendations || []).map((r) => `<li>${escHtml(r)}</li>`).join("");

    document.getElementById("debate-verdict-card").innerHTML = `
      <div style="display:flex;gap:16px;align-items:center;margin-bottom:12px;flex-wrap:wrap;">
        <span style="font-size:1.4em;font-weight:700;background:${ac};color:#fff;padding:6px 16px;border-radius:6px;">${escHtml(v.safety_assessment || "?")}</span>
        <span style="color:#aaa;">Winner: <strong style="color:#fff;">${escHtml(v.winner || "?")}</strong></span>
        <span style="color:#aaa;">Confidence: <strong style="color:#fff;">${((v.confidence || 0) * 100).toFixed(0)}%</strong></span>
      </div>
      ${v.judge_reasoning ? `<p style="color:#ddd;margin-bottom:12px;">${escHtml(v.judge_reasoning)}</p>` : ""}
      ${vulns ? `<div style="margin-bottom:8px;"><strong style="color:#f44336;">Vulnerabilities:</strong> ${vulns}</div>` : ""}
      ${dimFlags ? `<div style="margin-bottom:8px;"><strong style="color:#ffa726;">Dimensional Flags:</strong> ${dimFlags}</div>` : ""}
      ${v.strongest_prosecution_point ? `<div style="margin-bottom:4px;"><strong style="color:#e57373;">Prosecution:</strong> ${escHtml(v.strongest_prosecution_point)}</div>` : ""}
      ${v.strongest_defense_point ? `<div style="margin-bottom:4px;"><strong style="color:#81c784;">Defense:</strong> ${escHtml(v.strongest_defense_point)}</div>` : ""}
      ${recs ? `<div style="margin-top:8px;"><strong>Recommendations:</strong><ul style="margin:4px 0;">${recs}</ul></div>` : ""}`;

    // Transcript
    const roleColors = { prosecutor: "#e57373", defender: "#81c784", analyst: "#64b5f6", judge: "#ffa726" };
    let transcript = "";
    for (const t of data.turns || []) {
      const color = roleColors[t.role] || "#888";
      transcript += `<div style="border-left:3px solid ${color};padding:8px 12px;margin-bottom:10px;background:#1a1a1a;border-radius:0 4px 4px 0;">
        <div style="font-weight:600;color:${color};margin-bottom:4px;">${escHtml(t.role.toUpperCase())} <span style="color:#666;font-weight:400;font-size:0.85em;">(${escHtml(t.model_id)})</span></div>
        <div style="color:#ddd;white-space:pre-wrap;font-size:0.92em;">${escHtml(t.content)}</div>
      </div>`;
    }
    document.getElementById("debate-transcript").innerHTML = transcript;
  }

  window.loadDebateHistory = async function () {
    try {
      const results = await api("/debate/results");
      let html = "";
      for (const r of results) {
        const ac = assessmentColor(r.safety_assessment);
        html += `<div style="display:flex;gap:12px;align-items:center;padding:8px;border-bottom:1px solid #333;cursor:pointer;" onclick="viewDebateResult('${escHtml(r.filename)}')">
          <span style="background:${ac};color:#fff;padding:2px 8px;border-radius:3px;font-size:0.8em;min-width:80px;text-align:center;">${escHtml(r.safety_assessment)}</span>
          <span style="color:#ddd;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">${escHtml(r.prompt_preview)}</span>
          <span style="color:#666;font-size:0.8em;">${escHtml(r.timestamp ? r.timestamp.split("T")[0] : "")}</span>
        </div>`;
      }
      document.getElementById("debate-history").innerHTML = html || '<p style="color:#888;">No saved debates.</p>';
    } catch (e) {
      document.getElementById("debate-history").innerHTML = `<p style="color:#f44336;">${e.message}</p>`;
    }
  };

  window.viewDebateResult = async function (filename) {
    try {
      const data = await api(`/debate/results/${filename}`);
      renderDebateResults({
        verdict: data.verdict,
        turns: data.turns,
      });
      document.getElementById("debate-results").scrollIntoView({ behavior: "smooth" });
    } catch (e) {
      alert("Error: " + e.message);
    }
  };

  /* ================================================================
     Section Loaders
     ================================================================ */
  const SL = window.SECTION_LOADERS || {};

  SL["dimension-explorer"] = async function () {
    await renderDimensionExplorer();
    document.getElementById("dim-exp-btn").addEventListener("click", renderDimensionExplorer);
    document.getElementById("dim-exp-search").addEventListener("input", renderDimensionExplorer);
  };

  SL["dimensional-rater"] = async function () {
    await initRater();
    document.getElementById("rater-run-btn").addEventListener("click", runRating);
  };

  SL["boundary-prober"] = async function () {
    await initProber();
    document.getElementById("prober-run-btn").addEventListener("click", runProber);
  };

  SL["debate-arena"] = async function () {
    await initDebate();
    document.getElementById("debate-run-btn").addEventListener("click", runDebate);
    loadDebateHistory();
  };

  window.SECTION_LOADERS = SL;
})();
