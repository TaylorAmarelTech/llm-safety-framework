// =============================================================================
// Document Agent Plugin
// =============================================================================

let _daCurrentTab = 'sources';
let _daJobPollTimer = null;
let _daDocPage = 0;

SECTION_LOADERS['doc-agent'] = function() { switchDocAgentTab('sources'); };

function switchDocAgentTab(tab) {
    _daCurrentTab = tab;
    document.querySelectorAll('#section-doc-agent .da-tab').forEach(t => t.style.display = 'none');
    document.getElementById('da-tab-' + tab).style.display = '';
    const tabBtns = document.querySelectorAll('#section-doc-agent .tab-btn');
    tabBtns.forEach(b => b.classList.remove('active'));
    const tabNames = ['sources', 'documents', 'kb', 'jobs', 'settings', 'indicator-matrix'];
    const idx = tabNames.indexOf(tab);
    if (idx >= 0 && tabBtns[idx]) tabBtns[idx].classList.add('active');
    if (tab === 'sources') loadScraperSources();
    else if (tab === 'documents') loadScraperDocs();
    else if (tab === 'kb') { loadKBStats(); queryKB(); }
    else if (tab === 'jobs') loadScraperJobs();
    else if (tab === 'settings') { loadStealthStatus(); loadStealthConfig(); }
    else if (tab === 'indicator-matrix') { loadIMGrid(); loadIMSectors(); loadIMCorridors(); }
}

const TIER_LABELS = {1:'IGO', 2:'PH Govt', 3:'ID Govt', 4:'Dest Reg', 5:'NGO', 6:'Courts', 7:'Academic'};
const TIER_COLORS = {1:'#6366f1', 2:'#22c55e', 3:'#f59e0b', 4:'#3b82f6', 5:'#ec4899', 6:'#14b8a6', 7:'#8b5cf6'};

async function loadScraperSources() {
    const tierFilter = document.getElementById('da-tier-filter').value;
    let url = '/scraper/sources';
    if (tierFilter) url += '?tier=' + tierFilter;
    try {
        // Fetch sources and health in parallel
        const [d, hd] = await Promise.all([
            apiCall(url),
            apiCall('/scraper/sources/health').catch(() => ({ sources: [] }))
        ]);
        const sources = d.sources || [];
        const healthMap = {};
        (hd.sources || []).forEach(h => { healthMap[h.source_id] = h; });
        let html = '<table style="width:100%;border-collapse:collapse"><thead><tr>' +
            '<th style="text-align:left;padding:8px;border-bottom:1px solid var(--gray-200)">Tier</th>' +
            '<th style="text-align:left;padding:8px;border-bottom:1px solid var(--gray-200)">Name</th>' +
            '<th style="text-align:left;padding:8px;border-bottom:1px solid var(--gray-200)">URL</th>' +
            '<th style="text-align:center;padding:8px;border-bottom:1px solid var(--gray-200)">Enabled</th>' +
            '<th style="text-align:center;padding:8px;border-bottom:1px solid var(--gray-200)">Docs</th>' +
            '<th style="text-align:left;padding:8px;border-bottom:1px solid var(--gray-200)">Last Checked</th>' +
            '<th style="padding:8px;border-bottom:1px solid var(--gray-200)">Actions</th>' +
            '</tr></thead><tbody>';
        sources.forEach(s => {
            const tierBg = TIER_COLORS[s.tier] || '#555';
            const tierLbl = TIER_LABELS[s.tier] || 'T' + s.tier;
            const checked = s.last_checked ? s.last_checked.substring(0, 16).replace('T', ' ') : 'Never';
            const h = healthMap[s.id];
            let healthDot = '';
            if (h && h.total_fetches > 0) {
                const rate = h.success_rate;
                const color = rate >= 0.8 ? '#22c55e' : rate >= 0.5 ? '#f59e0b' : '#ef4444';
                const title = Math.round(rate * 100) + '% success (' + h.total_fetches + ' fetches)';
                healthDot = ' <span title="' + escHtml(title) + '" style="display:inline-block;width:8px;height:8px;border-radius:50%;background:' + color + '"></span>';
            }
            html += '<tr style="border-bottom:1px solid var(--gray-200)">' +
                '<td style="padding:8px"><span style="background:' + tierBg + ';color:#fff;padding:2px 8px;border-radius:10px;font-size:11px">' + escHtml(tierLbl) + '</span></td>' +
                '<td style="padding:8px">' + escHtml(s.name) + healthDot +
                (s.requires_js ? ' <span style="background:#f59e0b22;color:#f59e0b;padding:1px 4px;border-radius:3px;font-size:9px;font-weight:bold">JS</span>' : '') +
                (s.feed_url ? ' <span style="background:#22c55e22;color:#22c55e;padding:1px 4px;border-radius:3px;font-size:9px;font-weight:bold">RSS</span>' : '') +
                (s.stealth_level > 0 ? ' <span style="background:' + (STEALTH_LEVEL_COLORS[s.stealth_level] || '#888') + '22;color:' + (STEALTH_LEVEL_COLORS[s.stealth_level] || '#888') + ';padding:1px 4px;border-radius:3px;font-size:9px;font-weight:bold">S' + s.stealth_level + '</span>' : '') +
                (s.corridors && s.corridors.length ? '<br><span style="font-size:10px;color:var(--gray-500)">' + s.corridors.join(', ') + '</span>' : '') +
                '</td>' +
                '<td style="padding:8px;font-size:12px;max-width:250px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap"><a href="' + escHtml(s.url) + '" target="_blank" style="color:var(--primary)">' + escHtml(s.url) + '</a></td>' +
                '<td style="padding:8px;text-align:center"><label class="toggle"><input type="checkbox" ' + (s.enabled ? 'checked' : '') + ' onchange="toggleScraperSource(\'' + escHtml(s.id) + '\')"><span class="knob"></span></label></td>' +
                '<td style="padding:8px;text-align:center">' + s.doc_count + '</td>' +
                '<td style="padding:8px;font-size:12px;color:var(--gray-500)">' + escHtml(checked) + '</td>' +
                '<td style="padding:8px"><button class="btn" style="font-size:11px;padding:3px 8px" onclick="triggerScrape([\'' + escHtml(s.id) + '\'])">Scrape</button> ' +
                '<button class="btn" style="font-size:11px;padding:3px 8px;color:var(--danger)" onclick="deleteScraperSource(\'' + escHtml(s.id) + '\')">Del</button></td>' +
                '</tr>';
        });
        html += '</tbody></table>';
        document.getElementById('da-sources-table').innerHTML = html;
    } catch(e) {
        document.getElementById('da-sources-table').innerHTML = '<p style="color:var(--danger)">Failed to load sources: ' + escHtml(e.message) + '</p>';
    }
}

async function toggleScraperSource(id) {
    await apiCall('/scraper/sources/' + id + '/toggle', { method: 'PUT' });
    loadScraperSources();
}

function toggleAddSourceForm() {
    const f = document.getElementById('da-add-source-form');
    f.style.display = f.style.display === 'none' ? '' : 'none';
}

async function addScraperSource() {
    const body = {
        id: document.getElementById('da-new-id').value.trim(),
        name: document.getElementById('da-new-name').value.trim(),
        url: document.getElementById('da-new-url').value.trim(),
        tier: parseInt(document.getElementById('da-new-tier').value),
        selectors: document.getElementById('da-new-selectors').value.split(',').map(s=>s.trim()).filter(Boolean),
        description: document.getElementById('da-new-desc').value.trim(),
    };
    if (!body.id || !body.name || !body.url) { toast('ID, Name, and URL are required', 'error'); return; }
    try {
        const d = await apiCall('/scraper/sources', { method: 'POST', body: JSON.stringify(body) });
        toast('Source added');
        toggleAddSourceForm();
        loadScraperSources();
    } catch(e) {
        toast(e.message || 'Error adding source', 'error');
    }
}

async function deleteScraperSource(id) {
    if (!confirm('Delete source ' + id + '?')) return;
    await apiCall('/scraper/sources/' + id, { method: 'DELETE' });
    loadScraperSources();
}

async function triggerScrape(ids) {
    const body = {};
    if (ids && ids.length) body.source_ids = ids;
    const d = await apiCall('/scraper/run', { method: 'POST', body: JSON.stringify(body) });
    toast(d.message || 'Scrape started');
    setTimeout(() => { switchDocAgentTab('jobs'); loadScraperJobs(); }, 1000);
}

// -- Documents tab --

async function loadScraperDocs() {
    const sourceFilter = document.getElementById('da-doc-source-filter').value;
    let url = '/scraper/documents?limit=50&offset=' + (_daDocPage * 50);
    if (sourceFilter) url += '&source_id=' + sourceFilter;
    try {
        const d = await apiCall(url);
        const docs = d.documents || [];
        document.getElementById('da-doc-count').textContent = 'Total: ' + (d.total || 0);

        let html = '<table style="width:100%;border-collapse:collapse"><thead><tr>' +
            '<th style="text-align:left;padding:8px;border-bottom:1px solid var(--gray-200)">Title</th>' +
            '<th style="text-align:left;padding:8px;border-bottom:1px solid var(--gray-200)">Source</th>' +
            '<th style="text-align:center;padding:8px;border-bottom:1px solid var(--gray-200)">Type</th>' +
            '<th style="text-align:center;padding:8px;border-bottom:1px solid var(--gray-200)">Words</th>' +
            '<th style="text-align:left;padding:8px;border-bottom:1px solid var(--gray-200)">Fetched</th>' +
            '<th style="padding:8px;border-bottom:1px solid var(--gray-200)">Actions</th>' +
            '</tr></thead><tbody>';
        docs.forEach(doc => {
            const fetched = doc.fetched_at ? doc.fetched_at.substring(0, 16).replace('T', ' ') : '';
            html += '<tr style="border-bottom:1px solid var(--gray-200);cursor:pointer" onclick="viewScraperDoc(\'' + escHtml(doc.id) + '\')">' +
                '<td style="padding:8px;max-width:300px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">' + escHtml(doc.title) + '</td>' +
                '<td style="padding:8px;font-size:12px;color:var(--gray-500)">' + escHtml(doc.source_id) + '</td>' +
                '<td style="padding:8px;text-align:center"><span style="background:var(--gray-100);padding:2px 6px;border-radius:4px;font-size:11px">' + escHtml(doc.content_type) + '</span></td>' +
                '<td style="padding:8px;text-align:center">' + (doc.word_count || 0) + '</td>' +
                '<td style="padding:8px;font-size:12px;color:var(--gray-500)">' + escHtml(fetched) + '</td>' +
                '<td style="padding:8px"><button class="btn" style="font-size:11px;padding:3px 8px;color:var(--danger)" onclick="event.stopPropagation();deleteScraperDoc(\'' + escHtml(doc.id) + '\')">Del</button></td>' +
                '</tr>';
        });
        html += '</tbody></table>';
        document.getElementById('da-docs-table').innerHTML = html;
    } catch(e) {
        document.getElementById('da-docs-table').innerHTML = '<p style="color:var(--danger)">Failed to load documents</p>';
    }
}

async function viewScraperDoc(id) {
    try {
        const d = await apiCall('/scraper/documents/' + id);
        const doc = d.document;
        document.getElementById('da-doc-title').textContent = doc.title;
        document.getElementById('da-doc-meta').innerHTML =
            '<strong>Source:</strong> ' + escHtml(doc.source_id) + ' | <strong>Type:</strong> ' + escHtml(doc.content_type) +
            ' | <strong>Words:</strong> ' + doc.word_count + ' | <strong>Fetched:</strong> ' + escHtml(doc.fetched_at || '');
        document.getElementById('da-doc-text').textContent = doc.text || '';

        let factsHtml = '';
        if (doc.extraction && doc.extraction.facts && doc.extraction.facts.length) {
            factsHtml = '<h5>Extracted Facts (' + doc.extraction.facts.length + ') — Relevance: ' + (doc.extraction.relevance_score * 100).toFixed(0) + '%</h5>';
            factsHtml += '<div style="display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px">';
            doc.extraction.facts.forEach(f => {
                const bg = f.type === 'fee_cap' ? '#22c55e' : f.type === 'law' ? '#3b82f6' : f.type === 'case_study' ? '#ef4444' : f.type === 'statistic' ? '#f59e0b' : '#6366f1';
                const label = f.type + ': ' + (f.jurisdiction || f.corridor || f.metric || f.agency || '');
                factsHtml += '<span style="background:' + bg + '22;border:1px solid ' + bg + ';color:' + bg + ';padding:3px 8px;border-radius:12px;font-size:11px">' + escHtml(label) + '</span>';
            });
            factsHtml += '</div>';
            if (doc.extraction.summary) factsHtml += '<p style="color:var(--gray-500);font-size:13px">' + escHtml(doc.extraction.summary) + '</p>';
        } else {
            factsHtml = '<p style="color:var(--gray-500);font-size:13px">No facts extracted yet</p>';
        }
        document.getElementById('da-doc-facts').innerHTML = factsHtml;
        document.getElementById('da-doc-detail').style.display = '';
    } catch(e) {
        toast('Failed to load document', 'error');
    }
}

async function deleteScraperDoc(id) {
    if (!confirm('Delete document ' + id + '?')) return;
    await apiCall('/scraper/documents/' + id, { method: 'DELETE' });
    loadScraperDocs();
}

// -- Knowledge Base tab --

async function loadKBStats() {
    try {
        const d = await apiCall('/scraper/knowledge-base');
        const cats = d.by_category || {};
        let html = '';
        const catColors = {fee_cap:'#22c55e', law:'#3b82f6', bilateral_agreement:'#8b5cf6', case_study:'#ef4444', statistic:'#f59e0b', advisory:'#ec4899', regulation_change:'#14b8a6', contact:'#6366f1', court_ruling:'#0ea5e9', embassy_notice:'#a855f7', recruitment_violation:'#f43f5e', policy_update:'#06b6d4', training_material:'#84cc16', complaint:'#d946ef', penalty:'#fb923c'};
        html += '<div style="background:var(--gray-50);padding:14px;border-radius:8px;text-align:center;border:1px solid var(--gray-200)"><div style="font-size:24px;font-weight:bold;color:var(--gray-700)">' + (d.total_facts || 0) + '</div><div style="font-size:12px;color:var(--gray-500)">Total Facts</div></div>';
        html += '<div style="background:var(--gray-50);padding:14px;border-radius:8px;text-align:center;border:1px solid var(--gray-200)"><div style="font-size:24px;font-weight:bold;color:var(--gray-700)">' + (d.total_docs || 0) + '</div><div style="font-size:12px;color:var(--gray-500)">Documents</div></div>';
        html += '<div style="background:var(--gray-50);padding:14px;border-radius:8px;text-align:center;border:1px solid var(--gray-200)"><div style="font-size:24px;font-weight:bold;color:var(--gray-700)">' + ((d.avg_confidence || 0) * 100).toFixed(0) + '%</div><div style="font-size:12px;color:var(--gray-500)">Avg Confidence</div></div>';
        for (const [cat, count] of Object.entries(cats)) {
            const color = catColors[cat] || '#888';
            html += '<div style="background:var(--gray-50);padding:14px;border-radius:8px;text-align:center;border:1px solid var(--gray-200)"><div style="font-size:24px;font-weight:bold;color:' + color + '">' + count + '</div><div style="font-size:12px;color:var(--gray-500)">' + escHtml(cat.replace(/_/g, ' ')) + '</div></div>';
        }
        document.getElementById('da-kb-stats').innerHTML = html;
    } catch(e) {
        document.getElementById('da-kb-stats').innerHTML = '<p style="color:var(--danger)">Failed to load KB stats</p>';
    }
}

async function queryKB() {
    const category = document.getElementById('da-kb-category').value;
    const jurisdiction = document.getElementById('da-kb-jurisdiction').value.trim();
    const corridor = document.getElementById('da-kb-corridor').value.trim();
    let url = '/scraper/knowledge-base/query?limit=100';
    if (category) url += '&category=' + category;
    if (jurisdiction) url += '&jurisdiction=' + encodeURIComponent(jurisdiction);
    if (corridor) url += '&corridor=' + encodeURIComponent(corridor);
    try {
        const d = await apiCall(url);
        const facts = d.facts || [];
        let html = '<table style="width:100%;border-collapse:collapse"><thead><tr>' +
            '<th style="text-align:left;padding:8px;border-bottom:1px solid var(--gray-200)">Type</th>' +
            '<th style="text-align:left;padding:8px;border-bottom:1px solid var(--gray-200)">Jurisdiction / Corridor</th>' +
            '<th style="text-align:left;padding:8px;border-bottom:1px solid var(--gray-200)">Details</th>' +
            '<th style="text-align:center;padding:8px;border-bottom:1px solid var(--gray-200)">Conf</th>' +
            '<th style="text-align:left;padding:8px;border-bottom:1px solid var(--gray-200)">Source</th>' +
            '</tr></thead><tbody>';
        facts.forEach(f => {
            const type = f.type || 'unknown';
            const jur = f.jurisdiction || f.corridor || '';
            const details = f.summary || f.amount || f.description || f.name || f.title || f.metric || f.ruling || '';
            const src = f._source_doc || '';
            const conf = f._confidence != null ? (f._confidence * 100).toFixed(0) + '%' : '-';
            html += '<tr style="border-bottom:1px solid var(--gray-200)">' +
                '<td style="padding:8px"><span style="background:var(--gray-100);padding:2px 6px;border-radius:4px;font-size:11px">' + escHtml(type) + '</span></td>' +
                '<td style="padding:8px">' + escHtml(jur) + '</td>' +
                '<td style="padding:8px;max-width:400px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:13px">' + escHtml(details) + '</td>' +
                '<td style="padding:8px;text-align:center;font-size:11px">' + conf + '</td>' +
                '<td style="padding:8px;font-size:11px;color:var(--gray-500)">' + escHtml(src) + '</td>' +
                '</tr>';
        });
        html += '</tbody></table>';
        if (!facts.length) html = '<p style="color:var(--gray-500)">No facts found matching filters</p>';
        document.getElementById('da-kb-facts-table').innerHTML = html;
    } catch(e) {
        document.getElementById('da-kb-facts-table').innerHTML = '<p style="color:var(--danger)">Query failed</p>';
    }
}

async function rebuildKB() {
    toast('Rebuilding knowledge base...');
    const d = await apiCall('/scraper/knowledge-base/rebuild', { method: 'POST' });
    toast('KB rebuilt — ' + JSON.stringify(d.counts || {}));
    loadKBStats();
    queryKB();
}

function exportKB() {
    apiCall('/scraper/knowledge-base/query?limit=10000')
        .then(d => {
            const blob = new Blob([JSON.stringify(d.facts || [], null, 2)], {type:'application/json'});
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'knowledge_base_export.json';
            a.click();
        });
}

// -- Jobs tab --

async function loadScraperJobs() {
    try {
        const d = await apiCall('/scraper/jobs?limit=20');
        const jobs = d.jobs || [];

        const running = jobs.find(j => j.status === 'running');
        if (running) {
            document.getElementById('da-active-job').style.display = '';
            const pct = running.sources_total ? Math.round((running.sources_done / running.sources_total) * 100) : 0;
            document.getElementById('da-active-job-progress').style.width = pct + '%';
            document.getElementById('da-active-job-label').textContent =
                running.phase + ' — Sources: ' + running.sources_done + '/' + running.sources_total +
                ' | Docs found: ' + running.docs_found + ' | New: ' + running.docs_new +
                ' | Skipped: ' + (running.unchanged_skipped || 0) +
                ' | Robots: ' + (running.robots_blocked || 0) +
                ' | Facts: ' + running.facts_extracted;
            if (!_daJobPollTimer) _daJobPollTimer = setInterval(loadScraperJobs, 3000);
        } else {
            document.getElementById('da-active-job').style.display = 'none';
            if (_daJobPollTimer) { clearInterval(_daJobPollTimer); _daJobPollTimer = null; }
        }

        let html = '<table style="width:100%;border-collapse:collapse"><thead><tr>' +
            '<th style="text-align:left;padding:8px;border-bottom:1px solid var(--gray-200)">Job ID</th>' +
            '<th style="text-align:center;padding:8px;border-bottom:1px solid var(--gray-200)">Status</th>' +
            '<th style="text-align:center;padding:8px;border-bottom:1px solid var(--gray-200)">Sources</th>' +
            '<th style="text-align:center;padding:8px;border-bottom:1px solid var(--gray-200)">Docs Found</th>' +
            '<th style="text-align:center;padding:8px;border-bottom:1px solid var(--gray-200)">New</th>' +
            '<th style="text-align:center;padding:8px;border-bottom:1px solid var(--gray-200)">Facts</th>' +
            '<th style="text-align:left;padding:8px;border-bottom:1px solid var(--gray-200)">Started</th>' +
            '</tr></thead><tbody>';
        jobs.forEach(j => {
            const statusColor = j.status === 'completed' ? '#22c55e' : j.status === 'running' ? '#f59e0b' : '#ef4444';
            const started = j.started_at ? j.started_at.substring(0, 16).replace('T', ' ') : '';
            html += '<tr style="border-bottom:1px solid var(--gray-200)">' +
                '<td style="padding:8px;font-size:12px;font-family:monospace">' + escHtml(j.id) + '</td>' +
                '<td style="padding:8px;text-align:center"><span style="color:' + statusColor + '">' + escHtml(j.status) + '</span></td>' +
                '<td style="padding:8px;text-align:center">' + (j.sources_done || 0) + '/' + (j.sources_total || 0) + '</td>' +
                '<td style="padding:8px;text-align:center">' + (j.docs_found || 0) + '</td>' +
                '<td style="padding:8px;text-align:center">' + (j.docs_new || 0) + '</td>' +
                '<td style="padding:8px;text-align:center">' + (j.facts_extracted || 0) + '</td>' +
                '<td style="padding:8px;font-size:12px;color:var(--gray-500)">' + escHtml(started) + '</td>' +
                '</tr>';
        });
        html += '</tbody></table>';
        if (!jobs.length) html = '<p style="color:var(--gray-500)">No scrape jobs yet</p>';
        document.getElementById('da-jobs-table').innerHTML = html;
    } catch(e) {
        document.getElementById('da-jobs-table').innerHTML = '<p style="color:var(--danger)">Failed to load jobs</p>';
    }
}

// -- Stealth Settings tab --

const STEALTH_LEVEL_LABELS = {0:'None', 1:'Basic', 2:'Moderate', 3:'Full', 4:'Maximum'};
const STEALTH_LEVEL_COLORS = {0:'#6b7280', 1:'#22c55e', 2:'#f59e0b', 3:'#8b5cf6', 4:'#ef4444'};

async function loadStealthStatus() {
    try {
        const d = await apiCall('/scraper/stealth/status');
        const pkgs = d.packages || {};
        const container = document.getElementById('da-stealth-packages');
        let html = '';
        const labels = {
            fake_useragent: {name: 'fake-useragent', desc: 'UA rotation (Level 1+)', level: 1},
            curl_cffi: {name: 'curl_cffi', desc: 'TLS fingerprint spoofing (Level 2+)', level: 2},
            playwright_stealth: {name: 'playwright-stealth', desc: 'Browser anti-detection (Level 3+)', level: 3},
            nodriver: {name: 'nodriver', desc: 'CDP direct, best anti-detection (Level 4)', level: 4},
        };
        for (const [key, info] of Object.entries(labels)) {
            const installed = pkgs[key] === true;
            const icon = installed ? '&#10003;' : '&#10007;';
            const color = installed ? '#22c55e' : '#ef4444';
            const bg = installed ? '#22c55e11' : '#ef444411';
            html += '<div style="background:' + bg + ';padding:14px;border-radius:8px;border:1px solid ' + color + '33">' +
                '<div style="font-size:20px;color:' + color + '">' + icon + '</div>' +
                '<div style="font-weight:600;font-size:13px;color:var(--gray-700)">' + escHtml(info.name) + '</div>' +
                '<div style="font-size:11px;color:var(--gray-500)">' + escHtml(info.desc) + '</div>' +
                '</div>';
        }
        container.innerHTML = html;
    } catch(e) {
        document.getElementById('da-stealth-packages').innerHTML = '<p style="color:var(--danger)">Failed to load package status</p>';
    }
}

async function loadStealthConfig() {
    try {
        const d = await apiCall('/scraper/stealth/config');
        const cfg = d.config || {};
        document.getElementById('da-stealth-level').value = cfg.level || 0;
        document.getElementById('da-stealth-jitter-min').value = cfg.jitter_min != null ? cfg.jitter_min : 0.5;
        document.getElementById('da-stealth-jitter-max').value = cfg.jitter_max != null ? cfg.jitter_max : 2.5;
        document.getElementById('da-stealth-tls').value = cfg.tls_impersonate || 'chrome120';
        document.getElementById('da-stealth-viewport').checked = !!cfg.viewport_randomize;
        document.getElementById('da-stealth-locale').checked = !!cfg.locale_randomize;
        document.getElementById('da-stealth-cookies').checked = !!cfg.persist_cookies;
        document.getElementById('da-stealth-proxy-enabled').checked = !!cfg.proxy_enabled;
        document.getElementById('da-stealth-proxy-rotation').value = cfg.proxy_rotation || 'round_robin';
        document.getElementById('da-stealth-proxy-list').value = (cfg.proxy_list || []).join('\n');
    } catch(e) {
        toast('Failed to load stealth config', 'error');
    }
}

async function saveStealthConfig() {
    const proxyText = document.getElementById('da-stealth-proxy-list').value.trim();
    const body = {
        level: parseInt(document.getElementById('da-stealth-level').value),
        jitter_min: parseFloat(document.getElementById('da-stealth-jitter-min').value),
        jitter_max: parseFloat(document.getElementById('da-stealth-jitter-max').value),
        tls_impersonate: document.getElementById('da-stealth-tls').value,
        viewport_randomize: document.getElementById('da-stealth-viewport').checked,
        locale_randomize: document.getElementById('da-stealth-locale').checked,
        persist_cookies: document.getElementById('da-stealth-cookies').checked,
        proxy_enabled: document.getElementById('da-stealth-proxy-enabled').checked,
        proxy_rotation: document.getElementById('da-stealth-proxy-rotation').value,
        proxy_list: proxyText ? proxyText.split('\n').map(l => l.trim()).filter(Boolean) : [],
    };
    try {
        const d = await apiCall('/scraper/stealth/config', {method:'PUT', body:JSON.stringify(body)});
        toast('Stealth settings saved (Level ' + STEALTH_LEVEL_LABELS[d.config.level] + ')');
    } catch(e) {
        toast('Failed to save stealth config: ' + (e.message || ''), 'error');
    }
}


// =============================================================================
// Indicator Stacking Matrix
// =============================================================================

const IM_RISK_COLORS = {normal:'#22c55e', yellow_flag:'#f59e0b', red_flag:'#ef4444', critical:'#7c2d12'};
const IM_RISK_LABELS = {normal:'Normal', yellow_flag:'Yellow Flag', red_flag:'Red Flag', critical:'Critical'};
const ILO_SHORT = {
    abuse_of_vulnerability:'Vuln.', deception:'Decep.', restriction_of_movement:'Move.',
    isolation:'Isol.', physical_sexual_violence:'Viol.', intimidation_threats:'Threats',
    retention_of_documents:'Docs', withholding_wages:'Wages', debt_bondage:'Debt',
    abusive_conditions:'Cond.', excessive_overtime:'OT'
};
let _imActions = [];
let _imSelectedActions = new Set();

function switchIMSubTab(tab) {
    document.querySelectorAll('#da-tab-indicator-matrix .im-sub').forEach(s => s.style.display = 'none');
    document.getElementById('im-sub-' + tab).style.display = '';
    const btns = document.querySelectorAll('#da-tab-indicator-matrix .tab-bar .tab-btn');
    btns.forEach(b => b.classList.remove('active'));
    const names = ['grid','scoring','patterns','corridors','palermo'];
    const i = names.indexOf(tab);
    if (i >= 0 && btns[i]) btns[i].classList.add('active');
    if (tab === 'scoring') loadIMScorer();
    if (tab === 'patterns') loadIMPatterns();
    if (tab === 'corridors') loadIMCorridorComparison();
    if (tab === 'palermo') loadIMPalermo();
}

// -- Sectors / Corridors dropdowns --
async function loadIMSectors() {
    try {
        const d = await apiCall('/scraper/indicator-matrix/sectors');
        const opts = (d.sectors||[]).map(s => `<option value="${escHtml(s.sector)}">${escHtml(s.sector)} (${s.action_count})</option>`);
        const sel1 = document.getElementById('im-sector-filter');
        const sel2 = document.getElementById('im-pattern-sector');
        if (sel1) sel1.innerHTML = '<option value="">All Sectors</option>' + opts.join('');
        if (sel2) sel2.innerHTML = '<option value="">All Sectors</option>' + opts.join('');
    } catch(e) {}
}

async function loadIMCorridors() {
    try {
        const d = await apiCall('/scraper/indicator-matrix/corridors');
        const items = d.corridors || [];
        const opts = items.map(c => `<option value="${escHtml(c.corridor)}">${escHtml(c.corridor)} (${escHtml(c.origin_country)} → ${escHtml(c.destination_country)})</option>`);
        ['im-corridor-filter','im-corridor-select-1','im-corridor-select-2'].forEach(id => {
            const el = document.getElementById(id);
            if (el) {
                const prefix = id === 'im-corridor-filter' ? '<option value="">All Corridors</option>' : '';
                el.innerHTML = prefix + opts.join('');
            }
        });
        if (items.length >= 2) {
            const s2 = document.getElementById('im-corridor-select-2');
            if (s2) s2.selectedIndex = 1;
        }
    } catch(e) {}
}

// -- Phase × Indicator Grid --
async function loadIMGrid() {
    const sector = document.getElementById('im-sector-filter')?.value || '';
    const corridor = document.getElementById('im-corridor-filter')?.value || '';
    try {
        const d = await apiCall('/scraper/indicator-matrix');
        const params = new URLSearchParams();
        if (sector) params.set('sector', sector);
        if (corridor) params.set('corridor', corridor);
        const ad = await apiCall('/scraper/indicator-matrix/actions?' + params);
        const actions = ad.actions || [];

        // Build filtered matrix from actions
        const phases = d.phases || [];
        const indicators = d.indicators || [];
        const counts = {};
        phases.forEach(p => { counts[p] = {}; indicators.forEach(ind => { counts[p][ind] = 0; }); });
        actions.forEach(a => {
            const p = a.phase;
            (a.ilo_indicators || []).forEach(ind => {
                if (counts[p] && counts[p][ind] !== undefined) counts[p][ind]++;
            });
        });

        let html = '<table style="width:100%;border-collapse:collapse;font-size:12px">';
        html += '<thead><tr><th style="padding:6px;border:1px solid var(--gray-200);background:var(--gray-50);text-align:left">Phase</th>';
        indicators.forEach(ind => {
            html += `<th style="padding:6px;border:1px solid var(--gray-200);background:var(--gray-50);text-align:center;writing-mode:vertical-lr;min-width:40px" title="${escHtml(ind)}">${escHtml(ILO_SHORT[ind]||ind)}</th>`;
        });
        html += '<th style="padding:6px;border:1px solid var(--gray-200);background:var(--gray-50);text-align:center">Total</th></tr></thead><tbody>';

        phases.forEach(phase => {
            html += `<tr><td style="padding:6px;border:1px solid var(--gray-200);font-weight:600;white-space:nowrap">${escHtml(phase.replace(/_/g,' '))}</td>`;
            let rowTotal = 0;
            indicators.forEach(ind => {
                const c = counts[phase]?.[ind] || 0;
                rowTotal += c;
                const bg = c === 0 ? '#f8fafc' : c <= 2 ? '#fef3c7' : c <= 5 ? '#fed7aa' : '#fca5a5';
                html += `<td style="padding:4px;border:1px solid var(--gray-200);text-align:center;background:${bg};cursor:pointer" title="${escHtml(ind)}: ${c} actions" onclick="showIMCellActions('${phase}','${ind}')">${c||''}</td>`;
            });
            html += `<td style="padding:4px;border:1px solid var(--gray-200);text-align:center;font-weight:600">${rowTotal}</td></tr>`;
        });

        html += '</tbody></table>';
        html += `<p style="margin-top:12px;font-size:12px;color:var(--gray-500)">${actions.length} actions total. Click a cell to see details.</p>`;
        document.getElementById('im-grid-container').innerHTML = html;
    } catch(e) {
        document.getElementById('im-grid-container').innerHTML = '<p style="color:red">Failed to load indicator matrix: ' + escHtml(e.message||'') + '</p>';
    }
}

async function showIMCellActions(phase, indicator) {
    try {
        const d = await apiCall(`/scraper/indicator-matrix/actions?phase=${phase}&indicator=${indicator}`);
        const actions = d.actions || [];
        if (!actions.length) { toast('No actions in this cell'); return; }
        let html = `<h4>${escHtml(phase.replace(/_/g,' '))} × ${escHtml(indicator.replace(/_/g,' '))}</h4><ul style="margin-top:8px">`;
        actions.forEach(a => {
            const risk = a.prevalence === 'high' ? '#ef4444' : a.prevalence === 'medium' ? '#f59e0b' : '#22c55e';
            html += `<li style="margin-bottom:8px"><strong>${escHtml(a.id)}</strong>: ${escHtml(a.action)}<br>`;
            html += `<span style="font-size:11px;color:var(--gray-500)">Legal: ${escHtml(a.legal_justification||'')}</span><br>`;
            html += `<span style="font-size:11px;color:${risk}">Red flag: ${escHtml(a.red_flag_when||'')}</span></li>`;
        });
        html += '</ul>';
        document.getElementById('im-grid-container').innerHTML += `<div style="margin-top:16px;padding:16px;background:var(--gray-50);border-radius:8px;border:1px solid var(--gray-200)">${html}</div>`;
    } catch(e) {}
}

// -- Interactive Scorer --
async function loadIMScorer() {
    try {
        const d = await apiCall('/scraper/indicator-matrix/actions');
        _imActions = d.actions || [];
        const byPhase = {};
        _imActions.forEach(a => { (byPhase[a.phase] = byPhase[a.phase]||[]).push(a); });

        let html = '';
        Object.keys(byPhase).sort().forEach(phase => {
            html += `<div style="margin-bottom:16px"><h5 style="margin-bottom:6px;text-transform:capitalize">${escHtml(phase.replace(/_/g,' '))}</h5>`;
            byPhase[phase].forEach(a => {
                const checked = _imSelectedActions.has(a.id) ? 'checked' : '';
                html += `<label style="display:flex;align-items:flex-start;gap:6px;margin-bottom:4px;font-size:12px;cursor:pointer">`;
                html += `<input type="checkbox" ${checked} onchange="toggleIMAction('${a.id}')">`;
                html += `<span><strong>${escHtml(a.id)}</strong>: ${escHtml(a.action)}</span></label>`;
            });
            html += '</div>';
        });
        document.getElementById('im-phase-groups').innerHTML = html;
        renderIMScore();
    } catch(e) {}
}

function toggleIMAction(id) {
    if (_imSelectedActions.has(id)) _imSelectedActions.delete(id);
    else _imSelectedActions.add(id);
    renderIMScore();
}

async function renderIMScore() {
    const ids = Array.from(_imSelectedActions);
    if (!ids.length) {
        document.getElementById('im-risk-gauge').innerHTML = '<div style="padding:24px;text-align:center;color:var(--gray-400)">Select actions to see risk assessment</div>';
        document.getElementById('im-score-details').innerHTML = '';
        return;
    }
    try {
        const d = await apiCall('/scraper/indicator-matrix/score', {method:'POST', body:JSON.stringify({action_ids:ids})});
        const color = IM_RISK_COLORS[d.risk_level] || '#666';
        const label = IM_RISK_LABELS[d.risk_level] || d.risk_level;

        let gauge = `<div style="text-align:center;padding:20px;background:${color}15;border:2px solid ${color};border-radius:12px">`;
        gauge += `<div style="font-size:28px;font-weight:700;color:${color}">${escHtml(label)}</div>`;
        gauge += `<div style="font-size:13px;color:var(--gray-600);margin-top:4px">${d.indicator_count} indicator(s) across ${d.phase_count} phase(s)</div>`;
        gauge += `<div style="font-size:12px;color:var(--gray-500);margin-top:8px">${escHtml(d.risk_explanation||'')}</div>`;
        gauge += '</div>';
        document.getElementById('im-risk-gauge').innerHTML = gauge;

        let det = '';
        // Indicators
        if (d.matched_indicators?.length) {
            det += '<h5 style="margin-top:12px">ILO Indicators Triggered</h5><div style="display:flex;flex-wrap:wrap;gap:4px;margin-top:4px">';
            d.matched_indicators.forEach(ind => { det += `<span style="padding:2px 8px;background:#ef444420;color:#ef4444;border-radius:12px;font-size:11px">${escHtml(ind.replace(/_/g,' '))}</span>`; });
            det += '</div>';
        }
        // Palermo
        det += '<h5 style="margin-top:12px">Palermo Protocol Coverage</h5>';
        const pc = d.palermo_coverage || {};
        ['act','means','purpose'].forEach(elem => {
            const items = pc[elem] || [];
            const check = items.length ? '&#10003;' : '&#10007;';
            const col = items.length ? '#22c55e' : '#ef4444';
            det += `<div style="font-size:12px;margin-top:2px"><span style="color:${col}">${check}</span> <strong>${elem.toUpperCase()}</strong>: ${items.length ? escHtml(items.join(', ')) : 'none'}</div>`;
        });
        if (d.palermo_complete) det += '<div style="margin-top:4px;font-size:12px;color:#7c2d12;font-weight:600">All 3 Palermo elements satisfied — meets trafficking definition</div>';
        // Matched patterns
        if (d.pattern_match_scores?.length) {
            det += '<h5 style="margin-top:12px">Matched Patterns</h5>';
            d.pattern_match_scores.slice(0, 5).forEach(ps => {
                const rc = IM_RISK_COLORS[ps.risk_level] || '#666';
                det += `<div style="font-size:12px;margin-top:4px;padding:6px;background:var(--gray-50);border-radius:4px">`;
                det += `<span style="color:${rc};font-weight:600">${escHtml(ps.pattern_name)}</span> — ${ps.overlap_pct}% match</div>`;
            });
        }
        // Legal refs
        if (d.legal_references?.length) {
            det += '<h5 style="margin-top:12px">Legal References</h5><ul style="font-size:11px;margin-top:4px">';
            d.legal_references.forEach(r => { det += `<li>${escHtml(r)}</li>`; });
            det += '</ul>';
        }
        document.getElementById('im-score-details').innerHTML = det;
    } catch(e) {
        document.getElementById('im-risk-gauge').innerHTML = '<p style="color:red">Scoring failed</p>';
    }
}

// -- Known Patterns --
async function loadIMPatterns() {
    const risk = document.getElementById('im-pattern-risk')?.value || 'yellow_flag';
    const sector = document.getElementById('im-pattern-sector')?.value || '';
    const params = new URLSearchParams({min_risk: risk});
    if (sector) params.set('sector', sector);
    try {
        const d = await apiCall('/scraper/indicator-matrix/combinations?' + params);
        const combos = d.combinations || [];
        if (!combos.length) {
            document.getElementById('im-patterns-list').innerHTML = '<p style="color:var(--gray-400)">No patterns at this risk level.</p>';
            return;
        }
        let html = '<div style="display:grid;gap:12px">';
        combos.forEach(p => {
            const rc = IM_RISK_COLORS[p.risk_level] || '#666';
            html += `<div style="padding:12px;border:1px solid var(--gray-200);border-radius:8px;border-left:4px solid ${rc}">`;
            html += `<div style="display:flex;justify-content:space-between;align-items:center">`;
            html += `<strong>${escHtml(p.name||p.id)}</strong>`;
            html += `<span style="padding:2px 8px;background:${rc}20;color:${rc};border-radius:12px;font-size:11px;font-weight:600">${escHtml(IM_RISK_LABELS[p.risk_level]||p.risk_level)}</span></div>`;
            html += `<p style="font-size:12px;color:var(--gray-600);margin-top:6px">${escHtml(p.description||'')}</p>`;
            if (p.ilo_indicators?.length) {
                html += '<div style="display:flex;flex-wrap:wrap;gap:3px;margin-top:6px">';
                p.ilo_indicators.forEach(ind => { html += `<span style="padding:1px 6px;background:#3b82f620;color:#3b82f6;border-radius:8px;font-size:10px">${escHtml(ind.replace(/_/g,' '))}</span>`; });
                html += '</div>';
            }
            if (p.corridors?.length) {
                html += `<div style="font-size:11px;color:var(--gray-500);margin-top:4px">Corridors: ${escHtml(p.corridors.join(', '))}</div>`;
            }
            if (p.sectors?.length) {
                html += `<div style="font-size:11px;color:var(--gray-500);margin-top:2px">Sectors: ${escHtml(p.sectors.join(', '))}</div>`;
            }
            html += '</div>';
        });
        html += '</div>';
        document.getElementById('im-patterns-list').innerHTML = html;
    } catch(e) {
        document.getElementById('im-patterns-list').innerHTML = '<p style="color:red">Failed to load patterns</p>';
    }
}

// -- Corridor Comparison --
async function loadIMCorridorComparison() {
    const c1 = document.getElementById('im-corridor-select-1')?.value;
    const c2 = document.getElementById('im-corridor-select-2')?.value;
    if (!c1) return;
    try {
        const [d1, d2] = await Promise.all([
            apiCall(`/scraper/indicator-matrix/corridor/${c1}`),
            c2 && c2 !== c1 ? apiCall(`/scraper/indicator-matrix/corridor/${c2}`) : null,
        ]);
        const p1 = d1.profile;
        const p2 = d2?.profile;

        let html = '<div style="display:grid;grid-template-columns:1fr' + (p2 ? ' 1fr' : '') + ';gap:20px">';

        [p1, p2].filter(Boolean).forEach(p => {
            html += `<div style="padding:16px;border:1px solid var(--gray-200);border-radius:8px">`;
            html += `<h4>${escHtml(p.corridor)} — ${escHtml(p.origin_country)} → ${escHtml(p.destination_country)}</h4>`;
            html += `<div style="font-size:12px;color:var(--gray-500);margin-top:4px">Sectors: ${escHtml((p.primary_sectors||[]).join(', '))}${p.kafala_system ? ' | <strong>Kafala</strong>' : ''}</div>`;

            // Indicator bars
            html += '<h5 style="margin-top:12px">Indicator Prevalence</h5>';
            const prev = p.indicator_prevalence || {};
            Object.entries(prev).sort((a,b) => b[1]-a[1]).forEach(([ind, val]) => {
                const pct = Math.round(val * 100);
                const color = pct >= 70 ? '#ef4444' : pct >= 40 ? '#f59e0b' : '#22c55e';
                html += `<div style="display:flex;align-items:center;gap:6px;margin-top:3px;font-size:11px">`;
                html += `<span style="width:100px;text-align:right">${escHtml(ind.replace(/_/g,' '))}</span>`;
                html += `<div style="flex:1;height:14px;background:var(--gray-100);border-radius:4px;overflow:hidden">`;
                html += `<div style="width:${pct}%;height:100%;background:${color};border-radius:4px"></div></div>`;
                html += `<span style="width:30px">${pct}%</span></div>`;
            });

            // Phase risk
            html += '<h5 style="margin-top:12px">Phase Risk Profile</h5>';
            const phases = p.phase_risk_profile || {};
            Object.entries(phases).forEach(([phase, val]) => {
                const pct = Math.round(val * 100);
                const color = pct >= 70 ? '#ef4444' : pct >= 40 ? '#f59e0b' : '#22c55e';
                html += `<div style="display:flex;align-items:center;gap:6px;margin-top:3px;font-size:11px">`;
                html += `<span style="width:100px;text-align:right">${escHtml(phase.replace(/_/g,' '))}</span>`;
                html += `<div style="flex:1;height:14px;background:var(--gray-100);border-radius:4px;overflow:hidden">`;
                html += `<div style="width:${pct}%;height:100%;background:${color};border-radius:4px"></div></div>`;
                html += `<span style="width:30px">${pct}%</span></div>`;
            });

            if (p.summary) html += `<p style="font-size:12px;color:var(--gray-600);margin-top:12px">${escHtml(p.summary)}</p>`;
            html += '</div>';
        });

        html += '</div>';
        document.getElementById('im-corridor-comparison').innerHTML = html;
    } catch(e) {
        document.getElementById('im-corridor-comparison').innerHTML = '<p style="color:red">Failed to load corridor profiles</p>';
    }
}

// -- Palermo Mapping --
async function loadIMPalermo() {
    try {
        const d = await apiCall('/scraper/indicator-matrix/palermo-mapping');
        const mapping = d.mapping || {};
        const elemColors = {act:'#3b82f6', means:'#f59e0b', purpose:'#ef4444'};

        let html = '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px">';
        ['act','means','purpose'].forEach(elem => {
            const color = elemColors[elem];
            const subtypes = mapping[elem] || {};
            html += `<div style="padding:16px;border:2px solid ${color};border-radius:8px">`;
            html += `<h4 style="color:${color};text-align:center;margin-bottom:12px">${elem.toUpperCase()}</h4>`;
            Object.entries(subtypes).sort((a,b) => b[1].length - a[1].length).forEach(([subtype, ids]) => {
                html += `<div style="margin-bottom:8px">`;
                html += `<div style="font-size:12px;font-weight:600">${escHtml(subtype.replace(/_/g,' '))} <span style="color:var(--gray-400)">(${ids.length})</span></div>`;
                html += `<div style="font-size:10px;color:var(--gray-500);margin-top:2px">${escHtml(ids.slice(0,8).join(', '))}${ids.length > 8 ? '...' : ''}</div>`;
                html += '</div>';
            });
            html += '</div>';
        });
        html += '</div>';
        document.getElementById('im-palermo-diagram').innerHTML = html;
    } catch(e) {
        document.getElementById('im-palermo-diagram').innerHTML = '<p style="color:red">Failed to load Palermo mapping</p>';
    }
}
