// =============================================================================
// Analytics Plugin — Dashboard, Testing, Analytics, Conversations, Comparison
// =============================================================================

// --- Global state ---
// dashboardCharts, _coverageData, _coverageTab are declared in shell.html (var)
// so we assign here rather than re-declaring with let.
dashboardCharts = {};
let analyticsCharts = {};
let _convCache = [];
_coverageData = null;
_coverageTab = 'ilo';
let _ddResults = [];
let _ddIndex = 0;
let _ddIndicators = null;
let _rvRunId = null;
let _rvRunData = null;
let _rvSummary = null;

// --- Section loader registrations ---
SECTION_LOADERS['dashboard'] = loadDashboard;
SECTION_LOADERS['testing'] = loadTestingPage;
SECTION_LOADERS['analytics'] = loadAnalytics;
SECTION_LOADERS['conversations'] = loadConversations;
SECTION_LOADERS['model-comparison'] = loadComparisonPage;


// =============================================================================
// Dashboard
// =============================================================================

async function loadDashboard() {
    try {
        const [dashData, statsData] = await Promise.all([
            apiCall('/analytics/dashboard', { silent: true }),
            apiCall('/analytics/stats', { silent: true }),
        ]);
        const d = dashData;
        const s = statsData.stats;
        const o = d.overall_stats;
        const r = d.system_readiness;

        // Readiness checklist
        const checks = [
            { label: 'API endpoints configured', done: r.has_endpoints, action: 'endpoints', count: r.endpoint_count },
            { label: 'Models enabled', done: r.has_endpoints, action: 'endpoints', count: s.models.enabled },
            { label: 'Test prompts loaded', done: r.has_prompts, action: 'prompt-sets', count: s.prompts.total },
            { label: 'Pipeline built', done: r.has_pipeline, action: 'transform', count: r.pipeline_count },
            { label: 'Tests executed', done: r.has_runs, action: 'testing', count: r.run_count },
        ];
        let rHtml = '';
        for (const c of checks) {
            const icon = c.done ? '&#10003;' : '&#8212;';
            const cls = c.done ? 'done' : 'pending';
            const countStr = c.done ? ` (${c.count})` : '';
            rHtml += `<li class="readiness-item">
                <span class="readiness-check ${cls}">${icon}</span>
                <span>${c.done ? c.label + countStr : `<a onclick="showSection('${c.action}')">${c.label}</a>`}</span>
            </li>`;
        }
        document.getElementById('dashboard-readiness').innerHTML = rHtml;

        // 6 stat cards
        const modelsCount = Object.keys(d.per_model_rates).length;
        document.getElementById('dashboard-stats').innerHTML = `
            <div class="stat-card stat-card-total"><div class="value">${o.total_runs}</div><div class="label">Test Runs</div></div>
            <div class="stat-card stat-card-secondary"><div class="value">${o.total_results}</div><div class="label">Total Results</div></div>
            <div class="stat-card stat-card-safe"><div class="value">${o.safe_rate}%</div><div class="label">Safety Rate</div></div>
            <div class="stat-card stat-card-harmful"><div class="value">${o.harmful_rate}%</div><div class="label">Harmful Rate</div></div>
            <div class="stat-card stat-card-models"><div class="value">${modelsCount || s.models.enabled}</div><div class="label">Models Tested</div></div>
            <div class="stat-card stat-card-total"><div class="value">${r.pipeline_count}</div><div class="label">Pipeline Prompts</div></div>
        `;

        // Safety doughnut (cross-run aggregated)
        if (dashboardCharts.safety) dashboardCharts.safety.destroy();
        const safeCtx = document.getElementById('chart-safety').getContext('2d');
        dashboardCharts.safety = new Chart(safeCtx, {
            type: 'doughnut',
            data: {
                labels: ['Safe', 'Harmful', 'Unclear', 'Error'],
                datasets: [{
                    data: [o.safe_count, o.harmful_count, o.unclear_count, o.error_count],
                    backgroundColor: ['#10b981', '#ef4444', '#f59e0b', '#6b7280'],
                }],
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'bottom' } } },
        });

        // Categories bar chart - stacked safe vs harmful rates
        if (dashboardCharts.categories) dashboardCharts.categories.destroy();
        const catCtx = document.getElementById('chart-categories').getContext('2d');
        const catRates = d.per_category_rates;
        const catLabels = Object.keys(catRates).map(c => c.replace(/_/g, ' '));
        const catSafe = Object.values(catRates).map(v => v.safe_rate);
        const catHarmful = Object.values(catRates).map(v => v.harmful_rate);
        if (catLabels.length > 0) {
            dashboardCharts.categories = new Chart(catCtx, {
                type: 'bar',
                data: {
                    labels: catLabels,
                    datasets: [
                        { label: 'Safe %', data: catSafe, backgroundColor: '#10b981' },
                        { label: 'Harmful %', data: catHarmful, backgroundColor: '#ef4444' },
                    ],
                },
                options: { responsive: true, maintainAspectRatio: false, scales: { x: { stacked: true }, y: { stacked: true, max: 100 } }, plugins: { legend: { position: 'bottom' } } },
            });
        } else {
            // Fallback to prompt counts if no run data yet
            const cats = s.prompts.by_category;
            dashboardCharts.categories = new Chart(catCtx, {
                type: 'bar',
                data: {
                    labels: Object.keys(cats).map(c => c.replace(/_/g, ' ')),
                    datasets: [{ label: 'Prompts', data: Object.values(cats), backgroundColor: '#2563eb' }],
                },
                options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } } },
            });
        }

        // Recent runs table
        const rrEl = document.getElementById('dashboard-recent-runs');
        if (d.recent_runs.length === 0) {
            rrEl.innerHTML = '<div style="color:var(--gray-400);font-size:12px;padding:8px">No test runs yet. <a onclick="showSection(\'testing\')">Run your first test</a></div>';
        } else {
            let rrHtml = '<table class="recent-runs-table"><thead><tr><th>Date</th><th>Status</th><th>Results</th><th>Safe</th><th>Harmful</th><th>Models</th></tr></thead><tbody>';
            for (const run of d.recent_runs) {
                const date = run.started_at ? new Date(run.started_at).toLocaleString() : '-';
                const statusCls = run.status === 'completed' ? 'tag-safe' : (run.status === 'failed' ? 'tag-harmful' : 'tag-pending');
                rrHtml += `<tr onclick="if(typeof openRunViewer==='function')openRunViewer('${run.id}')">
                    <td>${date}</td>
                    <td><span class="${statusCls}" style="padding:2px 8px;border-radius:4px;font-size:11px">${run.status}</span></td>
                    <td>${run.result_count}</td>
                    <td style="color:var(--success)">${run.safe_count}</td>
                    <td style="color:var(--danger)">${run.harmful_count}</td>
                    <td>${(run.models || []).join(', ')}</td>
                </tr>`;
            }
            rrHtml += '</tbody></table>';
            rrEl.innerHTML = rrHtml;
        }

        // Load heatmap
        loadHeatmap();

    } catch (e) {
        document.getElementById('dashboard-stats').innerHTML = '<div class="stat-card"><div class="label">Could not load stats</div></div>';
    }
}

function heatmapColor(rate) {
    if (rate <= 30) return '#dc2626';
    if (rate <= 50) return '#f59e0b';
    if (rate <= 70) return '#d97706';
    if (rate <= 85) return '#65a30d';
    return '#16a34a';
}

async function loadHeatmap() {
    const minResults = parseInt(document.getElementById('heatmap-min-results')?.value) || 1;
    const container = document.getElementById('heatmap-container');
    if (!container) return;
    try {
        const data = await apiCall(`/analytics/heatmap?min_results=${minResults}`, { silent: true });
        if (!data.categories.length || !data.models.length) {
            container.innerHTML = '<div style="color:var(--gray-400);font-size:12px;text-align:center;padding:16px">No test run data for heatmap yet. Run tests to populate.</div>';
            return;
        }
        let html = '<table class="heatmap-table"><thead><tr><th class="row-header">Category / Model</th>';
        for (const m of data.models) html += `<th>${escHtml(m)}</th>`;
        html += '<th class="heatmap-total-col">Total</th></tr></thead><tbody>';

        for (const cat of data.categories) {
            html += `<tr><th class="row-header">${escHtml(cat.replace(/_/g, ' '))}</th>`;
            for (const m of data.models) {
                const cell = (data.matrix[cat] || {})[m];
                if (cell && cell.total > 0) {
                    const rate = cell.safety_rate;
                    const bg = heatmapColor(rate);
                    const tc = (rate > 30 && rate < 70) ? '#000' : '#fff';
                    html += `<td style="background:${bg};color:${tc}">${rate.toFixed(0)}%<div class="heatmap-cell-tip">Safe: ${cell.safe_count} | Harmful: ${cell.harmful_count} | Total: ${cell.total}</div></td>`;
                } else {
                    html += `<td style="background:var(--gray-50);color:var(--gray-300)">-</td>`;
                }
            }
            const catT = data.totals_by_category[cat];
            html += `<td class="heatmap-total-col">${catT ? catT.safety_rate.toFixed(0) + '% (' + catT.total + ')' : '-'}</td></tr>`;
        }

        // Totals row
        html += '<tr class="heatmap-total-row"><th class="row-header">Total</th>';
        for (const m of data.models) {
            const mT = data.totals_by_model[m];
            html += `<td>${mT ? mT.safety_rate.toFixed(0) + '% (' + mT.total + ')' : '-'}</td>`;
        }
        html += '<td></td></tr></tbody></table>';
        container.innerHTML = html;
    } catch (e) {
        container.innerHTML = '<div style="color:var(--gray-400);font-size:12px;text-align:center;padding:16px">Unable to load heatmap</div>';
    }
}

async function exportDashboardReport() {
    try {
        const [dashData, heatData] = await Promise.all([
            apiCall('/analytics/dashboard', { silent: true }),
            apiCall('/analytics/heatmap', { silent: true }),
        ]);
        const o = dashData.overall_stats;
        const cats = Object.keys(dashData.per_category_rates);
        const models = Object.keys(dashData.per_model_rates);

        // Build heatmap HTML
        let hmHtml = '';
        if (heatData.categories.length && heatData.models.length) {
            hmHtml = '<h2>Attack Effectiveness Heatmap</h2><table style="width:100%;border-collapse:collapse;font-size:12px;margin-bottom:24px">';
            hmHtml += '<tr><th style="padding:6px;border:1px solid #e5e7eb;background:#f9fafb;text-align:left">Category</th>';
            for (const m of heatData.models) hmHtml += `<th style="padding:6px;border:1px solid #e5e7eb;background:#f9fafb;text-align:center">${m}</th>`;
            hmHtml += '</tr>';
            for (const cat of heatData.categories) {
                hmHtml += `<tr><td style="padding:6px;border:1px solid #e5e7eb;font-weight:600;text-transform:capitalize">${cat.replace(/_/g, ' ')}</td>`;
                for (const m of heatData.models) {
                    const cell = (heatData.matrix[cat] || {})[m];
                    if (cell && cell.total > 0) {
                        const bg = cell.safety_rate > 70 ? '#10b981' : cell.safety_rate > 30 ? '#f59e0b' : '#ef4444';
                        hmHtml += `<td style="padding:6px;border:1px solid #e5e7eb;text-align:center;background:${bg};color:#fff;font-weight:600">${cell.safety_rate.toFixed(0)}%</td>`;
                    } else {
                        hmHtml += '<td style="padding:6px;border:1px solid #e5e7eb;text-align:center;color:#d1d5db">-</td>';
                    }
                }
                hmHtml += '</tr>';
            }
            hmHtml += '</table>';
        }

        // Build model rates table
        let modelHtml = '';
        if (models.length) {
            modelHtml = '<h2>Per-Model Safety Rates</h2><table style="width:100%;border-collapse:collapse;font-size:12px;margin-bottom:24px">';
            modelHtml += '<tr><th style="padding:6px;border:1px solid #e5e7eb;background:#f9fafb;text-align:left">Model</th><th style="padding:6px;border:1px solid #e5e7eb;background:#f9fafb">Safety Rate</th><th style="padding:6px;border:1px solid #e5e7eb;background:#f9fafb">Harmful Rate</th><th style="padding:6px;border:1px solid #e5e7eb;background:#f9fafb">Total</th></tr>';
            for (const m of models) {
                const mr = dashData.per_model_rates[m];
                modelHtml += `<tr><td style="padding:6px;border:1px solid #e5e7eb">${m}</td><td style="padding:6px;border:1px solid #e5e7eb;text-align:center;color:#10b981;font-weight:600">${mr.safe_rate}%</td><td style="padding:6px;border:1px solid #e5e7eb;text-align:center;color:#ef4444;font-weight:600">${mr.harmful_rate}%</td><td style="padding:6px;border:1px solid #e5e7eb;text-align:center">${mr.total}</td></tr>`;
            }
            modelHtml += '</table>';
        }

        const html = `<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Dashboard Report</title>
<style>body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#1f2937;background:#f9fafb;padding:32px;max-width:900px;margin:0 auto}
h1{font-size:22px;margin-bottom:4px}h2{font-size:16px;margin:24px 0 12px;color:#374151}.meta{color:#6b7280;font-size:13px;margin-bottom:24px}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:24px}.stat{background:#fff;border:1px solid #e5e7eb;border-radius:8px;padding:14px;text-align:center}
.stat .val{font-size:24px;font-weight:700}.stat .lbl{font-size:11px;color:#6b7280;margin-top:2px}
.footer{margin-top:32px;text-align:center;color:#9ca3af;font-size:11px}</style></head><body>
<h1>LLM Safety Testing - Dashboard Report</h1>
<div class="meta">Generated ${new Date().toLocaleString()} &middot; ${o.total_runs} runs &middot; ${o.total_results} results</div>
<div class="stats">
<div class="stat"><div class="val" style="color:#2563eb">${o.total_runs}</div><div class="lbl">Test Runs</div></div>
<div class="stat"><div class="val">${o.total_results}</div><div class="lbl">Total Results</div></div>
<div class="stat"><div class="val" style="color:#10b981">${o.safe_rate}%</div><div class="lbl">Safety Rate</div></div>
<div class="stat"><div class="val" style="color:#ef4444">${o.harmful_rate}%</div><div class="lbl">Harmful Rate</div></div>
</div>${hmHtml}${modelHtml}
<div class="footer">LLM Safety Testing Framework</div></body></html>`;

        const blob = new Blob([html], { type: 'text/html' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url; a.download = 'dashboard_report.html'; a.click();
        URL.revokeObjectURL(url);
    } catch (e) {
        toast('Could not generate report', 'error');
    }
}


// =============================================================================
// Testing
// =============================================================================

async function _loadTestingModels() {
    try {
        const data = await apiCall('/endpoints/all/enabled', { silent: true });
        const models = data.models || [];
        const sel = document.getElementById('test-model-select');
        if (!sel) return;
        sel.innerHTML = models.length
            ? models.map(m => `<option value="${m.id}">${escHtml(m.name)} (${m.endpoint_name})</option>`).join('')
            : '<option value="">No enabled models</option>';
    } catch (e) {}
}

async function loadTestingPage() {
    _loadTestingModels();
    try {
        const status = await apiCall('/spinning/pipeline', { silent: true });
        const info = document.getElementById('test-pipeline-info');
        if (status.pipeline) {
            const p = status.pipeline;
            info.innerHTML = `<div class="pipeline-readiness ready">Pipeline ready: <strong>${p.total}</strong> prompts from ${(p.sources || []).length} sources</div>`;
        } else {
            info.innerHTML = `<div class="pipeline-readiness not-ready">No active pipeline. <a onclick="showSection('transform')" style="cursor:pointer;text-decoration:underline">Build one in the Transform Workbench</a>.</div>`;
        }
        // Show enabled model tags
        const modelsEl = document.getElementById('test-enabled-models');
        try {
            const mData = await apiCall('/endpoints/all/enabled', { silent: true });
            const models = mData.models || [];
            if (models.length) {
                modelsEl.innerHTML = '<div style="font-size:11px;font-weight:600;color:var(--gray-500);margin-bottom:4px">ENABLED MODELS</div>' +
                    models.map(m => `<span class="model-tag">${escHtml(m.name)}</span>`).join('');
            } else {
                modelsEl.innerHTML = '<div style="font-size:12px;color:var(--warning)">No models enabled. <a onclick="showSection(\'endpoints\')" style="cursor:pointer;text-decoration:underline">Configure endpoints</a>.</div>';
            }
        } catch(e) {}
    } catch (e) {}
    loadTestRuns();
}

async function runBatchTests() {
    const maxPrompts = parseInt(document.getElementById('batch-max-prompts').value) || 50;
    toast('Starting pipeline test run...');
    const progEl = document.getElementById('batch-progress');
    progEl.style.display = 'block';
    document.getElementById('batch-progress-fill').style.width = '10%';
    document.getElementById('batch-progress-label').textContent = 'Starting...';
    try {
        const data = await apiCall('/analytics/tests/run', {
            method: 'POST',
            body: JSON.stringify({ use_pipeline: true, max_prompts: maxPrompts }),
        });
        if (data.status === 'error') {
            progEl.style.display = 'none';
            document.getElementById('batch-result').innerHTML = `<div style="color:var(--warning)">${escHtml(data.message)}</div>`;
            return;
        }
        document.getElementById('batch-progress-fill').style.width = '100%';
        document.getElementById('batch-progress-label').textContent = 'Complete';
        document.getElementById('batch-result').innerHTML = `
            <div style="background:var(--success-light);border:1px solid var(--success);border-radius:8px;padding:12px 16px;font-size:13px">
                <strong>Run:</strong> ${escHtml((data.run_id || '').substring(0, 16))}<br>
                <strong>Prompts:</strong> ${data.prompt_count} &middot;
                <strong>Models:</strong> ${(data.models || []).map(m => `<span class="model-tag">${m}</span>`).join(' ')}
            </div>`;
        toast('Test run started!');
        setTimeout(() => { progEl.style.display = 'none'; }, 3000);
        loadTestRuns();
    } catch (e) {
        progEl.style.display = 'none';
        document.getElementById('batch-result').innerHTML = `<div style="color:var(--warning)">${escHtml(e.message)}</div>`;
    }
}

async function loadTestRuns() {
    try {
        const data = await apiCall('/analytics/tests/runs', { silent: true });
        const el = document.getElementById('test-runs-list');
        if (!data.runs || data.runs.length === 0) {
            el.innerHTML = '<div style="color:var(--gray-400);padding:16px;text-align:center">No test runs yet. Run a batch test to see results here.</div>';
            return;
        }
        let html = '<table><thead><tr><th>Run ID</th><th>Started</th><th>Status</th><th>Prompts</th><th>Results</th><th>Safe/Harmful</th><th>Models</th><th>Actions</th></tr></thead><tbody>';
        for (const r of data.runs) {
            const statusCls = r.status === 'completed' ? 'tag-safe' : r.status === 'started' ? 'tag-blue' : 'tag-pending';
            // Build sparkline bar
            const safe = r.safe_count || 0;
            const harmful = r.harmful_count || 0;
            const total = r.result_count || 1;
            const safePct = Math.round(safe / total * 100) || 0;
            const harmPct = Math.round(harmful / total * 100) || 0;
            const sparkline = `<div class="result-sparkline" title="${safe} safe, ${harmful} harmful">` +
                (safe > 0 ? `<div class="spark-safe" style="height:${Math.max(4, safePct * 0.2)}px;width:${Math.max(6, safePct / 3)}px"></div>` : '') +
                (harmful > 0 ? `<div class="spark-harmful" style="height:${Math.max(4, harmPct * 0.2)}px;width:${Math.max(6, harmPct / 3)}px"></div>` : '') +
                `</div> <span style="font-size:11px;color:var(--gray-500)">${safe}/${harmful}</span>`;
            html += `<tr>
                <td style="font-family:monospace;font-size:11px">${escHtml((r.id || '').substring(0, 16))}</td>
                <td style="font-size:12px">${r.started_at ? new Date(r.started_at).toLocaleString() : ''}</td>
                <td><span class="tag ${statusCls}">${r.status}</span></td>
                <td>${r.prompt_count}</td>
                <td>${r.result_count}</td>
                <td>${sparkline}</td>
                <td style="font-size:11px">${(r.models || []).join(', ')}</td>
                <td><button class="btn btn-sm btn-primary" onclick="openRunViewer('${escHtml(r.id)}')">View</button></td>
            </tr>`;
        }
        html += '</tbody></table>';
        el.innerHTML = html;
    } catch (e) {
        document.getElementById('test-runs-list').innerHTML = '<div style="color:var(--gray-400)">Unable to load test runs</div>';
    }
}

async function executeTest() {
    const modelId = document.getElementById('test-model-select').value;
    const prompt = document.getElementById('test-prompt').value;
    if (!modelId) return toast('Select a model', 'error');
    if (!prompt) return toast('Enter a prompt', 'error');
    toast('Executing test...');
    // Show user bubble immediately
    document.getElementById('test-result').innerHTML = `
        <div class="chat-bubble user-bubble">
            <div class="bubble-meta">You</div>
            ${escHtml(prompt)}
        </div>
        <div class="chat-bubble assistant-bubble" style="opacity:0.5">
            <div class="bubble-meta">Assistant</div>
            <div class="loading" style="padding:4px 0;text-align:left">Thinking...</div>
        </div>
    `;
    try {
        const data = await apiCall('/analytics/tests/execute', {
            method: 'POST',
            body: JSON.stringify({ prompt, model_id: modelId }),
        });
        const cls = data.classification === 'SAFE' ? 'tag-safe' : data.classification === 'HARMFUL' ? 'tag-harmful' : 'tag-pending';
        const confPct = data.confidence != null ? (data.confidence * 100).toFixed(0) + '%' : 'N/A';
        document.getElementById('test-result').innerHTML = `
            <div class="chat-bubble user-bubble">
                <div class="bubble-meta">You</div>
                ${escHtml(prompt)}
            </div>
            <div class="chat-bubble assistant-bubble">
                <div class="bubble-meta">Assistant &middot; ${escHtml(data.model || modelId)}</div>
                <div style="white-space:pre-wrap;margin-bottom:8px">${escHtml(data.response || '')}</div>
                <div style="display:flex;align-items:center;gap:8px;margin-top:6px;padding-top:8px;border-top:1px solid var(--gray-200)">
                    <span class="tag ${cls}">${data.classification}</span>
                    <span style="font-size:11px;color:var(--gray-500)">Confidence: ${confPct}</span>
                </div>
            </div>
        `;
    } catch (e) {
        document.getElementById('test-result').innerHTML = `
            <div class="chat-bubble user-bubble">
                <div class="bubble-meta">You</div>
                ${escHtml(prompt)}
            </div>
            <div class="chat-bubble assistant-bubble" style="border:1px solid var(--danger)">
                <div class="bubble-meta" style="color:var(--danger)">Error</div>
                ${escHtml(e.message)}
            </div>
        `;
    }
}


// =============================================================================
// Analytics
// =============================================================================

async function loadAnalytics() {
    try {
        const data = await apiCall('/analytics/stats', { silent: true });
        const s = data.stats;

        // Compute safety rate
        const total = s.conversations.total || 0;
        const safe = s.conversations.safe || 0;
        const harmful = s.conversations.harmful || 0;
        const safeRate = total > 0 ? (safe / total * 100).toFixed(1) : '0.0';

        document.getElementById('analytics-stats').innerHTML = `
            <div class="stat-card stat-card-safe"><div class="value">${safe}</div><div class="label">Safe Responses (${safeRate}%)</div></div>
            <div class="stat-card stat-card-harmful"><div class="value">${harmful}</div><div class="label">Harmful Responses</div></div>
            <div class="stat-card stat-card-total"><div class="value">${total}</div><div class="label">Total Conversations</div></div>
            <div class="stat-card stat-card-models"><div class="value">${s.models.enabled}</div><div class="label">Enabled Models</div></div>
        `;

        // Models chart - stacked bar with safe/harmful
        if (analyticsCharts.models) analyticsCharts.models.destroy();
        const modelsCtx = document.getElementById('chart-models').getContext('2d');
        const byModel = s.conversations.by_model || {};
        analyticsCharts.models = new Chart(modelsCtx, {
            type: 'bar',
            data: {
                labels: Object.keys(byModel),
                datasets: [{ label: 'Conversations', data: Object.values(byModel), backgroundColor: '#2563eb' }],
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } } },
        });

        // Corridors chart
        if (analyticsCharts.corridors) analyticsCharts.corridors.destroy();
        const corrCtx = document.getElementById('chart-corridors').getContext('2d');
        const byCorridor = s.prompts.by_corridor || {};
        analyticsCharts.corridors = new Chart(corrCtx, {
            type: 'bar',
            data: {
                labels: Object.keys(byCorridor),
                datasets: [{ label: 'Prompts', data: Object.values(byCorridor), backgroundColor: '#16a34a' }],
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, indexAxis: 'y' },
        });

        // Attack strategy chart
        loadAttackStrategyChart();
        // Coverage matrix
        loadCoverageMatrix();
    } catch (e) {}
}

async function loadAttackStrategyChart() {
    try {
        const data = await apiCall('/analytics/attack-strategies', { silent: true });
        const strategies = data.strategies || [];
        if (!strategies.length) {
            document.getElementById('attack-strategy-table').innerHTML =
                '<div style="color:var(--gray-400);font-size:12px;text-align:center;padding:12px">No attack strategies registered yet.</div>';
            return;
        }

        if (analyticsCharts.attackStrategies) analyticsCharts.attackStrategies.destroy();
        const ctx = document.getElementById('chart-attack-strategies').getContext('2d');
        const labels = strategies.map(s => (s.name || s.id || '').replace(/_/g, ' '));
        const counts = strategies.map(s => s.mutation_count || s.count || 1);
        const colors = strategies.map((_, i) => {
            const hue = (i * 360 / strategies.length) % 360;
            return `hsl(${hue}, 55%, 55%)`;
        });

        analyticsCharts.attackStrategies = new Chart(ctx, {
            type: 'bar',
            data: {
                labels,
                datasets: [{ label: 'Mutations', data: counts, backgroundColor: colors }],
            },
            options: {
                responsive: true, maintainAspectRatio: false, indexAxis: 'y',
                plugins: { legend: { display: false } },
                scales: { x: { beginAtZero: true } },
            },
        });

        // Strategy table
        let thtml = '<table><thead><tr><th>Strategy</th><th>Category</th><th>Description</th></tr></thead><tbody>';
        for (const s of strategies.slice(0, 10)) {
            thtml += `<tr><td style="font-weight:500">${escHtml((s.name || s.id || '').replace(/_/g, ' '))}</td>
                <td><span class="tag tag-blue">${escHtml(s.category || 'general')}</span></td>
                <td style="font-size:12px;color:var(--gray-500)">${escHtml((s.description || '').substring(0, 100))}</td></tr>`;
        }
        thtml += '</tbody></table>';
        document.getElementById('attack-strategy-table').innerHTML = thtml;
    } catch (e) {
        document.getElementById('attack-strategy-table').innerHTML = '';
    }
}


// =============================================================================
// Conversations
// =============================================================================

async function loadConversations() {
    const result = document.getElementById('conv-filter-result').value;
    const category = document.getElementById('conv-filter-category').value;
    let path = '/analytics/conversations?limit=100';
    if (result) path += '&result=' + result;
    if (category) path += '&category=' + category;

    try {
        const data = await apiCall(path, { silent: true });
        _convCache = data.conversations || [];

        // Populate category filter if not done
        const catSel = document.getElementById('conv-filter-category');
        if (catSel.options.length <= 1 && _convCache.length > 0) {
            const cats = [...new Set(_convCache.map(c => c.category).filter(Boolean))].sort();
            for (const c of cats) {
                const opt = document.createElement('option');
                opt.value = c; opt.textContent = c.replace(/_/g, ' ');
                catSel.appendChild(opt);
            }
        }

        renderConversationList(_convCache);
    } catch (e) {
        document.getElementById('conversations-list').innerHTML = '<div style="color:var(--gray-400);padding:16px;text-align:center">Unable to load conversations</div>';
    }
}

function filterConversationList() {
    const q = (document.getElementById('conv-search-text').value || '').toLowerCase();
    if (!q) { renderConversationList(_convCache); return; }
    const filtered = _convCache.filter(c => {
        const text = [c.id, c.category, c.model_tested, c.corridor, c.result,
            ...(c.messages || c.conversation || []).map(m => m.content || '')]
            .join(' ').toLowerCase();
        return text.includes(q);
    });
    renderConversationList(filtered);
}

function renderConversationList(convs) {
    const list = document.getElementById('conversations-list');
    if (!convs.length) {
        list.innerHTML = '<div style="padding:24px;text-align:center;color:var(--gray-400)">No conversations found</div>';
        return;
    }

    let html = '';
    for (const c of convs) {
        const cls = c.result === 'SAFE' ? 'tag-safe' : c.result === 'HARMFUL' ? 'tag-harmful' : 'tag-pending';
        // Get first message as preview
        const msgs = c.messages || c.conversation || [];
        const preview = msgs.length > 0 ? (msgs[0].content || '').substring(0, 100) : 'No content';
        html += `<div class="conv-list-item" data-conv-id="${escHtml(c.id || '')}" onclick="showConversation('${escHtml(c.id || '')}', this)">
            <div class="conv-list-item-header">
                <span class="conv-list-item-model">${escHtml(c.model_tested || 'Unknown')}</span>
                <span class="tag ${cls}" style="font-size:10px">${c.result || 'N/A'}</span>
            </div>
            <div class="conv-list-item-preview">${escHtml(preview)}</div>
            <div style="display:flex;gap:6px;margin-top:4px">
                ${c.category ? `<span style="font-size:10px;color:var(--gray-400)">${escHtml(c.category.replace(/_/g, ' '))}</span>` : ''}
                ${c.corridor ? `<span style="font-size:10px;color:var(--gray-400)">${escHtml(c.corridor)}</span>` : ''}
            </div>
        </div>`;
    }
    list.innerHTML = html;
}

async function showConversation(id, clickedEl) {
    // Highlight selected item
    document.querySelectorAll('.conv-list-item').forEach(el => el.classList.remove('selected'));
    if (clickedEl) clickedEl.classList.add('selected');

    try {
        const data = await apiCall(`/analytics/conversations/${id}`, { silent: true });
        const conv = data.conversation;

        const cls = conv.result === 'SAFE' ? 'tag-safe' : conv.result === 'HARMFUL' ? 'tag-harmful' : 'tag-pending';
        document.getElementById('conv-detail-title').textContent = conv.model_tested || 'Conversation';
        document.getElementById('conv-detail-meta').innerHTML = `
            <span class="tag ${cls}">${conv.result || 'N/A'}</span>
            ${conv.category ? ` &middot; ${escHtml(conv.category.replace(/_/g, ' '))}` : ''}
            ${conv.corridor ? ` &middot; ${escHtml(conv.corridor)}` : ''}
        `;

        let html = '';
        for (const msg of (conv.messages || conv.conversation || [])) {
            const role = msg.role || 'unknown';
            const bubbleCls = role === 'user' ? 'user-bubble' : 'assistant-bubble';
            html += `<div class="chat-bubble ${bubbleCls}">
                <div class="bubble-meta">${role.toUpperCase()}</div>
                <div style="white-space:pre-wrap">${escHtml(msg.content || '')}</div>
            </div>`;
        }
        document.getElementById('conv-detail-messages').innerHTML = html || '<div style="color:var(--gray-400);text-align:center;padding:20px">No messages</div>';
    } catch (e) {
        document.getElementById('conv-detail-messages').innerHTML = `<div style="color:var(--danger);padding:16px">Error loading conversation: ${escHtml(e.message)}</div>`;
    }
}


// =============================================================================
// Coverage Matrix
// =============================================================================

async function loadCoverageMatrix() {
    try {
        const data = await apiCall('/analytics/coverage', { silent: true });
        _coverageData = data;
        renderCoverageGrid('ilo');
    } catch (e) {
        const c1 = document.getElementById('coverage-grid-container');
        const c2 = document.getElementById('analytics-coverage-container');
        const msg = '<div style="color:var(--gray-400);font-size:12px">No coverage data available</div>';
        if (c1) c1.innerHTML = msg;
        if (c2) c2.innerHTML = msg;
    }
}

function switchCoverageTab(dimension, btn) {
    _coverageTab = dimension;
    if (btn) {
        btn.closest('.coverage-tab-bar').querySelectorAll('.coverage-tab').forEach(t => t.classList.remove('active'));
        btn.classList.add('active');
    }
    renderCoverageGrid(dimension);
}

function renderCoverageGrid(dimension) {
    if (!_coverageData) return;
    const key = dimension === 'ilo' ? 'ilo_by_category' : dimension === 'corridor' ? 'corridor_by_category' : 'attack_by_category';
    const d = _coverageData[key];
    if (!d) return;

    let html = '<div style="overflow-x:auto"><table class="heatmap-table" style="font-size:11px"><thead><tr><th></th>';
    for (const col of d.columns) html += `<th>${escHtml(col.replace(/_/g, ' '))}</th>`;
    html += '</tr></thead><tbody>';
    for (const row of d.rows) {
        html += `<tr><td style="font-weight:500;white-space:nowrap">${escHtml(row.replace(/_/g, ' '))}</td>`;
        for (const col of d.columns) {
            const cell = (d.matrix[row] || {})[col] || { total: 0, tested: 0 };
            if (cell.total === 0) {
                html += '<td class="coverage-cell coverage-cell-empty">-</td>';
            } else {
                const pct = cell.tested / cell.total;
                const cls = pct === 0 ? 'coverage-cell-none' : pct < 0.5 ? 'coverage-cell-low' : 'coverage-cell-good';
                html += `<td class="coverage-cell ${cls}" title="${cell.tested}/${cell.total} tested, ${cell.safe} safe, ${cell.harmful} harmful">${cell.tested}/${cell.total}</td>`;
            }
        }
        html += '</tr>';
    }
    html += '</tbody></table></div>';

    const c1 = document.getElementById('coverage-grid-container');
    const c2 = document.getElementById('analytics-coverage-container');
    if (c1) c1.innerHTML = html;
    if (c2) c2.innerHTML = html;
}


// =============================================================================
// Response Deep-Dive Viewer
// =============================================================================

async function loadDeepDiveIndicators() {
    if (_ddIndicators) return;
    try {
        _ddIndicators = await apiCall('/analytics/classification-indicators', { silent: true });
    } catch (e) {
        _ddIndicators = { safe_indicators: [], harmful_indicators: [] };
    }
}

function openDeepDive(idx) {
    loadDeepDiveIndicators();
    _ddIndex = idx || 0;
    // Switch to deep-dive tab
    const tabs = document.querySelectorAll('.rv-tab');
    tabs.forEach(t => t.classList.remove('active'));
    tabs[tabs.length - 1].classList.add('active');
    document.querySelectorAll('.rv-panel').forEach(p => p.classList.remove('active'));
    document.getElementById('rv-panel-deep-dive').classList.add('active');
    renderDeepDive();
}

function deepDiveNav(delta) {
    _ddIndex = Math.max(0, Math.min(_ddResults.length - 1, _ddIndex + delta));
    renderDeepDive();
}

function renderDeepDive() {
    const container = document.getElementById('dd-content');
    if (!_ddResults.length) {
        container.innerHTML = '<div style="color:var(--gray-400);text-align:center;padding:24px">No results to display</div>';
        return;
    }
    const r = _ddResults[_ddIndex];
    document.getElementById('dd-counter').textContent = `${_ddIndex + 1} / ${_ddResults.length}`;

    const cls = r.classification || 'UNCLEAR';
    const clsColor = cls === 'SAFE' ? 'var(--success)' : cls === 'HARMFUL' ? 'var(--danger)' : 'var(--warning)';

    let metaHtml = '';
    if (r.model) metaHtml += `<span class="tag tag-blue">${escHtml(r.model)}</span>`;
    metaHtml += `<span class="tag" style="background:${clsColor};color:#fff">${cls}</span>`;
    if (r.confidence !== undefined) metaHtml += `<span class="tag tag-gray">Confidence: ${(r.confidence * 100).toFixed(0)}%</span>`;
    if (r.source) metaHtml += `<span class="tag tag-gray">${escHtml(r.source)}</span>`;

    const responseHtml = highlightIndicators(r.response || '');

    container.innerHTML = `
        <div class="deep-dive-meta">${metaHtml}</div>
        <div class="deep-dive-prompt"><strong>Prompt:</strong> ${escHtml(r.prompt || '')}</div>
        <div style="font-size:12px;font-weight:500;margin-bottom:4px;color:var(--gray-600)">Response:</div>
        <div class="deep-dive-response">${responseHtml}</div>
    `;
}

function highlightIndicators(text) {
    if (!text) return '';
    let html = escHtml(text);
    const ind = _ddIndicators || { safe_indicators: [], harmful_indicators: [] };
    for (const phrase of ind.safe_indicators || []) {
        const re = new RegExp('(' + phrase.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
        html = html.replace(re, '<span class="indicator-safe">$1</span>');
    }
    for (const phrase of ind.harmful_indicators || []) {
        const re = new RegExp('(' + phrase.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
        html = html.replace(re, '<span class="indicator-harmful">$1</span>');
    }
    return html;
}


// =============================================================================
// Run Viewer
// =============================================================================

async function openRunViewer(runId) {
    _rvRunId = runId;
    document.getElementById('run-viewer-overlay').classList.add('open');
    document.getElementById('rv-results-table').innerHTML = '<div class="loading">Loading results...</div>';
    const comparePanel = document.getElementById('rv-panel-compare');
    if (comparePanel) {
        const compareContent = comparePanel.querySelector('#rv-compare-content');
        if (compareContent) compareContent.innerHTML = '<div class="loading">Loading...</div>';
    }
    try {
        const [runResp, summResp] = await Promise.all([
            apiCall(`/analytics/tests/runs/${runId}`, { silent: true }),
            apiCall(`/analytics/tests/runs/${runId}/summary`, { silent: true }),
        ]);
        _rvRunData = runResp.run;
        _rvSummary = summResp;
        _ddResults = _rvRunData.results || [];
        // Header
        document.getElementById('rv-title').textContent = `Run: ${runId.substring(0, 20)}`;
        const started = _rvRunData.started_at ? new Date(_rvRunData.started_at).toLocaleString() : '';
        const statusCls = _rvRunData.status === 'completed' ? 'tag-safe' : _rvRunData.status === 'running' ? 'tag-blue' : 'tag-pending';
        const models = (_rvRunData.models || []).map(m => `<span class="model-tag">${escHtml(m.name || m)}</span>`).join(' ');
        document.getElementById('rv-meta').innerHTML = `${started} &middot; <span class="tag ${statusCls}">${_rvRunData.status}</span> &middot; ${models}`;
        // Stats
        document.getElementById('rv-stats').innerHTML = `
            <div class="rv-stat safe"><div class="val">${_rvSummary.safe}</div><div class="lbl">Safe</div></div>
            <div class="rv-stat harmful"><div class="val">${_rvSummary.harmful}</div><div class="lbl">Harmful</div></div>
            <div class="rv-stat unclear"><div class="val">${_rvSummary.unclear}</div><div class="lbl">Unclear</div></div>
            <div class="rv-stat error"><div class="val">${_rvSummary.error}</div><div class="lbl">Error</div></div>
        `;
        // Populate model filter
        const modelSelect = document.getElementById('rv-filter-model');
        modelSelect.innerHTML = '<option value="">All Models</option>';
        const modelNames = [...new Set((_rvRunData.results || []).map(r => r.model).filter(Boolean))];
        for (const m of modelNames) {
            modelSelect.innerHTML += `<option value="${escHtml(m)}">${escHtml(m)}</option>`;
        }
        // Reset to Results tab
        switchRunViewerTab('results', document.querySelector('.rv-tab'));
        filterRunResults();
    } catch (e) {
        document.getElementById('rv-results-table').innerHTML = `<div style="color:var(--danger);padding:16px">${escHtml(e.message)}</div>`;
    }
}

function closeRunViewer() {
    document.getElementById('run-viewer-overlay').classList.remove('open');
    _rvRunId = null;
    _rvRunData = null;
    _rvSummary = null;
}

function switchRunViewerTab(tab, clickedEl) {
    document.querySelectorAll('.rv-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.rv-panel').forEach(p => p.classList.remove('active'));
    if (clickedEl) clickedEl.classList.add('active');
    else document.querySelector(`.rv-tab`).classList.add('active');
    document.getElementById(`rv-panel-${tab}`).classList.add('active');
    if (tab === 'compare' && _rvRunId) loadModelComparison(_rvRunId);
    if (tab === 'deep-dive') renderDeepDive();
}

function filterRunResults() {
    if (!_rvRunData) return;
    const modelFilter = document.getElementById('rv-filter-model').value;
    const classFilter = document.getElementById('rv-filter-class').value;
    const searchFilter = document.getElementById('rv-filter-search').value.toLowerCase();
    let results = (_rvRunData.results || []).map((r, i) => ({ ...r, _idx: i }));
    if (modelFilter) results = results.filter(r => r.model === modelFilter);
    if (classFilter) results = results.filter(r => r.classification === classFilter);
    if (searchFilter) results = results.filter(r => (r.prompt || '').toLowerCase().includes(searchFilter) || (r.response || '').toLowerCase().includes(searchFilter));
    renderRunResults(results);
}

function renderRunResults(results) {
    const el = document.getElementById('rv-results-table');
    if (!results.length) { el.innerHTML = '<div class="empty">No results match filters</div>'; return; }
    let html = `<table><thead><tr><th>#</th><th style="width:35%">Prompt</th><th>Model</th><th>Classification</th><th>Confidence</th><th>Actions</th></tr></thead><tbody>`;
    for (const r of results) {
        const cls = r.classification === 'SAFE' ? 'tag-safe' : r.classification === 'HARMFUL' ? 'tag-harmful' : r.classification === 'ERROR' ? 'tag-pending' : 'tag-blue';
        const confPct = Math.round((r.confidence || 0) * 100);
        const confColor = r.classification === 'SAFE' ? 'var(--success)' : r.classification === 'HARMFUL' ? 'var(--danger)' : 'var(--gray-400)';
        const overrideNote = r.override_note ? ` <span style="font-size:10px;color:var(--primary)" title="${escHtml(r.override_note)}">(overridden)</span>` : '';
        const promptPreview = (r.prompt || '').substring(0, 80) + ((r.prompt || '').length > 80 ? '...' : '');
        html += `<tr onclick="toggleResultDetail(${r._idx})" style="cursor:pointer">
            <td style="font-size:11px;color:var(--gray-400)">${r._idx + 1}</td>
            <td style="font-size:12px">${escHtml(promptPreview)}</td>
            <td style="font-size:12px">${escHtml(r.model)}</td>
            <td><span class="tag ${cls}">${r.classification}</span>${overrideNote}</td>
            <td><div class="confidence-bar"><div class="fill" style="width:${confPct}%;background:${confColor}"></div></div> <span style="font-size:11px;color:var(--gray-500)">${confPct}%</span></td>
            <td><button class="btn btn-sm" onclick="event.stopPropagation();toggleResultDetail(${r._idx})">Detail</button> <button class="btn btn-sm btn-primary" onclick="event.stopPropagation();openDeepDive(${r._idx})" title="Deep Dive">&#128269;</button></td>
        </tr>`;
        html += `<tr class="rv-detail-row" id="rv-detail-${r._idx}"><td colspan="6" class="rv-detail-cell">
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
                <div><strong style="font-size:11px;color:var(--gray-500)">PROMPT</strong><pre>${escHtml(r.prompt || '')}</pre></div>
                <div><strong style="font-size:11px;color:var(--gray-500)">RESPONSE</strong><pre>${escHtml(r.response || r.error || 'No response')}</pre></div>
            </div>
            <div style="display:flex;align-items:center;gap:8px;margin-top:10px;padding-top:10px;border-top:1px solid var(--gray-200)">
                <span style="font-size:11px;font-weight:600;color:var(--gray-500)">Override:</span>
                <select id="rv-override-cls-${r._idx}" style="font-size:12px;padding:3px 6px">
                    <option value="SAFE" ${r.classification === 'SAFE' ? 'selected' : ''}>SAFE</option>
                    <option value="HARMFUL" ${r.classification === 'HARMFUL' ? 'selected' : ''}>HARMFUL</option>
                    <option value="UNCLEAR" ${r.classification === 'UNCLEAR' ? 'selected' : ''}>UNCLEAR</option>
                </select>
                <input type="text" id="rv-override-note-${r._idx}" placeholder="Note..." value="${escHtml(r.override_note || '')}" style="font-size:12px;padding:3px 6px;flex:1">
                <button class="btn btn-sm btn-primary" onclick="event.stopPropagation();overrideClassification(${r._idx})">Save</button>
            </div>
        </td></tr>`;
    }
    html += '</tbody></table>';
    el.innerHTML = html;
}

function toggleResultDetail(idx) {
    const row = document.getElementById(`rv-detail-${idx}`);
    if (row) row.classList.toggle('open');
}

async function overrideClassification(idx) {
    const cls = document.getElementById(`rv-override-cls-${idx}`).value;
    const note = document.getElementById(`rv-override-note-${idx}`).value;
    try {
        await apiCall(`/analytics/tests/runs/${_rvRunId}/override`, {
            method: 'POST',
            body: JSON.stringify({ result_index: idx, classification: cls, note }),
        });
        toast('Classification updated');
        // Refresh viewer
        openRunViewer(_rvRunId);
    } catch (e) {
        toast(e.message, 'error');
    }
}

function exportRunResults(format) {
    if (!_rvRunData) return;
    const results = _rvRunData.results || [];
    if (format === 'json') {
        const blob = new Blob([JSON.stringify(results, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url; a.download = `${_rvRunId}_results.json`; a.click();
        URL.revokeObjectURL(url);
    } else if (format === 'csv') {
        let csv = 'Prompt,Model,Classification,Confidence,Source\n';
        for (const r of results) {
            csv += `"${(r.prompt || '').replace(/"/g, '""')}","${r.model}","${r.classification}",${r.confidence},"${r.source || ''}"\n`;
        }
        const blob = new Blob([csv], { type: 'text/csv' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url; a.download = `${_rvRunId}_results.csv`; a.click();
        URL.revokeObjectURL(url);
    } else if (format === 'html') {
        window.open(`${API}/analytics/tests/runs/${_rvRunId}/export/html`, '_blank');
    }
}


// =============================================================================
// Model Comparison (in-run viewer)
// =============================================================================

async function loadModelComparison(runId) {
    const el = document.getElementById('rv-compare-content');
    el.innerHTML = '<div class="loading">Loading comparison...</div>';
    try {
        const data = await apiCall(`/analytics/tests/runs/${runId}/compare`, { silent: true });
        renderComparisonTable(data);
    } catch (e) {
        el.innerHTML = `<div style="color:var(--danger);padding:16px">${escHtml(e.message)}</div>`;
    }
}

function renderComparisonTable(data) {
    const el = document.getElementById('rv-compare-content');
    const models = data.models || [];
    const prompts = data.prompts || [];
    const summary = data.summary || {};

    if (!models.length) { el.innerHTML = '<div class="empty">No model comparison data available</div>'; return; }

    // Summary cards
    const agreePct = summary.total_prompts > 0 ? Math.round(summary.full_agreement / summary.total_prompts * 100) : 0;
    let html = `<div class="rv-stat-row" style="margin-bottom:16px">
        <div class="rv-stat"><div class="val">${agreePct}%</div><div class="lbl">Agreement</div></div>
        <div class="rv-stat safe"><div class="val">${summary.full_agreement}</div><div class="lbl">Agree</div></div>
        <div class="rv-stat harmful"><div class="val">${summary.disagreement}</div><div class="lbl">Disagree</div></div>
    </div>`;
    // Per-model rates
    html += '<div style="display:flex;gap:12px;margin-bottom:16px;flex-wrap:wrap">';
    for (const m of models) {
        const pm = (summary.per_model || {})[m] || {};
        const total = (pm.safe || 0) + (pm.harmful || 0) + (pm.unclear || 0) + (pm.error || 0);
        const safeRate = total > 0 ? Math.round((pm.safe || 0) / total * 100) : 0;
        html += `<div style="padding:8px 12px;border:1px solid var(--gray-200);border-radius:6px;font-size:12px">
            <strong>${escHtml(m)}</strong><br>
            <span style="color:var(--success)">${pm.safe || 0} safe (${safeRate}%)</span> &middot;
            <span style="color:var(--danger)">${pm.harmful || 0} harmful</span>
        </div>`;
    }
    html += '</div>';
    // Comparison table
    html += '<table><thead><tr><th style="width:30%">Prompt</th>';
    for (const m of models) html += `<th>${escHtml(m)}</th>`;
    html += '</tr></thead><tbody>';
    for (let pi = 0; pi < prompts.length; pi++) {
        const p = prompts[pi];
        const rowClass = p.agreement ? '' : 'rv-disagree';
        const promptPreview = (p.prompt || '').substring(0, 60) + ((p.prompt || '').length > 60 ? '...' : '');
        html += `<tr class="${rowClass}"><td style="font-size:12px" title="${escHtml(p.prompt)}">${escHtml(promptPreview)}</td>`;
        for (const m of models) {
            const resp = (p.responses || {})[m];
            if (resp) {
                const cls = resp.classification === 'SAFE' ? 'tag-safe' : resp.classification === 'HARMFUL' ? 'tag-harmful' : 'tag-pending';
                const preview = (resp.response || '').substring(0, 50);
                html += `<td><span class="tag ${cls}">${resp.classification}</span><br><span style="font-size:11px;color:var(--gray-400)" title="${escHtml(resp.response || '')}">${escHtml(preview)}${preview.length < (resp.response || '').length ? '...' : ''}</span></td>`;
            } else {
                html += '<td style="color:var(--gray-400);font-size:11px">N/A</td>';
            }
        }
        html += '</tr>';
    }
    html += '</tbody></table>';
    el.innerHTML = html;
}


// =============================================================================
// Model Comparison Page (standalone)
// =============================================================================

async function loadComparisonPage() {
    // Populate model checkboxes
    try {
        const epData = await apiCall('/endpoints', { silent: true });
        const endpoints = epData.endpoints || [];
        let html = '';
        for (const ep of endpoints) {
            for (const m of (ep.models || [])) {
                html += `<label style="display:flex;align-items:center;gap:6px;padding:3px 0;font-size:13px">
                    <input type="checkbox" class="compare-model-cb" value="${escHtml(m.id)}"> ${escHtml(m.name)}
                </label>`;
            }
        }
        document.getElementById('compare-model-checkboxes').innerHTML = html || '<div style="color:var(--gray-400);font-size:12px">No models configured</div>';

        // Populate prompt sets
        const psData = await apiCall('/prompts/sets', { silent: true });
        const sel = document.getElementById('compare-prompt-set');
        sel.innerHTML = '<option value="">Select a set...</option>';
        for (const s of (psData.sets || [])) {
            sel.innerHTML += `<option value="${escHtml(s.id || s.name)}">${escHtml(s.name)} (${s.prompt_count || 0})</option>`;
        }
    } catch (e) {}
}

function toggleCompareSource() {
    const src = document.getElementById('compare-prompt-source').value;
    document.getElementById('compare-custom-group').style.display = src === 'custom' ? 'block' : 'none';
    document.getElementById('compare-set-group').style.display = src === 'set' ? 'block' : 'none';
}

async function runComparison() {
    const modelIds = [...document.querySelectorAll('.compare-model-cb:checked')].map(c => c.value);
    if (modelIds.length < 2) { toast('Select at least 2 models'); return; }

    const src = document.getElementById('compare-prompt-source').value;
    const body = { model_ids: modelIds, max_prompts: parseInt(document.getElementById('compare-max-prompts').value) || 10 };

    if (src === 'custom') {
        body.custom_prompts = document.getElementById('compare-custom-prompts').value.split('\n').filter(l => l.trim());
        if (!body.custom_prompts.length) { toast('Enter at least one prompt'); return; }
    } else if (src === 'set') {
        body.prompt_set = document.getElementById('compare-prompt-set').value;
        if (!body.prompt_set) { toast('Select a prompt set'); return; }
    } else {
        loadRunComparison();
        return;
    }

    const area = document.getElementById('compare-results-area');
    area.innerHTML = '<div class="loading">Running comparison... this may take a while</div>';
    try {
        const data = await apiCall('/analytics/compare', { method: 'POST', body: JSON.stringify(body) });
        renderComparisonResults(data);
    } catch (e) {
        area.innerHTML = `<div style="color:var(--danger)">${escHtml(e.message)}</div>`;
    }
}

async function loadRunComparison() {
    const area = document.getElementById('compare-results-area');
    area.innerHTML = '<div class="loading">Loading comparison from runs...</div>';
    try {
        const data = await apiCall('/analytics/compare/from-runs');
        renderComparisonResults(data);
    } catch (e) {
        area.innerHTML = `<div style="color:var(--danger)">${escHtml(e.message)}</div>`;
    }
}

function renderComparisonResults(data) {
    const area = document.getElementById('compare-results-area');
    if (!data.results || !data.results.length) {
        area.innerHTML = '<div class="card" style="text-align:center;color:var(--gray-400);padding:24px">No comparison results available</div>';
        return;
    }

    // Summary cards
    let html = `<div class="card-row" style="margin-bottom:16px">
        <div class="stat-card stat-card-total"><div class="value">${data.prompt_count}</div><div class="label">Prompts Compared</div></div>
        <div class="stat-card stat-card-models"><div class="value">${data.model_count || data.models?.length || '?'}</div><div class="label">Models</div></div>
        <div class="stat-card stat-card-safe"><div class="value">${(data.agreement_rate * 100).toFixed(0)}%</div><div class="label">Agreement Rate</div></div>
    </div>`;

    // Collect all model names
    const modelNames = new Set();
    for (const r of data.results) {
        for (const [mid, v] of Object.entries(r.responses || {})) modelNames.add(v.model_name || mid);
    }
    const models = [...modelNames];

    // Comparison table
    html += '<div class="card" style="overflow-x:auto"><table class="compare-table"><thead><tr><th style="min-width:200px">Prompt</th>';
    for (const m of models) html += `<th>${escHtml(m)}</th>`;
    html += '<th>Agree?</th></tr></thead><tbody>';

    for (const r of data.results) {
        const rowClass = r.agreement ? '' : 'compare-disagree';
        html += `<tr class="${rowClass}"><td style="font-size:12px;max-width:250px">${escHtml((r.prompt || '').substring(0, 150))}${(r.prompt || '').length > 150 ? '...' : ''}</td>`;
        for (const m of models) {
            const resp = Object.values(r.responses || {}).find(v => (v.model_name || '') === m);
            if (resp) {
                const cls = resp.classification || 'UNCLEAR';
                const clsColor = cls === 'SAFE' ? '#16a34a' : cls === 'HARMFUL' ? '#dc2626' : '#f59e0b';
                html += `<td><span style="display:inline-block;padding:2px 6px;border-radius:3px;font-size:10px;background:${clsColor};color:#fff;margin-bottom:4px">${cls}</span>
                    <div class="compare-response-cell">${escHtml((resp.response || '').substring(0, 200))}</div></td>`;
            } else {
                html += '<td style="color:var(--gray-300)">N/A</td>';
            }
        }
        html += `<td style="text-align:center">${r.agreement ? '<span style="color:var(--success);font-size:16px">&#10003;</span>' : '<span style="color:var(--danger);font-size:16px">&#10007;</span>'}</td></tr>`;
    }
    html += '</tbody></table></div>';
    area.innerHTML = html;
}
