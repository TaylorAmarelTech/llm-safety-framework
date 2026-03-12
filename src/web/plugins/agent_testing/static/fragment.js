/* Agent & Tool Testing Plugin — frontend logic */
(function () {
  "use strict";
  const API = "/api/agent-testing";

  // -------------------------------------------------------------------------
  // Helpers
  // -------------------------------------------------------------------------
  async function fetchJson(url, opts) {
    const resp = await fetch(url, opts);
    if (!resp.ok) throw new Error(`${resp.status}: ${await resp.text()}`);
    return resp.json();
  }
  function escHtml(s) {
    const d = document.createElement("div");
    d.textContent = s || "";
    return d.innerHTML;
  }

  // -------------------------------------------------------------------------
  // Scenarios tab
  // -------------------------------------------------------------------------
  async function loadScenarios() {
    try {
      const data = await fetchJson(`${API}/scenarios`);
      const container = document.getElementById("agent-scenario-cards");
      if (!container) return;
      container.innerHTML = Object.entries(data.categories || {}).map(([key, cat]) => `
        <div class="col-md-6 col-lg-3">
          <div class="card h-100">
            <div class="card-body">
              <h6 class="card-title">${escHtml(cat.name)}</h6>
              <p class="card-text small text-muted">${escHtml(cat.description)}</p>
              <div class="small"><strong>Sub-types:</strong>
                ${(cat.sub_types || []).map(st => `<span class="badge bg-secondary me-1">${escHtml(st)}</span>`).join("")}
              </div>
            </div>
          </div>
        </div>`).join("");
    } catch (e) { console.warn("loadScenarios:", e); }
  }

  async function loadTargetAgents() {
    try {
      const data = await fetchJson(`${API}/target-agents`);
      const agents = data.agents || [];
      ["agent-gen-target", "agent-run-target"].forEach(id => {
        const sel = document.getElementById(id);
        if (!sel) return;
        sel.innerHTML = agents.map(a =>
          `<option value="${escHtml(a.id)}">${escHtml(a.name)} (${escHtml(a.type)})</option>`
        ).join("");
      });
    } catch (e) { console.warn("loadTargetAgents:", e); }
  }

  async function loadChains() {
    try {
      const data = await fetchJson(`${API}/chains`);
      const container = document.getElementById("agent-chains-list");
      if (!container) return;
      if (!data.chains || data.chains.length === 0) {
        container.innerHTML = '<p class="text-muted small">No agent chains loaded yet.</p>';
        return;
      }
      container.innerHTML = `
        <div class="table-responsive"><table class="table table-sm table-striped">
        <thead><tr><th>ID</th><th>Name</th><th>Category</th><th>Steps</th><th>Difficulty</th><th>Corridors</th></tr></thead>
        <tbody>${data.chains.map(c => `<tr>
          <td class="small">${escHtml(c.id)}</td>
          <td>${escHtml(c.name)}</td>
          <td><span class="badge bg-info">${escHtml(c.category)}</span></td>
          <td>${c.step_count}</td>
          <td>${escHtml(c.difficulty)}</td>
          <td class="small">${(c.corridors || []).join(", ")}</td>
        </tr>`).join("")}</tbody></table></div>`;
    } catch (e) { console.warn("loadChains:", e); }
  }

  async function loadMutators() {
    try {
      const data = await fetchJson(`${API}/mutators`);
      const container = document.getElementById("agent-mutators-list");
      if (!container) return;
      const cats = data.categories || {};
      if (Object.keys(cats).length === 0) {
        container.innerHTML = '<p class="text-muted small">No agent mutators loaded yet.</p>';
        return;
      }
      container.innerHTML = Object.entries(cats).map(([cat, names]) => `
        <div class="mb-2">
          <strong>${escHtml(cat)}</strong> (${names.length} mutators):
          <span class="small">${names.map(n => `<span class="badge bg-secondary me-1">${escHtml(n)}</span>`).join("")}</span>
        </div>`).join("");
    } catch (e) { console.warn("loadMutators:", e); }
  }

  // Generate prompts
  function setupGenerate() {
    const btn = document.getElementById("agent-gen-btn");
    if (!btn) return;
    btn.addEventListener("click", async () => {
      btn.disabled = true;
      btn.textContent = "Generating...";
      try {
        const body = {
          category: document.getElementById("agent-gen-category").value,
          target_agent: document.getElementById("agent-gen-target").value,
          count: parseInt(document.getElementById("agent-gen-count").value) || 5,
        };
        const data = await fetchJson(`${API}/generate`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(body),
        });
        const container = document.getElementById("agent-generated-prompts");
        if (container) {
          container.innerHTML = `<div class="alert alert-success">Generated ${data.generated} prompts</div>` +
            (data.prompts || []).map(p => `
              <div class="card mb-2"><div class="card-body small">
                <div class="d-flex justify-content-between mb-1">
                  <strong>${escHtml(p.id)}</strong>
                  <span class="badge bg-primary">${escHtml(p.category)}</span>
                </div>
                <pre style="white-space:pre-wrap;max-height:200px;overflow:auto;">${escHtml(p.prompt)}</pre>
              </div></div>`).join("");
        }
      } catch (e) {
        const container = document.getElementById("agent-generated-prompts");
        if (container) container.innerHTML = `<div class="alert alert-danger">${escHtml(e.message)}</div>`;
      } finally {
        btn.disabled = false;
        btn.textContent = "Generate";
      }
    });
  }

  // -------------------------------------------------------------------------
  // Results tab
  // -------------------------------------------------------------------------
  async function loadStats() {
    try {
      const data = await fetchJson(`${API}/stats`);
      const container = document.getElementById("agent-stats-cards");
      if (!container) return;
      container.innerHTML = `
        <div class="col-md-3"><div class="card text-center"><div class="card-body">
          <h3>${data.total_prompts || 0}</h3><small class="text-muted">Total Prompts</small>
        </div></div></div>
        <div class="col-md-3"><div class="card text-center"><div class="card-body">
          <h3>${data.total_results || 0}</h3><small class="text-muted">Test Results</small>
        </div></div></div>
        <div class="col-md-3"><div class="card text-center"><div class="card-body">
          <h3>${data.total_ratings || 0}</h3><small class="text-muted">Ratings</small>
        </div></div></div>
        <div class="col-md-3"><div class="card text-center"><div class="card-body">
          <h3>${Object.keys(data.by_category || {}).length}</h3><small class="text-muted">Categories Tested</small>
        </div></div></div>`;

      // Dimension averages
      const heatmap = document.getElementById("agent-dimension-heatmap");
      if (heatmap) {
        const avgs = data.dimension_averages || {};
        if (Object.keys(avgs).length === 0) {
          heatmap.innerHTML = '<p class="text-muted small">No dimension ratings yet.</p>';
        } else {
          heatmap.innerHTML = `<div class="d-flex gap-2 flex-wrap">${
            Object.entries(avgs).map(([dim, avg]) => {
              const color = avg <= 2 ? "success" : avg <= 3.5 ? "warning" : "danger";
              return `<div class="text-center p-2 rounded bg-${color} bg-opacity-25" style="min-width:80px;">
                <strong>${escHtml(dim)}</strong><br><span class="fs-5">${avg}</span>
              </div>`;
            }).join("")
          }</div>`;
        }
      }
    } catch (e) { console.warn("loadStats:", e); }
  }

  // -------------------------------------------------------------------------
  // Init
  // -------------------------------------------------------------------------
  function init() {
    loadScenarios();
    loadTargetAgents();
    loadChains();
    loadMutators();
    setupGenerate();

    // Results tab refresh
    const refreshBtn = document.getElementById("agent-refresh-stats");
    if (refreshBtn) refreshBtn.addEventListener("click", loadStats);

    // Load stats on first visit to results
    const observer = new MutationObserver(() => {
      const section = document.getElementById("section-agent-results");
      if (section && section.style.display !== "none") loadStats();
    });
    const target = document.getElementById("section-agent-results");
    if (target) observer.observe(target, { attributes: true, attributeFilter: ["style"] });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
