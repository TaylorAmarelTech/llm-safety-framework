/* LLM Cartography plugin — JS for all 5 sections */
(function () {
  "use strict";
  var API = "/api/cartography";

  var escHtml = function (s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  };

  /* ---------- Helpers ---------- */

  function api(path, opts) {
    return fetch(API + path, opts).then(function (r) {
      if (!r.ok) return r.text().then(function (t) { throw new Error(t); });
      return r.json();
    });
  }

  function postJson(path, body) {
    return api(path, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
  }

  function setHtml(id, html) {
    var el = document.getElementById(id);
    if (el) el.innerHTML = html;
  }

  function showEl(id, show) {
    var el = document.getElementById(id);
    if (el) el.style.display = show ? "block" : "none";
  }

  function parseJsonArea(id) {
    var el = document.getElementById(id);
    if (!el || !el.value.trim()) return null;
    try {
      return JSON.parse(el.value.trim());
    } catch (e) {
      showToast("Invalid JSON: " + e.message);
      return null;
    }
  }

  function showToast(msg) {
    if (window.showToast) window.showToast(msg);
    else console.log("[Cartography]", msg);
  }

  function badge(text, color) {
    return '<span style="display:inline-block;padding:2px 8px;border-radius:4px;' +
      'font-size:0.75rem;font-weight:600;background:' + color + ';color:#fff;">' +
      escHtml(text) + '</span>';
  }

  function severityColor(sev) {
    var map = { critical: "#dc3545", high: "#fd7e14", medium: "#ffc107", low: "#198754" };
    return map[sev] || "#6c757d";
  }

  function safetyColor(score) {
    if (score < 0.25) return "#198754";
    if (score < 0.55) return "#ffc107";
    return "#dc3545";
  }

  function renderJsonBlock(data) {
    return '<pre style="background:#f8f9fa;padding:12px;border-radius:6px;' +
      'font-size:0.8rem;max-height:500px;overflow:auto;white-space:pre-wrap;">' +
      escHtml(JSON.stringify(data, null, 2)) + '</pre>';
  }

  function renderTable(headers, rows) {
    var html = '<div style="overflow-x:auto;"><table class="table table-sm table-bordered" style="font-size:0.8rem;">';
    html += '<thead><tr>' + headers.map(function (h) { return '<th>' + escHtml(h) + '</th>'; }).join('') + '</tr></thead>';
    html += '<tbody>';
    rows.forEach(function (row) {
      html += '<tr>' + row.map(function (c) { return '<td>' + c + '</td>'; }).join('') + '</tr>';
    });
    html += '</tbody></table></div>';
    return html;
  }

  /* ========== cached dimension data ========== */
  var _dimensions = null;
  var _templates = null;

  function loadDimensions() {
    if (_dimensions) return Promise.resolve(_dimensions);
    return api("/dimensions").then(function (data) {
      _dimensions = data;
      return data;
    });
  }

  function loadTemplates() {
    if (_templates) return Promise.resolve(_templates);
    return api("/templates").then(function (data) {
      _templates = data;
      return data;
    });
  }

  function populateDimSelect(selectId, dims) {
    var el = document.getElementById(selectId);
    if (!el) return;
    el.innerHTML = dims.map(function (d) {
      return '<option value="' + escHtml(d.id) + '">' + escHtml(d.id + " — " + d.name) + '</option>';
    }).join('');
  }

  function populateTplSelect(selectId, tpls) {
    var el = document.getElementById(selectId);
    if (!el) return;
    el.innerHTML = tpls.map(function (t) {
      return '<option value="' + escHtml(t.key) + '">' + escHtml(t.key) + '</option>';
    }).join('');
  }

  /* =========================================================================
   * Section: Gradient Explorer
   * ========================================================================= */

  var SECTION_LOADERS = window.SECTION_LOADERS || {};

  SECTION_LOADERS["section-gradient-explorer"] = function () {
    Promise.all([loadDimensions(), loadTemplates()]).then(function (results) {
      var dims = results[0];
      var tpls = results[1];
      populateDimSelect("carto-dim-select", dims);
      populateDimSelect("carto-cross-a", dims);
      populateDimSelect("carto-cross-b", dims);
      populateTplSelect("carto-tpl-select", tpls);

      // Default cross-b to something different
      var crossB = document.getElementById("carto-cross-b");
      if (crossB && crossB.options.length > 1) crossB.selectedIndex = 1;
    }).catch(function (e) {
      console.warn("Failed to load cartography metadata:", e);
    });

    var genBtn = document.getElementById("carto-gen-btn");
    if (genBtn) genBtn.onclick = doGenerateGradient;

    var genAllBtn = document.getElementById("carto-gen-all-btn");
    if (genAllBtn) genAllBtn.onclick = doGenerateAll;

    var crossBtn = document.getElementById("carto-cross-btn");
    if (crossBtn) crossBtn.onclick = doCrossGradient;
  };

  function getGradientParams() {
    return {
      template: (document.getElementById("carto-tpl-select") || {}).value || "recruitment",
      baseline_level: parseInt((document.getElementById("carto-baseline") || {}).value || "3", 10),
    };
  }

  function doGenerateGradient() {
    var dim = (document.getElementById("carto-dim-select") || {}).value;
    if (!dim) return showToast("Select a dimension");
    var params = getGradientParams();
    showEl("carto-gradient-loading", true);
    setHtml("carto-gradient-result", "");
    postJson("/gradients/generate", {
      dimension: dim,
      template: params.template,
      baseline_level: params.baseline_level,
    }).then(function (data) {
      showEl("carto-gradient-loading", false);
      renderGradientResult(data);
    }).catch(function (e) {
      showEl("carto-gradient-loading", false);
      setHtml("carto-gradient-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function doGenerateAll() {
    var params = getGradientParams();
    showEl("carto-gradient-loading", true);
    setHtml("carto-gradient-result", "");
    postJson("/gradients/generate-all", {
      template: params.template,
      baseline_level: params.baseline_level,
    }).then(function (data) {
      showEl("carto-gradient-loading", false);
      var rows = data.families.map(function (f) {
        return [escHtml(f.dimension), escHtml(f.dimension_name), String(f.point_count)];
      });
      var html = '<div class="card p-3 mb-3">' +
        '<h6>' + data.total_families + ' Gradient Families (' + data.total_points + ' total points)</h6>' +
        renderTable(["Dimension", "Name", "Points"], rows) +
        '</div>';
      setHtml("carto-gradient-result", html);
    }).catch(function (e) {
      showEl("carto-gradient-loading", false);
      setHtml("carto-gradient-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function doCrossGradient() {
    var dimA = (document.getElementById("carto-cross-a") || {}).value;
    var dimB = (document.getElementById("carto-cross-b") || {}).value;
    if (!dimA || !dimB) return showToast("Select both dimensions");
    if (dimA === dimB) return showToast("Dimensions must be different");
    var params = getGradientParams();
    showEl("carto-gradient-loading", true);
    setHtml("carto-gradient-result", "");
    postJson("/gradients/cross", {
      dim_a: dimA,
      dim_b: dimB,
      template: params.template,
      baseline_level: params.baseline_level,
    }).then(function (data) {
      showEl("carto-gradient-loading", false);
      var rows = data.points.map(function (p) {
        var va = p.dimensional_vector[data.dim_a] || "?";
        var vb = p.dimensional_vector[data.dim_b] || "?";
        return [escHtml(p.id), String(va), String(vb), escHtml(p.prompt.substring(0, 120) + "...")];
      });
      var html = '<div class="card p-3 mb-3">' +
        '<h6>Cross-Gradient: ' + escHtml(data.dim_a) + ' x ' + escHtml(data.dim_b) +
        ' (' + data.total_points + ' points)</h6>' +
        renderTable(["ID", data.dim_a, data.dim_b, "Prompt Preview"], rows) +
        '</div>';
      setHtml("carto-gradient-result", html);
    }).catch(function (e) {
      showEl("carto-gradient-loading", false);
      setHtml("carto-gradient-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function renderGradientResult(data) {
    var rows = data.points.map(function (p) {
      var level = p.dimensional_vector[data.dimension] || "?";
      var desc = (p.metadata || {}).level_description || "";
      return [
        escHtml(p.id),
        String(level),
        escHtml(desc),
        escHtml(p.prompt.substring(0, 150) + "..."),
      ];
    });
    var html = '<div class="card p-3 mb-3">' +
      '<h6>Gradient: ' + escHtml(data.dimension) + ' — ' + escHtml(data.dimension_name) +
      ' (' + data.total_points + ' points)</h6>' +
      '<div class="small text-muted mb-2">Base prompt: ' + escHtml(data.base_prompt.substring(0, 200)) + '</div>' +
      renderTable(["ID", "Level", "Description", "Prompt Preview"], rows) +
      '</div>';
    setHtml("carto-gradient-result", html);
  }


  /* =========================================================================
   * Section: Topology Map
   * ========================================================================= */

  SECTION_LOADERS["section-topology-map"] = function () {
    var computeBtn = document.getElementById("topo-compute-btn");
    if (computeBtn) computeBtn.onclick = doTopoCompute;

    var gradBtn = document.getElementById("topo-gradient-btn");
    if (gradBtn) gradBtn.onclick = doTopoGradient;

    var cliffBtn = document.getElementById("topo-cliff-btn");
    if (cliffBtn) cliffBtn.onclick = doTopoCliffs;

    var blindBtn = document.getElementById("topo-blind-btn");
    if (blindBtn) blindBtn.onclick = doTopoBlind;
  };

  function getTopoPayload() {
    var pts = parseJsonArea("topo-points-json");
    if (!pts) return null;
    if (!Array.isArray(pts)) { showToast("Points must be a JSON array"); return null; }
    return {
      model_id: (document.getElementById("topo-model-id") || {}).value || "default",
      points: pts,
    };
  }

  function doTopoCompute() {
    var body = getTopoPayload();
    if (!body) return;
    showEl("topo-loading", true);
    setHtml("topo-result", "");
    postJson("/topology/compute", body).then(function (data) {
      showEl("topo-loading", false);
      var html = '<div class="card p-3 mb-3">';
      html += '<h6>Safety Surface: ' + escHtml(data.model_id) + '</h6>';
      html += '<div class="row g-3 mb-3">';
      html += metricCard("Total Points", data.total_points);
      html += metricCard("Mean Safety", data.mean_safety.toFixed(4), safetyColor(data.mean_safety));
      html += metricCard("Std Safety", data.std_safety.toFixed(4));
      html += metricCard("Coverage", (data.coverage_score * 100).toFixed(1) + "%");
      html += metricCard("Cliffs", data.cliffs.length);
      html += metricCard("Blind Spots", data.blind_spots.length);
      html += '</div>';

      // Gradients table
      if (data.gradients && Object.keys(data.gradients).length > 0) {
        var gradRows = Object.entries(data.gradients)
          .sort(function (a, b) { return Math.abs(b[1]) - Math.abs(a[1]); })
          .slice(0, 20)
          .map(function (e) {
            var color = e[1] > 0.01 ? "#dc3545" : (e[1] < -0.01 ? "#198754" : "#6c757d");
            return [escHtml(e[0]), '<span style="color:' + color + ';">' + e[1].toFixed(4) + '</span>'];
          });
        html += '<h6 class="mt-3">Top Gradients (partial derivatives)</h6>';
        html += renderTable(["Dimension", "dF/dDim"], gradRows);
      }
      html += '</div>';
      setHtml("topo-result", html);
    }).catch(function (e) {
      showEl("topo-loading", false);
      setHtml("topo-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function doTopoGradient() {
    var body = getTopoPayload();
    if (!body) return;
    showEl("topo-loading", true);
    setHtml("topo-result", "");
    postJson("/topology/gradient-vector", body).then(function (data) {
      showEl("topo-loading", false);
      var html = '<div class="card p-3 mb-3">';
      html += '<h6>Gradient Vector: ' + escHtml(data.model_id) + ' (' + data.total_dimensions + ' dims)</h6>';
      if (data.top_positive.length > 0) {
        html += '<h6 class="text-danger mt-2">Top Positive (push toward compliance)</h6>';
        var posRows = data.top_positive.map(function (d) {
          return [escHtml(d.dimension), '<span class="text-danger">' + d.derivative.toFixed(4) + '</span>'];
        });
        html += renderTable(["Dimension", "Derivative"], posRows);
      }
      if (data.top_negative.length > 0) {
        html += '<h6 class="text-success mt-2">Top Negative (push toward refusal)</h6>';
        var negRows = data.top_negative.map(function (d) {
          return [escHtml(d.dimension), '<span class="text-success">' + d.derivative.toFixed(4) + '</span>'];
        });
        html += renderTable(["Dimension", "Derivative"], negRows);
      }
      html += '</div>';
      setHtml("topo-result", html);
    }).catch(function (e) {
      showEl("topo-loading", false);
      setHtml("topo-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function doTopoCliffs() {
    var body = getTopoPayload();
    if (!body) return;
    showEl("topo-loading", true);
    setHtml("topo-result", "");
    postJson("/topology/cliffs", body).then(function (data) {
      showEl("topo-loading", false);
      if (data.total_cliffs === 0) {
        setHtml("topo-result", '<div class="alert alert-info">No cliffs detected (threshold=' + data.threshold + ').</div>');
        return;
      }
      var rows = data.cliffs.map(function (c) {
        return [
          escHtml(c.cliff_dimension),
          c.safety_delta.toFixed(4),
          c.safety_a.toFixed(4) + ' &rarr; ' + c.safety_b.toFixed(4),
          String(c.dimensional_distance),
          escHtml(c.point_a_id) + ' &rarr; ' + escHtml(c.point_b_id),
        ];
      });
      var html = '<div class="card p-3 mb-3">' +
        '<h6>' + data.total_cliffs + ' Cliffs Detected (threshold=' + data.threshold + ')</h6>' +
        renderTable(["Cliff Dimension", "Safety Delta", "Score Transition", "Dim Distance", "Points"], rows) +
        '</div>';
      setHtml("topo-result", html);
    }).catch(function (e) {
      showEl("topo-loading", false);
      setHtml("topo-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function doTopoBlind() {
    var body = getTopoPayload();
    if (!body) return;
    showEl("topo-loading", true);
    setHtml("topo-result", "");
    postJson("/topology/blind-spots", body).then(function (data) {
      showEl("topo-loading", false);
      if (data.total === 0) {
        setHtml("topo-result", '<div class="alert alert-success">No topology blind spots detected.</div>');
        return;
      }
      var rows = data.blind_spots.map(function (b) {
        return [
          escHtml(b.point_id),
          '<span style="color:' + safetyColor(b.safety_score) + ';">' + b.safety_score.toFixed(4) + '</span>',
          String(b.grade_level),
          String(b.high_scenario_dims),
          escHtml(b.prompt_preview.substring(0, 100)),
        ];
      });
      var html = '<div class="card p-3 mb-3">' +
        '<h6>' + data.total + ' Topology Blind Spots</h6>' +
        renderTable(["Point ID", "Safety Score", "Grade", "High ILO Dims", "Prompt Preview"], rows) +
        '</div>';
      setHtml("topo-result", html);
    }).catch(function (e) {
      showEl("topo-loading", false);
      setHtml("topo-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }


  /* =========================================================================
   * Section: Comparative Matrix
   * ========================================================================= */

  SECTION_LOADERS["section-comparative-matrix"] = function () {
    var scorecardsBtn = document.getElementById("compare-scorecards-btn");
    if (scorecardsBtn) scorecardsBtn.onclick = doCompareScorecards;

    var heatmapBtn = document.getElementById("compare-heatmap-btn");
    if (heatmapBtn) heatmapBtn.onclick = doCompareHeatmap;

    var rankBtn = document.getElementById("compare-rank-btn");
    if (rankBtn) rankBtn.onclick = doCompareRank;

    var pairBtn = document.getElementById("compare-pairwise-btn");
    if (pairBtn) pairBtn.onclick = doComparePairwise;
  };

  function getCompareModels() {
    var data = parseJsonArea("compare-models-json");
    if (!data || typeof data !== "object") {
      showToast("Enter a JSON object: {model_id: [points]}");
      return null;
    }
    return data;
  }

  function doCompareScorecards() {
    var models = getCompareModels();
    if (!models) return;
    showEl("compare-loading", true);
    setHtml("compare-result", "");
    postJson("/compare/scorecards", { models: models }).then(function (data) {
      showEl("compare-loading", false);
      var html = '';
      Object.entries(data.scorecards).forEach(function (entry) {
        var modelId = entry[0];
        var sc = entry[1];
        html += '<div class="card p-3 mb-3">';
        html += '<h6>' + escHtml(modelId) + '</h6>';
        html += '<div class="row g-2 mb-2">';
        html += metricCard("Overall", sc.overall_safety_score.toFixed(2) + "/10");
        html += metricCard("Tests", sc.total_tests);
        html += '</div>';
        if (sc.weakest_dimensions.length > 0) {
          html += '<div class="small mb-1"><strong>Weakest:</strong> ' + sc.weakest_dimensions.map(escHtml).join(", ") + '</div>';
        }
        if (sc.strongest_dimensions.length > 0) {
          html += '<div class="small mb-1"><strong>Strongest:</strong> ' + sc.strongest_dimensions.map(escHtml).join(", ") + '</div>';
        }
        html += '</div>';
      });
      setHtml("compare-result", html);
    }).catch(function (e) {
      showEl("compare-loading", false);
      setHtml("compare-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function doCompareHeatmap() {
    var models = getCompareModels();
    if (!models) return;
    var axis = (document.getElementById("compare-axis") || {}).value || "dimension";
    // Show axis selector
    var opts = document.getElementById("compare-heatmap-opts");
    if (opts) opts.style.display = "flex";

    showEl("compare-loading", true);
    setHtml("compare-result", "");
    postJson("/compare/heatmap", { models: models, axis: axis }).then(function (data) {
      showEl("compare-loading", false);
      var headers = ["Model"].concat(data.columns).concat(["Avg"]);
      var rows = data.models.map(function (m, i) {
        var cells = data.cells[i].map(function (val) {
          var color = val >= 7 ? "#198754" : (val >= 4 ? "#ffc107" : "#dc3545");
          return '<span style="color:' + color + ';font-weight:600;">' + val.toFixed(1) + '</span>';
        });
        cells.unshift(escHtml(m));
        cells.push('<strong>' + data.row_averages[i].toFixed(1) + '</strong>');
        return cells;
      });
      // Column averages row
      var avgRow = ["<strong>Avg</strong>"].concat(data.column_averages.map(function (v) {
        return '<strong>' + v.toFixed(1) + '</strong>';
      })).concat([""]);
      rows.push(avgRow);

      var html = '<div class="card p-3 mb-3">' +
        '<h6>Heatmap — axis: ' + escHtml(data.axis) + ' (higher = safer)</h6>' +
        renderTable(headers, rows) +
        '</div>';
      setHtml("compare-result", html);
    }).catch(function (e) {
      showEl("compare-loading", false);
      setHtml("compare-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function doCompareRank() {
    var models = getCompareModels();
    if (!models) return;
    showEl("compare-loading", true);
    setHtml("compare-result", "");
    postJson("/compare/rank", { models: models }).then(function (data) {
      showEl("compare-loading", false);
      var rows = data.ranking.map(function (r) {
        var medal = r.rank === 1 ? " &#129351;" : (r.rank === 2 ? " &#129352;" : (r.rank === 3 ? " &#129353;" : ""));
        return [
          '<strong>' + r.rank + '</strong>' + medal,
          escHtml(r.model_id),
          '<strong style="color:' + (r.safety_score >= 7 ? "#198754" : (r.safety_score >= 4 ? "#ffc107" : "#dc3545")) +
          ';">' + r.safety_score.toFixed(2) + '/10</strong>',
        ];
      });
      var html = '<div class="card p-3 mb-3">' +
        '<h6>Safety Ranking (' + data.model_count + ' models)</h6>' +
        renderTable(["Rank", "Model", "Safety Score"], rows) +
        '</div>';
      setHtml("compare-result", html);
    }).catch(function (e) {
      showEl("compare-loading", false);
      setHtml("compare-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function doComparePairwise() {
    var models = getCompareModels();
    if (!models) return;
    var modelA = (document.getElementById("compare-pair-a") || {}).value.trim();
    var modelB = (document.getElementById("compare-pair-b") || {}).value.trim();
    if (!modelA || !modelB) return showToast("Enter both model IDs");

    showEl("compare-loading", true);
    setHtml("compare-result", "");
    postJson("/compare/pairwise", {
      model_a: modelA,
      model_b: modelB,
      models: models,
    }).then(function (data) {
      showEl("compare-loading", false);
      if (data.error) {
        setHtml("compare-result", '<div class="alert alert-warning">' + escHtml(data.error) + '</div>');
        return;
      }
      var html = '<div class="card p-3 mb-3">';
      html += '<h6>Pairwise: ' + escHtml(data.model_a) + ' vs ' + escHtml(data.model_b) + '</h6>';
      html += '<div class="small mb-2">' + escHtml(data.summary) + '</div>';
      html += '<div class="row g-2 mb-3">';
      html += metricCard(data.model_a, data.overall_a.toFixed(2) + "/10");
      html += metricCard(data.model_b, data.overall_b.toFixed(2) + "/10");
      html += '</div>';
      if (data.a_stronger_on.length > 0) {
        html += '<div class="small mb-1"><strong>' + escHtml(data.model_a) + ' stronger on:</strong> ' +
          data.a_stronger_on.map(escHtml).join(", ") + '</div>';
      }
      if (data.b_stronger_on.length > 0) {
        html += '<div class="small mb-1"><strong>' + escHtml(data.model_b) + ' stronger on:</strong> ' +
          data.b_stronger_on.map(escHtml).join(", ") + '</div>';
      }
      // Delta table
      if (data.dimension_deltas) {
        var dimRows = Object.entries(data.dimension_deltas)
          .filter(function (e) { return Math.abs(e[1]) > 0.1; })
          .sort(function (a, b) { return Math.abs(b[1]) - Math.abs(a[1]); })
          .slice(0, 20)
          .map(function (e) {
            var color = e[1] > 0 ? "#198754" : "#dc3545";
            var winner = e[1] > 0 ? data.model_a : data.model_b;
            return [escHtml(e[0]), '<span style="color:' + color + ';">' + e[1].toFixed(2) + '</span>', escHtml(winner)];
          });
        if (dimRows.length > 0) {
          html += '<h6 class="mt-2">Top Dimension Deltas (A - B)</h6>';
          html += renderTable(["Dimension", "Delta", "Winner"], dimRows);
        }
      }
      html += '</div>';
      setHtml("compare-result", html);
    }).catch(function (e) {
      showEl("compare-loading", false);
      setHtml("compare-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }


  /* =========================================================================
   * Section: Attack Surface
   * ========================================================================= */

  SECTION_LOADERS["section-attack-surface"] = function () {
    var reportBtn = document.getElementById("attack-report-btn");
    if (reportBtn) reportBtn.onclick = doAttackReport;

    var dimBtn = document.getElementById("attack-dim-btn");
    if (dimBtn) dimBtn.onclick = doAttackDim;

    var techBtn = document.getElementById("attack-tech-btn");
    if (techBtn) techBtn.onclick = doAttackTech;

    var pathsBtn = document.getElementById("attack-paths-btn");
    if (pathsBtn) pathsBtn.onclick = doAttackPaths;
  };

  function getAttackPayload() {
    var pts = parseJsonArea("attack-points-json");
    if (!pts || !Array.isArray(pts)) { showToast("Enter a JSON array of scored points"); return null; }
    return { points: pts };
  }

  function doAttackReport() {
    var body = getAttackPayload();
    if (!body) return;
    showEl("attack-loading", true);
    setHtml("attack-result", "");
    postJson("/attack-surface/report", body).then(function (data) {
      showEl("attack-loading", false);
      var html = '<div class="card p-3 mb-3">';
      html += '<h6>Attack Surface Report</h6>';
      html += '<div class="row g-2 mb-3">';
      html += metricCard("Surface Score", data.attack_surface_score.toFixed(4), safetyColor(data.attack_surface_score));
      html += metricCard("Compliance Rate", (data.compliance_rate * 100).toFixed(1) + "%");
      html += metricCard("High Compliance", (data.high_compliance_rate * 100).toFixed(1) + "%");
      html += metricCard("Mean Score", data.mean_compliance_score.toFixed(4));
      html += metricCard("Total Points", data.total_points);
      html += '</div>';
      html += '<div class="small mb-2">' + escHtml(data.summary) + '</div>';

      // Grade distribution
      if (data.grade_distribution) {
        html += '<h6 class="mt-3">Grade Distribution</h6>';
        var gradeRows = Object.entries(data.grade_distribution).map(function (e) {
          return [String(e[0]), String(e[1])];
        });
        html += renderTable(["Grade Level", "Count"], gradeRows);
      }

      // Vulnerable dimensions
      if (data.most_vulnerable_dimensions && data.most_vulnerable_dimensions.length > 0) {
        html += '<h6 class="mt-3">Most Vulnerable Dimensions</h6>';
        var vulnRows = data.most_vulnerable_dimensions.map(function (d) {
          return [escHtml(d.dimension), '<span class="text-danger">' + d.vulnerability.toFixed(4) + '</span>'];
        });
        html += renderTable(["Dimension", "Vulnerability"], vulnRows);
      }

      // Attack paths
      if (data.attack_paths && data.attack_paths.length > 0) {
        html += '<h6 class="mt-3">Attack Paths (' + data.attack_paths.length + ')</h6>';
        var pathRows = data.attack_paths.map(function (p) {
          var steps = (p.steps || []).map(function (s) {
            return s.dim_id + ":" + s.from_level + "&rarr;" + s.to_level;
          }).join(", ");
          return [steps, p.starting_safety.toFixed(4), p.ending_safety.toFixed(4),
            '<strong>' + p.effectiveness.toFixed(4) + '</strong>'];
        });
        html += renderTable(["Steps", "Start", "End", "Effectiveness"], pathRows);
      }

      html += '</div>';
      setHtml("attack-result", html);
    }).catch(function (e) {
      showEl("attack-loading", false);
      setHtml("attack-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function doAttackDim() {
    var body = getAttackPayload();
    if (!body) return;
    showEl("attack-loading", true);
    setHtml("attack-result", "");
    postJson("/attack-surface/dimensions", body).then(function (data) {
      showEl("attack-loading", false);
      var rows = data.most_vulnerable.map(function (d) {
        return [escHtml(d.dimension), '<span class="text-danger fw-bold">' + d.vulnerability.toFixed(4) + '</span>'];
      });
      var html = '<div class="card p-3 mb-3">' +
        '<h6>Dimension Vulnerability (' + data.total_dimensions_measured + ' measured)</h6>' +
        renderTable(["Dimension", "Avg Compliance When High"], rows) +
        '</div>';
      setHtml("attack-result", html);
    }).catch(function (e) {
      showEl("attack-loading", false);
      setHtml("attack-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function doAttackTech() {
    var body = getAttackPayload();
    if (!body) return;
    showEl("attack-loading", true);
    setHtml("attack-result", "");
    postJson("/attack-surface/techniques", body).then(function (data) {
      showEl("attack-loading", false);
      var rows = data.most_effective.map(function (t) {
        return [
          escHtml(t.technique),
          (t.compliance_rate * 100).toFixed(1) + "%",
          t.mean_score.toFixed(4),
          String(t.count),
          t.max_score.toFixed(4),
        ];
      });
      var html = '<div class="card p-3 mb-3">' +
        '<h6>Technique Effectiveness (' + data.total_techniques + ' techniques)</h6>' +
        renderTable(["Technique", "Compliance Rate", "Mean Score", "Count", "Max Score"], rows) +
        '</div>';
      setHtml("attack-result", html);
    }).catch(function (e) {
      showEl("attack-loading", false);
      setHtml("attack-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function doAttackPaths() {
    var body = getAttackPayload();
    if (!body) return;
    showEl("attack-loading", true);
    setHtml("attack-result", "");
    postJson("/attack-surface/paths", body).then(function (data) {
      showEl("attack-loading", false);
      if (data.total_paths === 0) {
        setHtml("attack-result", '<div class="alert alert-success">No attack paths found above effectiveness threshold.</div>');
        return;
      }
      var rows = data.attack_paths.map(function (p) {
        var steps = (p.steps || []).map(function (s) {
          return s.dim_id + ": " + s.from_level + "&rarr;" + s.to_level + " (+" + s.safety_delta.toFixed(3) + ")";
        }).join("<br>");
        return [
          steps,
          p.starting_safety.toFixed(4),
          p.ending_safety.toFixed(4),
          '<strong class="text-danger">' + p.effectiveness.toFixed(4) + '</strong>',
        ];
      });
      var html = '<div class="card p-3 mb-3">' +
        '<h6>' + data.total_paths + ' Attack Paths (max effectiveness: ' + data.max_effectiveness.toFixed(4) + ')</h6>' +
        renderTable(["Steps", "Start Safety", "End Safety", "Effectiveness"], rows) +
        '</div>';
      setHtml("attack-result", html);
    }).catch(function (e) {
      showEl("attack-loading", false);
      setHtml("attack-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }


  /* =========================================================================
   * Section: Blind Spots
   * ========================================================================= */

  SECTION_LOADERS["section-blind-spots"] = function () {
    var detectBtn = document.getElementById("blind-detect-btn");
    if (detectBtn) detectBtn.onclick = doBlindDetect;

    var summaryBtn = document.getElementById("blind-summary-btn");
    if (summaryBtn) summaryBtn.onclick = doBlindSummary;

    var crossBtn = document.getElementById("blind-cross-btn");
    if (crossBtn) crossBtn.onclick = doBlindCross;

    var anomalyBtn = document.getElementById("blind-anomaly-btn");
    if (anomalyBtn) anomalyBtn.onclick = doBlindAnomaly;
  };

  function getBlindPayload() {
    var pts = parseJsonArea("blind-points-json");
    if (!pts || !Array.isArray(pts)) { showToast("Enter a JSON array of scored points"); return null; }
    return { points: pts };
  }

  function renderBlindSpotTable(spots) {
    if (spots.length === 0) return '<div class="alert alert-success">No blind spots detected.</div>';
    var rows = spots.map(function (bs) {
      var sev = bs.severity || "unknown";
      return [
        escHtml(bs.id),
        badge(sev, severityColor(sev)),
        escHtml(bs.type),
        escHtml(bs.description.substring(0, 200)),
        '<strong>' + (bs.effect_size || 0).toFixed(4) + '</strong>',
        String(bs.sample_size || 0),
        escHtml(bs.recommendation || "").substring(0, 150),
      ];
    });
    return renderTable(
      ["ID", "Severity", "Type", "Description", "Effect Size", "Samples", "Recommendation"],
      rows
    );
  }

  function doBlindDetect() {
    var body = getBlindPayload();
    if (!body) return;
    showEl("blind-loading", true);
    setHtml("blind-result", "");
    postJson("/blind-spots/detect", body).then(function (data) {
      showEl("blind-loading", false);
      var html = '<div class="card p-3 mb-3">';
      html += '<h6>' + data.total + ' Blind Spots Detected</h6>';
      if (data.by_severity) {
        html += '<div class="d-flex gap-2 mb-2 flex-wrap">';
        Object.entries(data.by_severity).forEach(function (e) {
          html += badge(e[0] + ": " + e[1], severityColor(e[0])) + " ";
        });
        html += '</div>';
      }
      html += renderBlindSpotTable(data.blind_spots);
      html += '</div>';
      setHtml("blind-result", html);
    }).catch(function (e) {
      showEl("blind-loading", false);
      setHtml("blind-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function doBlindSummary() {
    var body = getBlindPayload();
    if (!body) return;
    showEl("blind-loading", true);
    setHtml("blind-result", "");
    postJson("/blind-spots/summary", body).then(function (data) {
      showEl("blind-loading", false);
      var html = '<div class="card p-3 mb-3">';
      html += '<h6>Blind Spot Summary</h6>';
      html += '<div class="row g-2 mb-3">';
      html += metricCard("Total", data.total_blind_spots);
      html += metricCard("Critical", data.critical_count, "#dc3545");
      html += metricCard("High", data.high_count, "#fd7e14");
      html += '</div>';

      if (data.by_type) {
        html += '<h6>By Type</h6>';
        var typeRows = Object.entries(data.by_type).map(function (e) {
          return [escHtml(e[0]), String(e[1])];
        });
        html += renderTable(["Type", "Count"], typeRows);
      }

      if (data.top_blind_spots && data.top_blind_spots.length > 0) {
        html += '<h6 class="mt-3">Top Issues</h6>';
        var topRows = data.top_blind_spots.map(function (bs) {
          var sev = bs.severity || "unknown";
          return [
            escHtml(bs.id),
            badge(sev, severityColor(sev)),
            escHtml(bs.type || ""),
            escHtml(bs.description.substring(0, 200)),
            '<strong>' + (bs.effect_size || 0).toFixed(4) + '</strong>',
          ];
        });
        html += renderTable(["ID", "Severity", "Type", "Description", "Effect Size"], topRows);
      }
      html += '</div>';
      setHtml("blind-result", html);
    }).catch(function (e) {
      showEl("blind-loading", false);
      setHtml("blind-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function doBlindCross() {
    var body = getBlindPayload();
    if (!body) return;
    showEl("blind-loading", true);
    setHtml("blind-result", "");
    postJson("/blind-spots/cross-dimensional", body).then(function (data) {
      showEl("blind-loading", false);
      var html = '<div class="card p-3 mb-3">';
      html += '<h6>' + data.total + ' Cross-Dimensional Blind Spots</h6>';
      html += renderBlindSpotTable(data.cross_dimensional);
      html += '</div>';
      setHtml("blind-result", html);
    }).catch(function (e) {
      showEl("blind-loading", false);
      setHtml("blind-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }

  function doBlindAnomaly() {
    var body = getBlindPayload();
    if (!body) return;
    showEl("blind-loading", true);
    setHtml("blind-result", "");
    postJson("/blind-spots/gradient-anomalies", body).then(function (data) {
      showEl("blind-loading", false);
      var html = '<div class="card p-3 mb-3">';
      html += '<h6>' + data.total + ' Gradient Anomalies (' + data.families_detected + ' families detected)</h6>';
      html += renderBlindSpotTable(data.gradient_anomalies);
      html += '</div>';
      setHtml("blind-result", html);
    }).catch(function (e) {
      showEl("blind-loading", false);
      setHtml("blind-result", '<div class="alert alert-danger">' + escHtml(e.message) + '</div>');
    });
  }


  /* =========================================================================
   * Shared UI helpers
   * ========================================================================= */

  function metricCard(label, value, color) {
    return '<div class="col-auto">' +
      '<div class="card p-2 text-center" style="min-width:100px;">' +
      '<div class="small text-muted">' + escHtml(label) + '</div>' +
      '<div class="fw-bold"' + (color ? ' style="color:' + color + ';"' : '') + '>' +
      value + '</div>' +
      '</div></div>';
  }

})();
