/* Research Hub plugin — JS for Search, Saved Results, API Status */
(function () {
  "use strict";
  const API = "/api/research";
  const escHtml = (s) =>
    String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");

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
    return (
      '<span style="display:inline-block;padding:2px 8px;border-radius:4px;' +
      "font-size:0.75rem;font-weight:600;background:" +
      color +
      ';color:#fff;">' +
      escHtml(text) +
      "</span>"
    );
  }

  function truncate(s, max) {
    if (!s) return "";
    return s.length > max ? s.substring(0, max) + "..." : s;
  }

  function externalLink(url, text) {
    if (!url) return escHtml(text || "");
    return (
      '<a href="' +
      escHtml(url) +
      '" target="_blank" rel="noopener noreferrer">' +
      escHtml(text || url) +
      "</a>"
    );
  }

  /* ===== Section Loaders ===== */
  const SECTION_LOADERS = window.SECTION_LOADERS || {};

  /* ---------- Search ---------- */
  SECTION_LOADERS["section-research-search"] = async function () {
    // Load suggestions
    try {
      const suggestions = await api("/suggestions");
      const container = document.getElementById("research-suggestions");
      if (container) {
        container.innerHTML = suggestions
          .map(
            (s) =>
              '<button class="btn btn-sm btn-outline-secondary research-quick-btn" ' +
              'data-query="' +
              escHtml(s.query) +
              '">' +
              escHtml(s.label) +
              "</button>"
          )
          .join("");
        container.querySelectorAll(".research-quick-btn").forEach(function (btn) {
          btn.onclick = function () {
            var input = document.getElementById("research-query");
            if (input) input.value = this.dataset.query;
            searchAll();
          };
        });
      }
    } catch (e) {
      console.warn("Failed to load suggestions:", e);
    }

    // Search button
    var searchBtn = document.getElementById("research-search-btn");
    if (searchBtn) searchBtn.onclick = searchAll;

    // Enter key
    var queryInput = document.getElementById("research-query");
    if (queryInput) {
      queryInput.onkeydown = function (e) {
        if (e.key === "Enter") searchAll();
      };
    }

    // Tab switching
    document.querySelectorAll(".research-tab-btn").forEach(function (btn) {
      btn.onclick = function () {
        switchTab(this.dataset.tab);
      };
    });
  };

  function switchTab(tab) {
    document.querySelectorAll(".research-tab-btn").forEach(function (b) {
      b.classList.toggle("active", b.dataset.tab === tab);
    });
    document.querySelectorAll(".research-tab-content").forEach(function (el) {
      el.style.display = "none";
    });
    var target = document.getElementById("research-tab-" + tab);
    if (target) target.style.display = "block";
  }

  async function searchAll() {
    var queryInput = document.getElementById("research-query");
    var query = (queryInput ? queryInput.value : "").trim();
    if (!query) return;

    var apis = [];
    document.querySelectorAll(".research-api-cb:checked").forEach(function (cb) {
      apis.push(cb.value);
    });
    if (apis.length === 0) apis = ["semantic_scholar", "arxiv", "github", "huggingface", "openalex"];

    var loading = document.getElementById("research-loading");
    var panel = document.getElementById("research-results-panel");
    if (loading) loading.style.display = "block";
    if (panel) panel.style.display = "none";

    try {
      var data = await api("/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: query, apis: apis, max_results: 10 }),
      });

      if (loading) loading.style.display = "none";
      if (panel) panel.style.display = "block";

      renderResults(data);
    } catch (e) {
      if (loading) loading.style.display = "none";
      console.error("Search failed:", e);
    }
  }

  function renderResults(data) {
    var papers = data.papers || [];
    var repos = data.repos || [];
    var datasets = data.datasets || [];
    var models = data.models || [];
    var errors = data.errors || {};

    // Update counts
    setText("research-count-papers", papers.length);
    setText("research-count-repos", repos.length);
    setText("research-count-datasets", datasets.length);
    setText("research-count-models", models.length);

    // Errors
    var errDiv = document.getElementById("research-errors");
    if (errDiv) {
      var keys = Object.keys(errors);
      if (keys.length > 0) {
        errDiv.innerHTML =
          '<div class="alert alert-warning small py-1 px-2 mb-2">' +
          keys.map(function (k) { return escHtml(k) + ": " + escHtml(errors[k]); }).join("<br>") +
          "</div>";
      } else {
        errDiv.innerHTML = "";
      }
    }

    // Papers
    setHtml(
      "research-tab-papers",
      papers.length === 0
        ? '<div class="text-muted py-3">No papers found</div>'
        : papers.map(renderPaperCard).join("")
    );

    // Repos
    setHtml(
      "research-tab-repos",
      repos.length === 0
        ? '<div class="text-muted py-3">No repos found</div>'
        : repos.map(renderRepoCard).join("")
    );

    // Datasets
    setHtml(
      "research-tab-datasets",
      datasets.length === 0
        ? '<div class="text-muted py-3">No datasets found</div>'
        : datasets.map(renderDatasetCard).join("")
    );

    // Models
    setHtml(
      "research-tab-models",
      models.length === 0
        ? '<div class="text-muted py-3">No models found</div>'
        : models.map(renderModelCard).join("")
    );

    // Show first non-empty tab
    if (papers.length > 0) switchTab("papers");
    else if (repos.length > 0) switchTab("repos");
    else if (datasets.length > 0) switchTab("datasets");
    else if (models.length > 0) switchTab("models");
    else switchTab("papers");

    // Attach save handlers
    document.querySelectorAll(".research-save-btn").forEach(function (btn) {
      btn.onclick = function () {
        saveResult(this.dataset.type, this.dataset.payload);
      };
    });

    // Attach copy-citation handlers
    document.querySelectorAll(".research-cite-btn").forEach(function (btn) {
      btn.onclick = function () {
        copyCitation(this.dataset.citation);
      };
    });
  }

  function renderPaperCard(p) {
    var authors = (p.authors || []).slice(0, 3).join(", ");
    if ((p.authors || []).length > 3) authors += " et al.";
    var citation = buildCitation(p);
    var payload = escHtml(JSON.stringify(p).replace(/"/g, "&quot;"));
    return (
      '<div class="card mb-2 p-3">' +
      '<div class="d-flex justify-content-between align-items-start">' +
      "<div>" +
      '<h6 class="mb-1" style="font-size:0.9rem;">' +
      externalLink(p.url, p.title || "Untitled") +
      "</h6>" +
      '<div class="small text-muted mb-1">' +
      escHtml(authors) +
      (p.year ? " (" + p.year + ")" : "") +
      "</div>" +
      "</div>" +
      '<div class="d-flex gap-1">' +
      (p.source ? badge(p.source, "#6c757d") : "") +
      (p.citation_count ? ' <span class="small text-muted">' + p.citation_count + " cites</span>" : "") +
      "</div>" +
      "</div>" +
      '<div class="small mb-2">' +
      escHtml(truncate(p.abstract, 250)) +
      "</div>" +
      '<div class="d-flex gap-2">' +
      (p.pdf_url
        ? '<a href="' + escHtml(p.pdf_url) + '" target="_blank" class="btn btn-sm btn-outline-secondary">PDF</a>'
        : "") +
      '<button class="btn btn-sm btn-outline-primary research-save-btn" data-type="paper" data-payload="' +
      payload +
      '">Save</button>' +
      '<button class="btn btn-sm btn-outline-secondary research-cite-btn" data-citation="' +
      escHtml(citation) +
      '">Copy Citation</button>' +
      "</div>" +
      "</div>"
    );
  }

  function renderRepoCard(r) {
    var payload = escHtml(JSON.stringify(r).replace(/"/g, "&quot;"));
    return (
      '<div class="card mb-2 p-3">' +
      '<div class="d-flex justify-content-between align-items-start">' +
      "<div>" +
      '<h6 class="mb-1" style="font-size:0.9rem;">' +
      externalLink(r.url, r.full_name || r.name) +
      "</h6>" +
      '<div class="small mb-1">' +
      escHtml(truncate(r.description, 200)) +
      "</div>" +
      "</div>" +
      '<div class="text-end small text-nowrap">' +
      (r.stars ? "<strong>" + r.stars + "</strong> stars" : "") +
      (r.language ? "<br>" + escHtml(r.language) : "") +
      "</div>" +
      "</div>" +
      '<div class="d-flex gap-2 flex-wrap small mb-1">' +
      (r.topics || [])
        .slice(0, 6)
        .map(function (t) {
          return badge(t, "#0d6efd");
        })
        .join(" ") +
      "</div>" +
      '<div class="d-flex gap-2 mt-1">' +
      '<button class="btn btn-sm btn-outline-primary research-save-btn" data-type="repo" data-payload="' +
      payload +
      '">Save</button>' +
      "</div>" +
      "</div>"
    );
  }

  function renderDatasetCard(d) {
    var payload = escHtml(JSON.stringify(d).replace(/"/g, "&quot;"));
    return (
      '<div class="card mb-2 p-3">' +
      '<h6 class="mb-1" style="font-size:0.9rem;">' +
      externalLink(d.url, d.id) +
      "</h6>" +
      '<div class="small mb-1">' +
      escHtml(truncate(d.description, 200)) +
      "</div>" +
      '<div class="d-flex justify-content-between align-items-center">' +
      '<div class="d-flex gap-1 flex-wrap small">' +
      (d.tags || [])
        .slice(0, 5)
        .map(function (t) {
          return badge(t, "#198754");
        })
        .join(" ") +
      "</div>" +
      '<span class="small text-muted">' +
      (d.downloads ? d.downloads.toLocaleString() + " downloads" : "") +
      "</span>" +
      "</div>" +
      '<div class="mt-1">' +
      '<button class="btn btn-sm btn-outline-primary research-save-btn" data-type="dataset" data-payload="' +
      payload +
      '">Save</button>' +
      "</div>" +
      "</div>"
    );
  }

  function renderModelCard(m) {
    var payload = escHtml(JSON.stringify(m).replace(/"/g, "&quot;"));
    return (
      '<div class="card mb-2 p-3">' +
      '<h6 class="mb-1" style="font-size:0.9rem;">' +
      externalLink(m.url, m.id) +
      "</h6>" +
      '<div class="d-flex justify-content-between align-items-center mb-1">' +
      "<div>" +
      (m.pipeline_tag ? badge(m.pipeline_tag, "#6f42c1") + " " : "") +
      "</div>" +
      '<span class="small text-muted">' +
      (m.downloads ? m.downloads.toLocaleString() + " downloads" : "") +
      "</span>" +
      "</div>" +
      '<div class="d-flex gap-1 flex-wrap small mb-1">' +
      (m.tags || [])
        .slice(0, 5)
        .map(function (t) {
          return badge(t, "#0dcaf0");
        })
        .join(" ") +
      "</div>" +
      '<div class="mt-1">' +
      '<button class="btn btn-sm btn-outline-primary research-save-btn" data-type="model" data-payload="' +
      payload +
      '">Save</button>' +
      "</div>" +
      "</div>"
    );
  }

  function buildCitation(p) {
    var authors = (p.authors || []).join(", ");
    var year = p.year ? " (" + p.year + ")" : "";
    var title = p.title || "Untitled";
    return authors + year + ". " + title + ". " + (p.url || "");
  }

  function copyCitation(text) {
    if (!text) return;
    // Decode HTML entities for clipboard
    var tmp = document.createElement("textarea");
    tmp.innerHTML = text;
    var decoded = tmp.value;
    if (navigator.clipboard) {
      navigator.clipboard.writeText(decoded).then(function () {
        showToast("Citation copied to clipboard");
      });
    }
  }

  async function saveResult(type, payloadStr) {
    try {
      // Decode from escaped HTML attribute
      var tmp = document.createElement("textarea");
      tmp.innerHTML = payloadStr;
      var data = JSON.parse(tmp.value);
      await api("/saved", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ type: type, data: data, notes: "" }),
      });
      showToast("Saved " + type + " for later");
    } catch (e) {
      console.error("Failed to save:", e);
      showToast("Failed to save: " + e.message);
    }
  }

  /* ---------- Saved Results ---------- */
  SECTION_LOADERS["section-research-saved"] = async function () {
    await loadSaved();
    var refreshBtn = document.getElementById("research-refresh-saved");
    if (refreshBtn) refreshBtn.onclick = loadSaved;
    var exportBtn = document.getElementById("research-export-saved");
    if (exportBtn) exportBtn.onclick = exportSaved;
  };

  async function loadSaved() {
    try {
      var items = await api("/saved");
      var groups = { paper: [], repo: [], dataset: [], model: [] };
      items.forEach(function (item) {
        if (groups[item.type]) groups[item.type].push(item);
      });

      renderSavedGroup("saved-list-papers", groups.paper, "paper");
      renderSavedGroup("saved-list-repos", groups.repo, "repo");
      renderSavedGroup("saved-list-datasets", groups.dataset, "dataset");
      renderSavedGroup("saved-list-models", groups.model, "model");
    } catch (e) {
      console.error("Failed to load saved:", e);
    }
  }

  function renderSavedGroup(containerId, items, type) {
    var el = document.getElementById(containerId);
    if (!el) return;

    if (items.length === 0) {
      el.innerHTML = '<div class="text-muted small py-2">No saved ' + escHtml(type) + "s</div>";
      return;
    }

    el.innerHTML = items
      .map(function (item) {
        var d = item.data || {};
        var title = d.title || d.full_name || d.name || d.id || "Unknown";
        var desc = d.abstract || d.description || "";
        return (
          '<div class="card mb-2 p-2">' +
          '<div class="d-flex justify-content-between align-items-start">' +
          "<div>" +
          '<strong class="small">' +
          (d.url ? externalLink(d.url, title) : escHtml(title)) +
          "</strong>" +
          '<div class="small text-muted">' +
          escHtml(truncate(desc, 120)) +
          "</div>" +
          (item.notes
            ? '<div class="small mt-1"><em>Notes: ' + escHtml(item.notes) + "</em></div>"
            : "") +
          "</div>" +
          '<div class="d-flex gap-1">' +
          '<button class="btn btn-sm btn-outline-danger research-delete-btn" data-id="' +
          escHtml(item.id) +
          '">Delete</button>' +
          "</div>" +
          "</div>" +
          '<div class="small text-muted">Saved ' +
          escHtml(item.saved_at ? new Date(item.saved_at).toLocaleDateString() : "") +
          "</div>" +
          "</div>"
        );
      })
      .join("");

    // Attach delete handlers
    el.querySelectorAll(".research-delete-btn").forEach(function (btn) {
      btn.onclick = function () {
        removeSaved(this.dataset.id);
      };
    });
  }

  async function removeSaved(id) {
    try {
      await api("/saved/" + encodeURIComponent(id), { method: "DELETE" });
      await loadSaved();
      showToast("Removed saved item");
    } catch (e) {
      console.error("Failed to delete:", e);
    }
  }

  async function exportSaved() {
    try {
      var items = await api("/saved");
      var blob = new Blob([JSON.stringify(items, null, 2)], {
        type: "application/json",
      });
      var url = URL.createObjectURL(blob);
      var a = document.createElement("a");
      a.href = url;
      a.download = "research_saved_results.json";
      a.click();
      URL.revokeObjectURL(url);
    } catch (e) {
      console.error("Export failed:", e);
    }
  }

  /* ---------- API Status ---------- */
  SECTION_LOADERS["section-research-status"] = async function () {
    var btn = document.getElementById("research-check-status");
    if (btn) btn.onclick = checkStatus;
  };

  async function checkStatus() {
    var loading = document.getElementById("research-status-loading");
    var cards = document.getElementById("research-status-cards");
    var summary = document.getElementById("research-status-summary");
    var btn = document.getElementById("research-check-status");

    if (btn) btn.disabled = true;
    if (loading) loading.style.display = "block";
    if (cards) cards.innerHTML = "";
    if (summary) summary.innerHTML = "";

    try {
      var data = await api("/status");
      if (loading) loading.style.display = "none";
      if (btn) btn.disabled = false;

      var adapters = data.adapters || [];
      if (cards) {
        cards.innerHTML = adapters
          .map(function (a) {
            var color = a.available ? "#198754" : "#dc3545";
            var statusText = a.available ? "Available" : "Unavailable";
            var icon = a.available ? "&#10003;" : "&#10007;";
            return (
              '<div class="col-md-4 col-lg-3">' +
              '<div class="card p-3 h-100">' +
              '<div class="d-flex justify-content-between align-items-center mb-2">' +
              "<h6 class=\"mb-0\" style=\"font-size:0.85rem;\">" +
              escHtml(a.name) +
              "</h6>" +
              '<span style="color:' +
              color +
              ';font-size:1.2rem;">' +
              icon +
              "</span>" +
              "</div>" +
              '<div class="small">' +
              '<div>Status: <strong style="color:' +
              color +
              ';">' +
              statusText +
              "</strong></div>" +
              "<div>Latency: " +
              (a.latency_ms || 0) +
              "ms</div>" +
              (a.sample_count !== undefined
                ? "<div>Probe results: " + a.sample_count + "</div>"
                : "") +
              (a.error
                ? '<div class="text-danger mt-1" style="font-size:0.75rem;">Error: ' +
                  escHtml(truncate(a.error, 100)) +
                  "</div>"
                : "") +
              "</div>" +
              "</div>" +
              "</div>"
            );
          })
          .join("");
      }

      if (summary) {
        summary.innerHTML =
          data.available +
          " of " +
          data.total +
          " APIs available. Checked at " +
          new Date().toLocaleTimeString();
      }
    } catch (e) {
      if (loading) loading.style.display = "none";
      if (btn) btn.disabled = false;
      if (cards) {
        cards.innerHTML =
          '<div class="col-12"><div class="alert alert-danger">Status check failed: ' +
          escHtml(e.message) +
          "</div></div>";
      }
    }
  }

  /* ===== Utilities ===== */
  function setText(id, val) {
    var el = document.getElementById(id);
    if (el) el.textContent = String(val);
  }

  function setHtml(id, html) {
    var el = document.getElementById(id);
    if (el) el.innerHTML = html;
  }

  function showToast(msg) {
    // Use shell toast if available, otherwise console
    if (window.showToast) {
      window.showToast(msg);
    } else {
      console.log("[Research]", msg);
    }
  }
})();
