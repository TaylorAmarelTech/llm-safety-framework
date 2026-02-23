/* Chain Detection plugin — JS for all 4 tabs */
(function () {
  "use strict";
  const API = "/api/chain-detection";
  const escHtml = (s) =>
    String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");

  const GRADE_COLORS = ["#dc3545", "#fd7e14", "#ffc107", "#198754", "#0d6efd"];
  const GRADE_LABELS = ["BLIND", "PARTIAL", "AWARE", "COMPETENT", "EXPERT"];
  const DIFFICULTY_COLORS = {
    easy: "#198754",
    medium: "#ffc107",
    hard: "#fd7e14",
    expert: "#dc3545",
  };

  /* ===== Helpers ===== */
  async function api(path, opts) {
    const r = await fetch(API + path, opts);
    if (!r.ok) {
      const err = await r.text();
      throw new Error(err);
    }
    return r.json();
  }

  function badge(text, color) {
    return `<span style="display:inline-block;padding:2px 8px;border-radius:4px;font-size:0.75rem;font-weight:600;background:${color};color:#fff;">${escHtml(text)}</span>`;
  }

  function gradeBadge(grade) {
    return badge(GRADE_LABELS[grade] || grade, GRADE_COLORS[grade] || "#666");
  }

  function diffBadge(d) {
    return badge(d, DIFFICULTY_COLORS[d] || "#666");
  }

  /* ===== Chain Library ===== */
  const SECTION_LOADERS = window.SECTION_LOADERS || {};

  SECTION_LOADERS["section-chain-library"] = async function () {
    // Load categories for filter
    try {
      const cats = await api("/categories");
      const sel = document.getElementById("chain-filter-category");
      if (sel) {
        sel.innerHTML = '<option value="">All Categories</option>';
        for (const [k, v] of Object.entries(cats)) {
          sel.innerHTML += `<option value="${escHtml(k)}">${escHtml(k)} (${v})</option>`;
        }
      }
    } catch (e) {
      console.warn("Failed to load categories:", e);
    }

    // Load stats
    try {
      const stats = await api("/seeds/stats");
      const bar = document.getElementById("chain-stats-bar");
      if (bar) {
        bar.innerHTML =
          `<span><strong>${stats.total_chains}</strong> chains</span>` +
          `<span><strong>${stats.total_steps}</strong> total steps</span>` +
          `<span><strong>${stats.corridors?.length || 0}</strong> corridors</span>` +
          Object.entries(stats.categories || {})
            .map(([k, v]) => `<span>${escHtml(k)}: ${v}</span>`)
            .join("");
      }
    } catch (e) {
      console.warn("Failed to load stats:", e);
    }

    await loadChainList();

    // Filter button
    const btn = document.getElementById("chain-filter-btn");
    if (btn) btn.onclick = loadChainList;

    // Close modal
    const closeBtn = document.getElementById("chain-detail-close");
    if (closeBtn) closeBtn.onclick = () => {
      document.getElementById("chain-detail-modal").style.display = "none";
    };
  };

  async function loadChainList() {
    const cat = document.getElementById("chain-filter-category")?.value || "";
    const diff = document.getElementById("chain-filter-difficulty")?.value || "";
    const search = document.getElementById("chain-filter-search")?.value || "";

    let qs = "?";
    if (cat) qs += `category=${encodeURIComponent(cat)}&`;
    if (diff) qs += `difficulty=${encodeURIComponent(diff)}&`;
    if (search) qs += `search=${encodeURIComponent(search)}&`;

    try {
      const chains = await api("/chains" + qs);
      const list = document.getElementById("chain-list");
      if (!list) return;

      if (chains.length === 0) {
        list.innerHTML =
          '<div class="col-12 text-center text-muted py-4">No chains found</div>';
        return;
      }

      list.innerHTML = chains
        .map(
          (c) => `
        <div class="col-md-6 col-lg-4">
          <div class="card p-3 h-100" style="cursor:pointer;" data-chain-id="${escHtml(c.id)}">
            <div class="d-flex justify-content-between align-items-start mb-2">
              <h6 class="mb-0" style="font-size:0.9rem;">${escHtml(c.name)}</h6>
              ${diffBadge(c.difficulty)}
            </div>
            <div class="small text-muted mb-2">${escHtml(c.category)} &middot; ${c.step_count} steps &middot; ${(c.corridors || []).join(", ")}</div>
            <div class="small">${escHtml(c.emergent_risk?.substring(0, 120))}${c.emergent_risk?.length > 120 ? "..." : ""}</div>
          </div>
        </div>
      `
        )
        .join("");

      // Click handlers
      list.querySelectorAll("[data-chain-id]").forEach((el) => {
        el.onclick = () => showChainDetail(el.dataset.chainId);
      });
    } catch (e) {
      console.error("Failed to load chains:", e);
    }
  }

  async function showChainDetail(chainId) {
    try {
      const c = await api("/chains/" + chainId);
      const content = document.getElementById("chain-detail-content");
      if (!content) return;

      const stepsHtml = c.steps
        .map(
          (s, i) => `
        <div class="mb-3 p-2 rounded" style="background:var(--bg-secondary,#f8f9fa);">
          <div class="d-flex justify-content-between">
            <strong>Step ${i + 1}: ${escHtml(s.id)}</strong>
            ${s.sector ? `<span class="small text-muted">${escHtml(s.sector)}</span>` : ""}
          </div>
          <div class="mt-1">${escHtml(s.description)}</div>
          <div class="mt-1 small"><strong>Legal basis:</strong> ${escHtml(s.legal_basis)}</div>
          <div class="mt-1 small text-danger"><strong>Red flag:</strong> ${escHtml(s.red_flag_context)}</div>
        </div>
      `
        )
        .join("");

      const pe = c.palermo_elements || {};
      content.innerHTML = `
        <h4>${escHtml(c.name)}</h4>
        <div class="mb-2">${diffBadge(c.difficulty)} <span class="ms-2 small text-muted">${escHtml(c.category)} &middot; ${(c.corridors || []).join(", ")}</span></div>
        <div class="mb-3"><strong>Emergent risk:</strong> ${escHtml(c.emergent_risk)}</div>
        <div class="mb-3"><strong>Chain context:</strong> ${escHtml(c.chain_context)}</div>
        <h5>Steps (${c.steps.length})</h5>
        ${stepsHtml}
        <div class="mt-3 small">
          <strong>Palermo elements:</strong>
          Act: ${(pe.act || []).join(", ")} |
          Means: ${(pe.means || []).join(", ")} |
          Purpose: ${(pe.purpose || []).join(", ")}
        </div>
        <div class="mt-2 small text-muted">
          <strong>Sources:</strong> ${(c.source_references || []).join("; ")}
        </div>
      `;

      document.getElementById("chain-detail-modal").style.display = "block";
    } catch (e) {
      console.error("Failed to load chain detail:", e);
    }
  }

  /* ===== Chain Runner ===== */
  SECTION_LOADERS["section-chain-runner"] = async function () {
    // Load chains into select
    try {
      const chains = await api("/chains");
      const sel = document.getElementById("runner-chain-select");
      if (sel) {
        sel.innerHTML = chains
          .map(
            (c) =>
              `<option value="${escHtml(c.id)}">${escHtml(c.name)} (${escHtml(c.category)})</option>`
          )
          .join("");
      }

      // Also populate batch category
      const cats = await api("/categories");
      const batchCat = document.getElementById("runner-batch-category");
      if (batchCat) {
        batchCat.innerHTML = '<option value="">All Categories</option>';
        for (const [k, v] of Object.entries(cats)) {
          batchCat.innerHTML += `<option value="${escHtml(k)}">${escHtml(k)} (${v})</option>`;
        }
      }
    } catch (e) {
      console.warn("Failed to load chains for runner:", e);
    }

    // Load endpoints
    try {
      const endpoints = await fetch("/api/endpoints/all/enabled").then((r) =>
        r.json()
      );
      const epSel = document.getElementById("runner-endpoint-select");
      const mdSel = document.getElementById("runner-model-select");
      if (epSel && endpoints.length > 0) {
        epSel.innerHTML = endpoints
          .map(
            (ep) =>
              `<option value="${escHtml(ep.id)}" data-models='${escHtml(JSON.stringify(ep.models || []))}'>${escHtml(ep.name || ep.id)}</option>`
          )
          .join("");
        epSel.onchange = function () {
          const opt = this.selectedOptions[0];
          const models = JSON.parse(opt?.dataset.models || "[]");
          if (mdSel) {
            mdSel.innerHTML = models
              .map(
                (m) =>
                  `<option value="${escHtml(m.model_id || m.id)}">${escHtml(m.display_name || m.model_id || m.id)}</option>`
              )
              .join("");
          }
        };
        epSel.dispatchEvent(new Event("change"));
      }
    } catch (e) {
      console.warn("Failed to load endpoints:", e);
    }

    // Run single
    document.getElementById("runner-single-btn").onclick = runSingleTest;
    // Run batch
    document.getElementById("runner-batch-btn").onclick = runBatchTest;
  };

  async function runSingleTest() {
    const btn = document.getElementById("runner-single-btn");
    const output = document.getElementById("runner-output");
    const result = document.getElementById("runner-result");
    const progress = document.getElementById("runner-progress");

    btn.disabled = true;
    output.style.display = "block";
    progress.innerHTML = '<div class="spinner-border spinner-border-sm"></div> Running test...';
    result.innerHTML = "";

    try {
      const data = await api("/tests/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          chain_id:
            document.getElementById("runner-chain-select")?.value || "",
          test_mode:
            document.getElementById("runner-mode-select")?.value || "direct",
          model_id:
            document.getElementById("runner-model-select")?.value || "",
          endpoint_id:
            document.getElementById("runner-endpoint-select")?.value || "",
          use_judge:
            document.getElementById("runner-use-judge")?.checked || false,
        }),
      });

      progress.innerHTML = "Test complete!";
      result.innerHTML = renderSingleResult(data);
    } catch (e) {
      progress.innerHTML = `<span class="text-danger">Error: ${escHtml(e.message)}</span>`;
    }
    btn.disabled = false;
  }

  async function runBatchTest() {
    const btn = document.getElementById("runner-batch-btn");
    const output = document.getElementById("runner-output");
    const result = document.getElementById("runner-result");
    const progress = document.getElementById("runner-progress");

    btn.disabled = true;
    output.style.display = "block";
    progress.innerHTML = '<div class="spinner-border spinner-border-sm"></div> Running batch...';
    result.innerHTML = "";

    // Collect selected modes
    const modes = [];
    document
      .querySelectorAll("#runner-batch-modes input:checked")
      .forEach((cb) => modes.push(cb.value));

    // Get chain IDs for selected category
    const cat =
      document.getElementById("runner-batch-category")?.value || "";
    let chainIds = [];
    if (cat) {
      const chains = await api("/chains?category=" + encodeURIComponent(cat));
      chainIds = chains.map((c) => c.id);
    }

    try {
      const data = await api("/tests/batch", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          chain_ids: chainIds,
          test_modes: modes.length > 0 ? modes : ["direct"],
          model_id:
            document.getElementById("runner-model-select")?.value || "",
          endpoint_id:
            document.getElementById("runner-endpoint-select")?.value || "",
          max_chains: parseInt(
            document.getElementById("runner-batch-max")?.value || "10"
          ),
          use_judge: false,
        }),
      });

      progress.innerHTML = `Batch complete: ${data.total} tests run`;
      result.innerHTML = (data.results || [])
        .map((r) => renderSingleResult(r))
        .join("<hr>");
    } catch (e) {
      progress.innerHTML = `<span class="text-danger">Error: ${escHtml(e.message)}</span>`;
    }
    btn.disabled = false;
  }

  function renderSingleResult(r) {
    const s = r.score || {};
    return `
      <div class="mb-3 p-3 rounded" style="border-left:4px solid ${GRADE_COLORS[s.grade] || "#666"};">
        <div class="d-flex justify-content-between align-items-center mb-2">
          <div>
            ${gradeBadge(s.grade)}
            <span class="ms-2 small">${escHtml(r.test_case?.test_mode || "")} &middot; ${escHtml(r.model_id || "")}</span>
          </div>
          <span class="small text-muted">${r.duration_ms || 0}ms</span>
        </div>
        <div class="small mb-1">
          <strong>Chain detected:</strong> ${s.chain_detected ? "Yes" : "No"}
          &middot; <strong>Confidence:</strong> ${((s.confidence || 0) * 100).toFixed(0)}%
          &middot; <strong>Steps identified:</strong> ${(s.steps_identified || []).length}/${r.test_case?.chain_id ? "?" : 0}
        </div>
        <div class="small mb-1"><strong>Reasoning:</strong> ${escHtml(s.reasoning_quality || "N/A")}</div>
        ${s.missed_indicators?.length ? `<div class="small text-danger"><strong>Missed:</strong> ${(s.missed_indicators || []).map((m) => escHtml(m)).join("; ")}</div>` : ""}
        <details class="mt-2">
          <summary class="small">Full Response</summary>
          <pre class="mt-1 p-2 rounded" style="background:var(--bg-secondary,#f8f9fa);white-space:pre-wrap;font-size:0.75rem;max-height:400px;overflow-y:auto;">${escHtml(r.response || "")}</pre>
        </details>
      </div>
    `;
  }

  /* ===== Chain Results ===== */
  SECTION_LOADERS["section-chain-results"] = async function () {
    await loadResults();
    document.getElementById("results-refresh-btn").onclick = loadResults;
  };

  async function loadResults() {
    const model =
      document.getElementById("results-filter-model")?.value || "";
    const mode =
      document.getElementById("results-filter-mode")?.value || "";
    let qs = "?limit=100";
    if (model) qs += `&model_id=${encodeURIComponent(model)}`;
    if (mode) qs += `&test_mode=${encodeURIComponent(mode)}`;

    // Load analytics
    try {
      const summary = await api("/analytics/summary");
      const analytics = document.getElementById("results-analytics");
      if (analytics && summary.total_tests > 0) {
        analytics.innerHTML = `
          <div class="col-sm-3"><div class="card p-2 text-center"><div class="h4 mb-0">${summary.total_tests}</div><div class="small text-muted">Total Tests</div></div></div>
          <div class="col-sm-3"><div class="card p-2 text-center"><div class="h4 mb-0">${summary.average_grade?.toFixed(1) || "—"}</div><div class="small text-muted">Avg Grade</div></div></div>
          <div class="col-sm-3"><div class="card p-2 text-center"><div class="h4 mb-0">${((summary.detection_rate || 0) * 100).toFixed(0)}%</div><div class="small text-muted">Detection Rate</div></div></div>
          <div class="col-sm-3"><div class="card p-2 text-center">
            <div class="d-flex justify-content-center gap-1">
              ${Object.entries(summary.grade_distribution || {}).map(([label, count]) => `<span class="small">${escHtml(label)}: ${count}</span>`).join(" ")}
            </div>
            <div class="small text-muted">Grade Distribution</div>
          </div></div>
        `;
      } else if (analytics) {
        analytics.innerHTML =
          '<div class="col-12 text-center text-muted py-3">No test results yet. Run some tests first!</div>';
      }
    } catch (e) {
      console.warn("Failed to load analytics:", e);
    }

    // Load results
    try {
      const results = await api("/tests/results" + qs);
      const list = document.getElementById("results-list");
      if (!list) return;

      if (results.length === 0) {
        list.innerHTML =
          '<div class="text-center text-muted py-4">No results found</div>';
        return;
      }

      // Populate model filter from results
      const models = [...new Set(results.map((r) => r.model_id))];
      const modelSel = document.getElementById("results-filter-model");
      if (modelSel && modelSel.options.length <= 1) {
        models.forEach((m) => {
          modelSel.innerHTML += `<option value="${escHtml(m)}">${escHtml(m)}</option>`;
        });
      }

      list.innerHTML = results
        .map(
          (r) => `
        <div class="card mb-2 p-2">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              ${gradeBadge(r.grade)}
              <span class="ms-2 small">${escHtml(r.chain_id)} &middot; ${escHtml(r.test_mode)} &middot; ${escHtml(r.model_id)}</span>
            </div>
            <div class="small text-muted">
              ${r.chain_detected ? "Chain detected" : "Chain missed"}
              &middot; ${r.duration_ms}ms
              &middot; ${new Date(r.timestamp).toLocaleString()}
            </div>
          </div>
        </div>
      `
        )
        .join("");
    } catch (e) {
      console.error("Failed to load results:", e);
    }
  }

  /* ===== Chain Builder ===== */
  let builderStepCount = 0;

  SECTION_LOADERS["section-chain-builder"] = async function () {
    builderStepCount = 0;
    document.getElementById("builder-steps").innerHTML = "";
    addBuilderStep();
    addBuilderStep();

    document.getElementById("builder-add-step").onclick = addBuilderStep;
    document.getElementById("builder-save-btn").onclick = saveCustomChain;
  };

  function addBuilderStep() {
    builderStepCount++;
    const n = builderStepCount;
    const container = document.getElementById("builder-steps");
    const div = document.createElement("div");
    div.className = "mb-3 p-2 rounded";
    div.style.background = "var(--bg-secondary, #f8f9fa)";
    div.id = `builder-step-${n}`;
    div.innerHTML = `
      <div class="d-flex justify-content-between align-items-center mb-1">
        <strong>Step ${n}</strong>
        <button class="btn btn-sm btn-outline-danger" onclick="this.closest('[id^=builder-step]').remove()">Remove</button>
      </div>
      <div class="mb-1">
        <input type="text" class="form-control form-control-sm step-desc" placeholder="Description — what happens at this step">
      </div>
      <div class="mb-1">
        <input type="text" class="form-control form-control-sm step-legal" placeholder="Legal basis — why this is legal in isolation">
      </div>
      <div class="mb-1">
        <input type="text" class="form-control form-control-sm step-redflag" placeholder="Red flag context — why this is suspicious in the chain">
      </div>
      <div class="row g-2">
        <div class="col-6"><input type="text" class="form-control form-control-sm step-sector" placeholder="Sector (e.g. domestic_work)"></div>
        <div class="col-6"><input type="text" class="form-control form-control-sm step-corridor" placeholder="Corridor (e.g. PH-SA)"></div>
      </div>
    `;
    container.appendChild(div);
  }

  async function saveCustomChain() {
    const status = document.getElementById("builder-status");
    const name = document.getElementById("builder-name")?.value?.trim();
    if (!name) {
      status.textContent = "Name is required";
      return;
    }

    const steps = [];
    document
      .querySelectorAll("#builder-steps [id^=builder-step]")
      .forEach((el, i) => {
        const desc = el.querySelector(".step-desc")?.value?.trim();
        if (!desc) return;
        steps.push({
          id: `custom_s${i + 1}`,
          description: desc,
          legal_basis: el.querySelector(".step-legal")?.value?.trim() || "",
          red_flag_context:
            el.querySelector(".step-redflag")?.value?.trim() || "",
          sector: el.querySelector(".step-sector")?.value?.trim() || null,
          corridor: el.querySelector(".step-corridor")?.value?.trim() || null,
          indicator_action_ids: [],
        });
      });

    if (steps.length < 2) {
      status.textContent = "At least 2 steps required";
      return;
    }

    const corridors = (
      document.getElementById("builder-corridors")?.value || ""
    )
      .split(",")
      .map((s) => s.trim())
      .filter(Boolean);

    try {
      const res = await api("/chains", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: name,
          category:
            document.getElementById("builder-category")?.value || "custom",
          steps: steps,
          chain_context:
            document.getElementById("builder-context")?.value?.trim() || "",
          emergent_risk:
            document.getElementById("builder-risk")?.value?.trim() || "",
          difficulty:
            document.getElementById("builder-difficulty")?.value || "medium",
          corridors: corridors,
          source_references: [],
          palermo_elements: {},
        }),
      });

      status.innerHTML = `<span class="text-success">Saved! ID: ${escHtml(res.id)}</span>`;
    } catch (e) {
      status.innerHTML = `<span class="text-danger">Error: ${escHtml(e.message)}</span>`;
    }
  }
})();
