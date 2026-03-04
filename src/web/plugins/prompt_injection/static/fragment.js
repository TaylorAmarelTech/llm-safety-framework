/* Prompt Injection plugin — JS for all 4 tabs */
(function () {
  "use strict";
  const API = "/api/prompt-injection";
  const escHtml = (s) =>
    String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");

  const CATEGORY_COLORS = {
    instruction_override: "#dc3545",
    encoding_format: "#0d6efd",
    obfuscation: "#6f42c1",
    social_engineering: "#fd7e14",
    context_manipulation: "#198754",
    hybrid: "#20c997",
    output_evasion: "#6610f2",
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

  function catBadge(cat) {
    return badge(cat, CATEGORY_COLORS[cat] || "#666");
  }

  function copyToClipboard(text, btnEl) {
    navigator.clipboard.writeText(text).then(function () {
      if (btnEl) {
        var orig = btnEl.textContent;
        btnEl.textContent = "Copied!";
        setTimeout(function () { btnEl.textContent = orig; }, 1200);
      }
    });
  }

  /* Shared mutator cache */
  var _cachedMutators = null;
  async function fetchMutators(category, search) {
    var qs = "?";
    if (category) qs += "category=" + encodeURIComponent(category) + "&";
    if (search) qs += "search=" + encodeURIComponent(search) + "&";
    return api("/mutators" + qs);
  }
  async function getAllMutators() {
    if (!_cachedMutators) _cachedMutators = await api("/mutators");
    return _cachedMutators;
  }

  /* ===================================================================
   * Mutator Library
   * =================================================================== */
  const SECTION_LOADERS = window.SECTION_LOADERS || {};

  SECTION_LOADERS["section-mutator-library"] = async function () {
    /* Populate category filter */
    try {
      var cats = await api("/categories");
      var sel = document.getElementById("pi-lib-category");
      if (sel) {
        sel.innerHTML = '<option value="">All Categories</option>';
        for (var k in cats) {
          sel.innerHTML += '<option value="' + escHtml(k) + '">' + escHtml(k) + " (" + cats[k] + ")</option>";
        }
      }
    } catch (e) {
      console.warn("Failed to load categories:", e);
    }

    /* Populate stats bar */
    try {
      var stats = await api("/stats");
      var bar = document.getElementById("pi-lib-stats");
      if (bar) {
        bar.innerHTML =
          "<span><strong>" + stats.total_mutators + "</strong> mutators</span>" +
          "<span><strong>" + stats.category_count + "</strong> categories</span>" +
          "<span><strong>" + stats.deterministic + "</strong> deterministic</span>" +
          "<span><strong>" + stats.requires_llm + "</strong> require LLM</span>" +
          "<span><strong>" + stats.saved_batches + "</strong> saved batches</span>";
      }
    } catch (e) {
      console.warn("Failed to load stats:", e);
    }

    await loadMutatorGrid();

    var btn = document.getElementById("pi-lib-filter-btn");
    if (btn) btn.onclick = loadMutatorGrid;

    var closeBtn = document.getElementById("pi-lib-modal-close");
    if (closeBtn) closeBtn.onclick = function () {
      document.getElementById("pi-lib-modal").style.display = "none";
    };
  };

  async function loadMutatorGrid() {
    var cat = document.getElementById("pi-lib-category");
    var search = document.getElementById("pi-lib-search");
    var catVal = cat ? cat.value : "";
    var searchVal = search ? search.value : "";

    try {
      var mutators = await fetchMutators(catVal, searchVal);
      var grid = document.getElementById("pi-lib-grid");
      if (!grid) return;

      if (mutators.length === 0) {
        grid.innerHTML = '<div class="col-12 text-center text-muted py-4">No mutators found</div>';
        return;
      }

      /* Group by category */
      var grouped = {};
      for (var i = 0; i < mutators.length; i++) {
        var m = mutators[i];
        if (!grouped[m.category]) grouped[m.category] = [];
        grouped[m.category].push(m);
      }

      var html = "";
      for (var gcat in grouped) {
        html += '<div class="col-12 mt-2"><h5>' + catBadge(gcat) + " <span class=\"small text-muted ms-1\">" + grouped[gcat].length + " mutators</span></h5></div>";
        for (var j = 0; j < grouped[gcat].length; j++) {
          var mu = grouped[gcat][j];
          html += '<div class="col-md-6 col-lg-4">';
          html += '<div class="card p-3 h-100" style="cursor:pointer;" data-mutator-name="' + escHtml(mu.name) + '">';
          html += '<div class="d-flex justify-content-between align-items-start mb-1">';
          html += '<h6 class="mb-0" style="font-size:0.85rem;">' + escHtml(mu.name) + "</h6>";
          if (mu.requires_llm) html += '<span class="badge bg-warning text-dark" style="font-size:0.65rem;">LLM</span>';
          html += "</div>";
          html += '<div class="small text-muted">' + escHtml(mu.description || "No description") + "</div>";
          html += "</div></div>";
        }
      }
      grid.innerHTML = html;

      /* Click handler for detail */
      grid.querySelectorAll("[data-mutator-name]").forEach(function (el) {
        el.onclick = function () { showMutatorDetail(el.dataset.mutatorName); };
      });
    } catch (e) {
      console.error("Failed to load mutators:", e);
    }
  }

  async function showMutatorDetail(name) {
    try {
      var m = await api("/mutators/" + encodeURIComponent(name));
      var content = document.getElementById("pi-lib-modal-content");
      if (!content) return;
      content.innerHTML =
        "<h4>" + escHtml(m.name) + "</h4>" +
        '<div class="mb-2">' + catBadge(m.category) +
        (m.requires_llm ? ' <span class="badge bg-warning text-dark ms-1">Requires LLM</span>' : ' <span class="badge bg-success ms-1">Deterministic</span>') +
        "</div>" +
        '<div class="mb-3">' + escHtml(m.description) + "</div>" +
        '<div class="small text-muted"><strong>Class:</strong> ' + escHtml(m.class) + "</div>" +
        '<div class="small text-muted"><strong>Module:</strong> ' + escHtml(m.module) + "</div>" +
        '<hr><button class="btn btn-sm btn-outline-primary pi-try-mutator" data-name="' + escHtml(m.name) + '">Try in Mutation Lab</button>';

      content.querySelector(".pi-try-mutator").onclick = function () {
        document.getElementById("pi-lib-modal").style.display = "none";
        /* Switch to Mutation Lab tab */
        if (window.showSection) window.showSection("mutation-lab");
      };

      document.getElementById("pi-lib-modal").style.display = "block";
    } catch (e) {
      console.error("Failed to load mutator detail:", e);
    }
  }

  /* ===================================================================
   * Mutation Lab
   * =================================================================== */
  SECTION_LOADERS["section-mutation-lab"] = async function () {
    try {
      var mutators = await getAllMutators();
      var sel = document.getElementById("pi-lab-mutator-select");
      if (sel) {
        sel.innerHTML = "";
        /* Group options by category */
        var grouped = {};
        for (var i = 0; i < mutators.length; i++) {
          var m = mutators[i];
          if (!grouped[m.category]) grouped[m.category] = [];
          grouped[m.category].push(m);
        }
        for (var cat in grouped) {
          var grp = document.createElement("optgroup");
          grp.label = cat;
          for (var j = 0; j < grouped[cat].length; j++) {
            var opt = document.createElement("option");
            opt.value = grouped[cat][j].name;
            opt.textContent = grouped[cat][j].name;
            grp.appendChild(opt);
          }
          sel.appendChild(grp);
        }
      }
    } catch (e) {
      console.warn("Failed to load mutators for lab:", e);
    }

    document.getElementById("pi-lab-mutate-btn").onclick = applyMutation;
  };

  async function applyMutation() {
    var prompt = document.getElementById("pi-lab-prompt").value.trim();
    if (!prompt) { alert("Enter a prompt first."); return; }

    var sel = document.getElementById("pi-lab-mutator-select");
    var selected = [];
    if (sel) {
      for (var i = 0; i < sel.options.length; i++) {
        if (sel.options[i].selected) selected.push(sel.options[i].value);
      }
    }
    if (selected.length === 0) { alert("Select at least one mutator."); return; }

    var mode = document.querySelector('input[name="pi-lab-mode"]:checked');
    var modeVal = mode ? mode.value : "parallel";

    var btn = document.getElementById("pi-lab-mutate-btn");
    var status = document.getElementById("pi-lab-status");
    var results = document.getElementById("pi-lab-results");

    btn.disabled = true;
    status.innerHTML = '<div class="spinner-border spinner-border-sm"></div> Mutating...';
    results.innerHTML = "";

    try {
      var endpoint, body;
      if (selected.length === 1) {
        endpoint = "/mutate";
        body = { prompt: prompt, mutator: selected[0] };
      } else {
        endpoint = "/pipeline";
        body = { prompt: prompt, mutators: selected, mode: modeVal };
      }

      var data = await api(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });

      status.textContent = data.length + " mutation(s) returned (" + modeVal + " mode)";
      results.innerHTML = renderMutationResults(data);
    } catch (e) {
      status.innerHTML = '<span class="text-danger">Error: ' + escHtml(e.message) + "</span>";
    }
    btn.disabled = false;
  }

  function renderMutationResults(data) {
    if (!data || data.length === 0) return '<div class="text-muted">No results</div>';
    var html = "";
    for (var i = 0; i < data.length; i++) {
      var r = data[i];
      var hasDecoder = r.metadata && r.metadata.decoder;
      html += '<div class="mb-3 p-3 rounded" style="border-left:4px solid ' + (CATEGORY_COLORS[r.technique_category] || "#666") + '; background:var(--bg-secondary,#f8f9fa);">';
      html += '<div class="d-flex justify-content-between align-items-start mb-1">';
      html += '<div>' + catBadge(r.technique_category) + ' <strong class="ms-1">' + escHtml(r.mutator_name) + "</strong></div>";
      html += '<button class="btn btn-sm btn-outline-secondary pi-copy-btn" data-idx="' + i + '">Copy</button>';
      html += "</div>";
      html += '<div class="small text-muted mb-2">' + escHtml(r.description) + "</div>";
      html += '<div class="mb-1"><strong class="small">Original:</strong></div>';
      html += '<pre class="p-2 rounded small" style="background:var(--bg-primary,#fff);white-space:pre-wrap;max-height:120px;overflow-y:auto;">' + escHtml(r.original) + "</pre>";
      html += '<div class="mb-1"><strong class="small">Mutated:</strong></div>';
      html += '<pre class="p-2 rounded small" style="background:var(--bg-primary,#fff);white-space:pre-wrap;max-height:200px;overflow-y:auto;" id="pi-mut-text-' + i + '">' + escHtml(r.mutated) + "</pre>";
      if (hasDecoder) {
        html += '<button class="btn btn-sm btn-outline-info pi-decode-btn" data-idx="' + i + '">Decode</button>';
        html += '<span class="small text-muted ms-2" id="pi-decode-out-' + i + '"></span>';
      }
      if (r.metadata && Object.keys(r.metadata).length > 0) {
        html += '<details class="mt-1"><summary class="small">Metadata</summary>';
        html += '<pre class="p-2 rounded small" style="background:var(--bg-primary,#fff);max-height:120px;overflow-y:auto;">' + escHtml(JSON.stringify(r.metadata, null, 2)) + "</pre></details>";
      }
      html += "</div>";
    }
    return html;
  }

  /* Delegated click handlers for copy and decode */
  document.addEventListener("click", function (e) {
    if (e.target.classList.contains("pi-copy-btn")) {
      var idx = e.target.dataset.idx;
      var pre = document.getElementById("pi-mut-text-" + idx);
      if (pre) copyToClipboard(pre.textContent, e.target);
    }
    if (e.target.classList.contains("pi-decode-btn")) {
      decodeResult(e.target);
    }
  });

  async function decodeResult(btn) {
    var idx = btn.dataset.idx;
    var pre = document.getElementById("pi-mut-text-" + idx);
    var out = document.getElementById("pi-decode-out-" + idx);
    if (!pre || !out) return;

    btn.disabled = true;
    out.textContent = "Decoding...";

    try {
      /* We need metadata — retrieve from the closest .pi-decode-btn sibling details */
      var container = btn.closest(".mb-3");
      var metaPre = container ? container.querySelector("details pre") : null;
      var metadata = {};
      if (metaPre) {
        try { metadata = JSON.parse(metaPre.textContent); } catch (_) {}
      }

      var data = await api("/decode", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: pre.textContent,
          mutator: "",
          metadata: metadata,
        }),
      });
      out.innerHTML = '<span class="text-success">Decoded (' + escHtml(data.method) + "):</span> " + escHtml(data.decoded.substring(0, 200));
    } catch (e) {
      out.innerHTML = '<span class="text-danger">Decode error: ' + escHtml(e.message) + "</span>";
    }
    btn.disabled = false;
  }

  /* ===================================================================
   * Pipeline Builder
   * =================================================================== */
  var pipelineChain = [];

  SECTION_LOADERS["section-pipeline-builder"] = async function () {
    pipelineChain = [];
    renderPipelineChain();

    try {
      var mutators = await getAllMutators();
      var sel = document.getElementById("pi-pipe-add-select");
      if (sel) {
        sel.innerHTML = "";
        for (var i = 0; i < mutators.length; i++) {
          var opt = document.createElement("option");
          opt.value = mutators[i].name;
          opt.textContent = mutators[i].name + " (" + mutators[i].category + ")";
          sel.appendChild(opt);
        }
      }
    } catch (e) {
      console.warn("Failed to load mutators for pipeline:", e);
    }

    document.getElementById("pi-pipe-add-btn").onclick = function () {
      var sel = document.getElementById("pi-pipe-add-select");
      if (sel && sel.value) {
        pipelineChain.push(sel.value);
        renderPipelineChain();
      }
    };

    document.getElementById("pi-pipe-run-btn").onclick = runPipeline;
  };

  function renderPipelineChain() {
    var container = document.getElementById("pi-pipe-chain");
    if (!container) return;
    if (pipelineChain.length === 0) {
      container.innerHTML = '<div class="text-muted small p-2">No mutators added yet. Use the dropdown above to add steps.</div>';
      return;
    }
    var html = "";
    for (var i = 0; i < pipelineChain.length; i++) {
      html += '<div class="d-flex align-items-center gap-2 mb-1 p-2 rounded" style="background:var(--bg-secondary,#f8f9fa);">';
      html += '<span class="badge bg-secondary">' + (i + 1) + "</span>";
      html += '<span class="small flex-grow-1">' + escHtml(pipelineChain[i]) + "</span>";
      html += '<button class="btn btn-sm btn-outline-danger pi-pipe-remove" data-idx="' + i + '" title="Remove">&times;</button>';
      if (i > 0) html += '<button class="btn btn-sm btn-outline-secondary pi-pipe-up" data-idx="' + i + '" title="Move up">&uarr;</button>';
      if (i < pipelineChain.length - 1) html += '<button class="btn btn-sm btn-outline-secondary pi-pipe-down" data-idx="' + i + '" title="Move down">&darr;</button>';
      html += "</div>";
    }
    container.innerHTML = html;

    /* Remove / reorder handlers */
    container.querySelectorAll(".pi-pipe-remove").forEach(function (btn) {
      btn.onclick = function () {
        pipelineChain.splice(parseInt(btn.dataset.idx), 1);
        renderPipelineChain();
      };
    });
    container.querySelectorAll(".pi-pipe-up").forEach(function (btn) {
      btn.onclick = function () {
        var idx = parseInt(btn.dataset.idx);
        if (idx > 0) {
          var tmp = pipelineChain[idx - 1];
          pipelineChain[idx - 1] = pipelineChain[idx];
          pipelineChain[idx] = tmp;
          renderPipelineChain();
        }
      };
    });
    container.querySelectorAll(".pi-pipe-down").forEach(function (btn) {
      btn.onclick = function () {
        var idx = parseInt(btn.dataset.idx);
        if (idx < pipelineChain.length - 1) {
          var tmp = pipelineChain[idx + 1];
          pipelineChain[idx + 1] = pipelineChain[idx];
          pipelineChain[idx] = tmp;
          renderPipelineChain();
        }
      };
    });
  }

  async function runPipeline() {
    var prompt = document.getElementById("pi-pipe-prompt").value.trim();
    if (!prompt) { alert("Enter a prompt first."); return; }
    if (pipelineChain.length === 0) { alert("Add at least one mutator to the pipeline."); return; }

    var mode = document.querySelector('input[name="pi-pipe-mode"]:checked');
    var modeVal = mode ? mode.value : "parallel";

    var btn = document.getElementById("pi-pipe-run-btn");
    var status = document.getElementById("pi-pipe-status");
    var results = document.getElementById("pi-pipe-results");

    btn.disabled = true;
    status.innerHTML = '<div class="spinner-border spinner-border-sm"></div> Running pipeline (' + pipelineChain.length + " steps, " + modeVal + ")...";
    results.innerHTML = "";

    try {
      var data = await api("/pipeline", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          prompt: prompt,
          mutators: pipelineChain,
          mode: modeVal,
        }),
      });

      status.textContent = data.length + " mutation(s) from pipeline";
      results.innerHTML = renderMutationResults(data);
    } catch (e) {
      status.innerHTML = '<span class="text-danger">Error: ' + escHtml(e.message) + "</span>";
    }
    btn.disabled = false;
  }

  /* ===================================================================
   * Batch Results
   * =================================================================== */
  SECTION_LOADERS["section-batch-results"] = async function () {
    await loadBatchList();
    document.getElementById("pi-batch-refresh").onclick = loadBatchList;
    var closeBtn = document.getElementById("pi-batch-modal-close");
    if (closeBtn) closeBtn.onclick = function () {
      document.getElementById("pi-batch-modal").style.display = "none";
    };
  };

  async function loadBatchList() {
    /* Stats */
    try {
      var stats = await api("/stats");
      var statsEl = document.getElementById("pi-batch-stats");
      if (statsEl) {
        statsEl.innerHTML =
          '<div class="col-sm-3"><div class="card p-2 text-center"><div class="h4 mb-0">' + stats.total_mutators + '</div><div class="small text-muted">Total Mutators</div></div></div>' +
          '<div class="col-sm-3"><div class="card p-2 text-center"><div class="h4 mb-0">' + stats.category_count + '</div><div class="small text-muted">Categories</div></div></div>' +
          '<div class="col-sm-3"><div class="card p-2 text-center"><div class="h4 mb-0">' + stats.deterministic + '</div><div class="small text-muted">Deterministic</div></div></div>' +
          '<div class="col-sm-3"><div class="card p-2 text-center"><div class="h4 mb-0">' + stats.saved_batches + '</div><div class="small text-muted">Saved Batches</div></div></div>';
      }
    } catch (e) {
      console.warn("Failed to load batch stats:", e);
    }

    /* Batch list */
    try {
      var batches = await api("/batches");
      var list = document.getElementById("pi-batch-list");
      if (!list) return;

      if (batches.length === 0) {
        list.innerHTML = '<div class="text-center text-muted py-4">No batch results yet. Run a batch from the Mutation Lab to see results here.</div>';
        return;
      }

      var html = '<table class="table table-sm table-hover"><thead><tr>' +
        "<th>Batch ID</th><th>Created</th><th>Prompts</th><th>Mutators</th><th>Mutations</th><th>Mode</th><th>Actions</th>" +
        "</tr></thead><tbody>";
      for (var i = 0; i < batches.length; i++) {
        var b = batches[i];
        var s = b.stats || {};
        html += "<tr>";
        html += "<td><code class=\"small\">" + escHtml(b.id) + "</code></td>";
        html += "<td class=\"small\">" + escHtml(b.created_at ? new Date(b.created_at).toLocaleString() : "") + "</td>";
        html += "<td>" + (s.prompts || 0) + "</td>";
        html += "<td>" + (s.mutators || 0) + "</td>";
        html += "<td>" + (s.total_mutations || 0) + "</td>";
        html += "<td>" + escHtml(s.mode || "") + "</td>";
        html += '<td><button class="btn btn-sm btn-outline-primary pi-batch-view" data-id="' + escHtml(b.id) + '">View</button>';
        html += ' <button class="btn btn-sm btn-outline-danger pi-batch-del" data-id="' + escHtml(b.id) + '">Delete</button></td>';
        html += "</tr>";
      }
      html += "</tbody></table>";
      list.innerHTML = html;

      list.querySelectorAll(".pi-batch-view").forEach(function (btn) {
        btn.onclick = function () { showBatchDetail(btn.dataset.id); };
      });
      list.querySelectorAll(".pi-batch-del").forEach(function (btn) {
        btn.onclick = async function () {
          if (!confirm("Delete this batch?")) return;
          try {
            await api("/batches/" + encodeURIComponent(btn.dataset.id), { method: "DELETE" });
            loadBatchList();
          } catch (e) {
            alert("Delete failed: " + e.message);
          }
        };
      });
    } catch (e) {
      console.error("Failed to load batches:", e);
    }
  }

  async function showBatchDetail(batchId) {
    try {
      var data = await api("/batches/" + encodeURIComponent(batchId));
      var content = document.getElementById("pi-batch-modal-content");
      if (!content) return;

      var s = data.stats || {};
      var html = "<h4>Batch: " + escHtml(data.id) + "</h4>";
      html += '<div class="mb-2 small text-muted">Created: ' + escHtml(data.created_at || "") + "</div>";
      html += '<div class="d-flex gap-3 mb-3">';
      html += "<span><strong>" + (s.prompts || 0) + "</strong> prompts</span>";
      html += "<span><strong>" + (s.mutators || 0) + "</strong> mutators</span>";
      html += "<span><strong>" + (s.total_mutations || 0) + "</strong> total mutations</span>";
      html += "<span>Mode: <strong>" + escHtml(s.mode || "") + "</strong></span>";
      html += "</div>";

      /* Category breakdown */
      if (s.categories_hit) {
        html += '<div class="mb-3">';
        for (var cat in s.categories_hit) {
          html += catBadge(cat) + " <span class=\"small me-2\">" + s.categories_hit[cat] + "</span>";
        }
        html += "</div>";
      }

      /* Results per prompt */
      var results = data.results || [];
      for (var p = 0; p < results.length; p++) {
        var promptResults = results[p];
        if (!promptResults || promptResults.length === 0) continue;
        html += '<div class="mb-3 p-2 rounded" style="background:var(--bg-secondary,#f8f9fa);">';
        html += '<h6>Prompt ' + (p + 1) + '</h6>';
        html += '<pre class="p-2 rounded small" style="background:var(--bg-primary,#fff);white-space:pre-wrap;max-height:80px;overflow-y:auto;">' + escHtml(promptResults[0].original || "") + "</pre>";
        for (var r = 0; r < promptResults.length; r++) {
          var mr = promptResults[r];
          html += '<div class="ms-3 mb-2 p-2 rounded" style="border-left:3px solid ' + (CATEGORY_COLORS[mr.technique_category] || "#666") + ';">';
          html += '<div class="small"><strong>' + escHtml(mr.mutator_name) + "</strong> " + catBadge(mr.technique_category) + "</div>";
          html += '<pre class="p-1 rounded small mt-1" style="background:var(--bg-primary,#fff);white-space:pre-wrap;max-height:100px;overflow-y:auto;">' + escHtml(mr.mutated) + "</pre>";
          html += "</div>";
        }
        html += "</div>";
      }

      content.innerHTML = html;
      document.getElementById("pi-batch-modal").style.display = "block";
    } catch (e) {
      console.error("Failed to load batch:", e);
    }
  }

  /* Register section loaders on global object */
  window.SECTION_LOADERS = SECTION_LOADERS;
})();
