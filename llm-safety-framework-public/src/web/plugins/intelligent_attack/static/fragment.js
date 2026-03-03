// =============================================================================
// Intelligent Attack Plugin
// =============================================================================

SECTION_LOADERS['intelligent-attack'] = function () {
    loadEmbeddingSources();
    loadAnalysisHistory();
};

async function loadEmbeddingSources() {
    try {
        const data = await apiCall('/intelligent-attack/embedding-sources', { silent: true });
        const container = document.getElementById('embedding-sources');
        if (!data.sources || data.sources.length === 0) {
            container.innerHTML = '<div style="color:var(--gray-400)">No embedding sources available. Configure an API endpoint with a key, or install sentence-transformers.</div>';
            return;
        }
        let html = '<table><thead><tr><th>Source</th><th>Type</th><th>Dimensions</th></tr></thead><tbody>';
        for (const s of data.sources) {
            html += `<tr><td>${escHtml(s.name)}</td><td><span class="tag tag-blue">${s.type}</span></td><td>${s.dimensions || 'auto'}</td></tr>`;
        }
        html += '</tbody></table>';
        container.innerHTML = html;
    } catch (e) {}
}

async function runAnalysis() {
    toast('Running analysis...');
    try {
        const data = await apiCall('/intelligent-attack/analyze', { method: 'POST', body: JSON.stringify({}) });
        document.getElementById('analysis-results').innerHTML = data.analysis
            ? `<div class="preview-box">${escHtml(JSON.stringify(data.analysis, null, 2))}</div>`
            : `<div style="color:var(--gray-400)">${data.message || 'No analysis results'}</div>`;
    } catch (e) {}
}

async function suggestProbes() {
    toast('Generating probes...');
    document.getElementById('analysis-results').innerHTML = '<div class="loading">Generating targeted probes...</div>';
    try {
        const data = await apiCall('/intelligent-attack/suggest-probes', { method: 'POST', body: JSON.stringify({}) });
        if (data.probes && data.probes.length) {
            let html = `<div style="font-size:12px;color:var(--gray-500);margin-bottom:12px">${data.probes.length} probes generated targeting guardrail gaps</div>`;
            for (const p of data.probes) {
                const sevCls = p.severity === 'critical' ? 'gap-sev-critical' : p.severity === 'high' ? 'gap-sev-high' : 'gap-sev-medium';
                html += `<div class="gap-card">
                    <div class="gap-card-header">
                        <span class="gap-sev ${sevCls}">${escHtml(p.severity || 'unknown')}</span>
                        <span style="font-size:12px;color:var(--gray-500)">Gap: ${escHtml(p.gap_id || '')}</span>
                        <span class="feature-pill feature-pill-attack" style="margin-left:auto">${escHtml(p.strategy || 'direct')}</span>
                    </div>
                    <div style="font-size:13px;color:var(--gray-700);padding:8px 12px;background:var(--gray-50);border-radius:6px;margin-top:6px">${escHtml(p.probe || '')}</div>
                    <div style="margin-top:8px;display:flex;gap:6px">
                        <button class="btn btn-sm" onclick="showSection('testing').then(()=>{const el=document.getElementById('test-prompt');if(el)el.value=this.dataset.probe})" data-probe="${escHtml(p.probe || '')}">Quick Test</button>
                    </div>
                </div>`;
            }
            document.getElementById('analysis-results').innerHTML = html;
        } else {
            document.getElementById('analysis-results').innerHTML = `<div style="color:var(--gray-400)">${escHtml(data.message || 'No probes available. Run a full analysis first.')}</div>`;
        }
    } catch (e) {}
}

async function extractFeatures() {
    const text = document.getElementById('feature-prompts').value;
    if (!text.trim()) return toast('Enter some prompts', 'error');
    const prompts = text.split('\n').filter(l => l.trim());
    toast('Extracting features...');
    try {
        const data = await apiCall('/intelligent-attack/features', {
            method: 'POST', body: JSON.stringify({ prompts }),
        });
        let html = '';
        for (let i = 0; i < data.features.length; i++) {
            const f = data.features[i];
            const iloHtml = f.ilo_indicators.length
                ? f.ilo_indicators.map(ind => `<span class="feature-pill feature-pill-ilo">${escHtml(ind)}</span>`).join('')
                : '<span style="color:var(--gray-400);font-size:11px">none detected</span>';
            const atkHtml = f.attack_types.length
                ? f.attack_types.map(at => `<span class="feature-pill feature-pill-attack">${escHtml(at)}</span>`).join('')
                : '<span style="color:var(--gray-400);font-size:11px">none detected</span>';
            html += `<div style="padding:10px 0;border-bottom:1px solid var(--gray-100)">
                <div style="font-size:12px;color:var(--gray-700);margin-bottom:6px">${escHtml(prompts[i].substring(0, 120))}${prompts[i].length > 120 ? '...' : ''}</div>
                <div style="margin-bottom:4px"><span style="font-size:10px;font-weight:600;color:var(--gray-500);margin-right:6px">ILO:</span>${iloHtml}</div>
                <div><span style="font-size:10px;font-weight:600;color:var(--gray-500);margin-right:6px">ATTACKS:</span>${atkHtml}</div>
                <div style="font-size:10px;color:var(--gray-400);margin-top:4px">${f.word_count} words</div>
            </div>`;
        }
        document.getElementById('feature-results').innerHTML = html;
    } catch (e) {}
}

async function runFullAnalysis() {
    toast('Running full feature space analysis on pipeline...');
    document.getElementById('analysis-results').innerHTML = '<div class="loading">Analyzing feature space...</div>';
    try {
        const data = await apiCall('/intelligent-attack/analyze/run', {
            method: 'POST', body: JSON.stringify({ min_cluster_size: 5, harm_rate_threshold: 0.3 }),
        });
        let html = '';
        if (data.analysis) {
            const a = data.analysis;
            html += `<div class="card-row" style="margin-bottom:16px">
                <div class="stat-card stat-card-total"><div class="value">${a.total_points || 0}</div><div class="label">Points Analyzed</div></div>
                <div class="stat-card"><div class="value">${a.n_clusters || 0}</div><div class="label">Clusters Found</div></div>
                <div class="stat-card stat-card-harmful"><div class="value">${data.gaps ? data.gaps.length : 0}</div><div class="label">Gaps Identified</div></div>
                <div class="stat-card"><div class="value">${data.feature_dimensions || 0}</div><div class="label">Feature Dims</div></div>
            </div>`;

            if (a.clusters && a.clusters.length) {
                html += '<h4 style="margin-bottom:10px">Clusters</h4><div class="cluster-grid" style="margin-bottom:16px">';
                for (const cl of a.clusters) {
                    const harmPct = ((cl.harm_rate || 0) * 100).toFixed(0);
                    const harmColor = harmPct > 50 ? 'var(--danger)' : harmPct > 20 ? 'var(--warning)' : 'var(--success)';
                    html += `<div class="cluster-card">
                        <div class="cluster-card-id">Cluster ${escHtml(cl.id || cl.label || '?')}</div>
                        <div class="cluster-card-harm">
                            <span class="harm-pct" style="color:${harmColor}">${harmPct}%</span>
                            <span style="font-size:11px;color:var(--gray-500)">harm rate</span>
                        </div>
                        <div class="progress-track"><div class="progress-fill" style="width:${harmPct}%;background:${harmColor}"></div></div>
                        <div class="cluster-card-meta">${cl.size || 0} prompts</div>
                    </div>`;
                }
                html += '</div>';
            }

            if (data.gaps && data.gaps.length) {
                html += '<h4 style="margin-bottom:10px">Guardrail Gaps</h4>';
                for (const g of data.gaps) {
                    const sevCls = g.severity === 'critical' ? 'gap-sev-critical' : g.severity === 'high' ? 'gap-sev-high' : g.severity === 'medium' ? 'gap-sev-medium' : 'gap-sev-low';
                    const harmPct = ((g.harm_rate || 0) * 100).toFixed(0);
                    html += `<div class="gap-card">
                        <div class="gap-card-header">
                            <span class="gap-sev ${sevCls}">${escHtml(g.severity || 'unknown')}</span>
                            <strong style="font-size:13px">${escHtml(g.id || '')}</strong>
                        </div>
                        <div class="gap-card-stats">
                            <span><strong>${g.size || 0}</strong> prompts</span>
                            <span>Harm rate: <strong>${harmPct}%</strong> <span class="harm-bar" style="width:${Math.max(4, Math.min(60, harmPct * 0.6))}px"></span></span>
                        </div>
                        ${g.description ? `<div style="font-size:12px;color:var(--gray-500);margin-top:6px">${escHtml(g.description)}</div>` : ''}
                    </div>`;
                }
            }
        } else {
            html = `<div style="color:var(--gray-400)">${data.detail || 'Analysis requires numpy/scikit-learn. Install with: pip install numpy scikit-learn'}</div>`;
        }
        document.getElementById('analysis-results').innerHTML = html;
    } catch (e) {
        document.getElementById('analysis-results').innerHTML = `<div style="color:var(--warning)">${escHtml(e.message || 'Analysis failed - ensure numpy and scikit-learn are installed')}</div>`;
    }
}

async function loadAnalysisHistory() {
    try {
        const data = await apiCall('/intelligent-attack/analyses', { silent: true });
        const el = document.getElementById('analysis-history');
        if (!data.analyses || data.analyses.length === 0) {
            el.innerHTML = '<div style="color:var(--gray-400);font-size:12px;text-align:center;padding:12px">No analyses saved yet. Run a full analysis first.</div>';
            return;
        }
        let html = '<table><thead><tr><th>ID</th><th>Created</th><th>Points</th><th>Clusters</th><th>Actions</th></tr></thead><tbody>';
        for (const a of data.analyses) {
            html += `<tr>
                <td style="font-family:monospace;font-size:11px">${escHtml((a.id || '').substring(0, 16))}</td>
                <td style="font-size:12px">${a.created_at ? new Date(a.created_at).toLocaleString() : ''}</td>
                <td>${a.total_points || 0}</td>
                <td>${a.n_clusters || 0}</td>
                <td><button class="btn btn-sm" onclick="runAnalysis()">Load</button></td>
            </tr>`;
        }
        html += '</tbody></table>';
        el.innerHTML = html;
    } catch (e) {
        document.getElementById('analysis-history').innerHTML = '<div style="color:var(--gray-400)">Unable to load analyses</div>';
    }
}
