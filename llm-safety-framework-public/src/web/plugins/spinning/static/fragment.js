// =============================================================================
// Transform Workbench Plugin
// =============================================================================

SECTION_LOADERS['transform'] = loadTransformWorkbench;

// =============================================================================
// Transform Workbench Tab Navigation
// =============================================================================

function showTransformTab(tabId) {
    const bar = document.getElementById('transform-tab-bar');
    const tabs = document.getElementById('transform-tabs');
    if (!bar || !tabs) return;
    tabs.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    bar.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    const panel = document.getElementById(tabId);
    if (panel) panel.classList.add('active');
    // Highlight the correct tab button
    const tabNames = { 'tab-tw-spintax': 0, 'tab-tw-regex': 1, 'tab-tw-charpad': 2, 'tab-tw-llm': 3, 'tab-tw-attack': 4, 'tab-tw-custom': 5, 'tab-tw-encode': 6, 'tab-tw-obfuscate': 7, 'tab-tw-jailbreak': 8, 'tab-tw-multilingual': 9, 'tab-tw-chains': 10, 'tab-tw-pipeline': 11 };
    const idx = tabNames[tabId];
    if (idx !== undefined) {
        const btns = bar.querySelectorAll('.tab-btn');
        if (btns[idx]) btns[idx].classList.add('active');
    }
    // Load data for specific tabs
    if (tabId === 'tab-tw-llm') loadSpinningModels();
    if (tabId === 'tab-tw-attack') loadAttackStrategies();
    if (tabId === 'tab-tw-pipeline') loadPipeline();
    if (tabId === 'tab-tw-jailbreak') loadJailbreakTemplates();
    if (tabId === 'tab-tw-multilingual') loadMultilingualTab();
    if (tabId === 'tab-tw-chains') loadChainTab();
    // Render prompt source selectors for applicable tabs
    const tabTextareas = {
        'tab-tw-regex': 'regex-prompts', 'tab-tw-charpad': 'charpad-prompts',
        'tab-tw-llm': 'llm-rephrase-prompts', 'tab-tw-attack': 'attack-aug-prompts',
        'tab-tw-custom': 'custom-aug-prompts',
        'tab-tw-encode': 'encode-prompts', 'tab-tw-obfuscate': 'obfuscate-prompts',
        'tab-tw-jailbreak': 'jailbreak-prompts', 'tab-tw-multilingual': 'multilingual-prompts',
    };
    if (tabTextareas[tabId]) renderPromptSource(tabId, tabTextareas[tabId]);
    // Receive any transferred prompts
    if (_transferPrompts && tabTextareas[tabId]) _receiveTransferPrompts(tabTextareas[tabId]);
}

function loadTransformWorkbench() {
    loadSpinningModels();
    loadAttackStrategies();
    loadPipeline();
}

// =============================================================================
// Preview Panel
// =============================================================================

let _previewData = [];
function updatePreview(prompts, label, originals) {
    _previewData = prompts || [];
    const container = document.getElementById('preview-content');
    const copyBtn = document.getElementById('preview-copy-btn');
    if (!prompts || prompts.length === 0) {
        container.innerHTML = '<div style="padding:16px;text-align:center;color:var(--gray-400)">No results yet</div>';
        if (copyBtn) copyBtn.style.display = 'none';
        return;
    }
    if (copyBtn) copyBtn.style.display = '';
    let html = `<div class="preview-stat"><span class="preview-stat-val">${prompts.length}</span><span class="preview-stat-label">${label || 'prompts generated'}</span></div>`;
    const showCount = Math.min(prompts.length, 30);
    for (let i = 0; i < showCount; i++) {
        const p = typeof prompts[i] === 'string' ? prompts[i] : JSON.stringify(prompts[i]);
        const orig = originals && originals[i] ? originals[i] : null;
        html += `<div class="preview-item">`;
        if (orig) html += `<div class="preview-original">${escHtml(orig)}</div>`;
        html += `${escHtml(p)}</div>`;
    }
    if (prompts.length > showCount) {
        html += `<div style="padding:8px 16px;color:var(--gray-400);font-size:11px;text-align:center">... and ${prompts.length - showCount} more</div>`;
    }
    container.innerHTML = html;
}
function copyPreviewResults() {
    const text = _previewData.map(p => typeof p === 'string' ? p : JSON.stringify(p)).join('\n');
    navigator.clipboard.writeText(text).then(() => toast('Copied to clipboard'));
}

// =============================================================================
// Workflow helpers: export, send-to, prompt source
// =============================================================================

let _transferPrompts = null;

function renderStepExport(containerId, prompts, label) {
    const container = document.getElementById(containerId);
    if (!container || !prompts || !prompts.length) return;
    const existing = container.querySelector('.step-actions');
    if (existing) existing.remove();
    const bar = document.createElement('div');
    bar.className = 'step-actions';
    const normalized = prompts.map(p => typeof p === 'string' ? p : JSON.stringify(p));
    // Export buttons
    const btnJson = document.createElement('button');
    btnJson.className = 'btn';
    btnJson.textContent = '\u2B73 JSON';
    btnJson.onclick = () => {
        const blob = new Blob([JSON.stringify({ label: label || 'prompts', prompts: normalized }, null, 2)], { type: 'application/json' });
        const a = document.createElement('a'); a.href = URL.createObjectURL(blob);
        a.download = (label || 'prompts').replace(/\s+/g, '_') + '.json'; a.click();
    };
    const btnCsv = document.createElement('button');
    btnCsv.className = 'btn';
    btnCsv.textContent = '\u2B73 CSV';
    btnCsv.onclick = () => {
        const csv = 'prompt\n' + normalized.map(p => '"' + p.replace(/"/g, '""') + '"').join('\n');
        const blob = new Blob([csv], { type: 'text/csv' });
        const a = document.createElement('a'); a.href = URL.createObjectURL(blob);
        a.download = (label || 'prompts').replace(/\s+/g, '_') + '.csv'; a.click();
    };
    const btnCopy = document.createElement('button');
    btnCopy.className = 'btn';
    btnCopy.textContent = '\u2398 Copy';
    btnCopy.onclick = () => navigator.clipboard.writeText(normalized.join('\n')).then(() => toast('Copied ' + normalized.length + ' prompts'));
    bar.append(btnJson, btnCsv, btnCopy);
    // Send-to buttons
    const sep = document.createElement('div'); sep.className = 'step-sep'; bar.appendChild(sep);
    const targets = [
        { label: 'Send to Regex', tab: 'tab-tw-regex', textarea: 'regex-prompts' },
        { label: 'Send to LLM Rephrase', tab: 'tab-tw-llm', textarea: 'llm-rephrase-prompts' },
        { label: 'Send to Attack Augment', tab: 'tab-tw-attack', textarea: 'attack-aug-prompts' },
        { label: 'Send to Encode', tab: 'tab-tw-encode', textarea: 'encode-prompts' },
        { label: 'Send to Obfuscate', tab: 'tab-tw-obfuscate', textarea: 'obfuscate-prompts' },
        { label: 'Send to Jailbreak', tab: 'tab-tw-jailbreak', textarea: 'jailbreak-prompts' },
        { label: 'Send to Chains', tab: 'tab-tw-chains', textarea: 'chain-prompts' },
    ];
    for (const t of targets) {
        const btn = document.createElement('button');
        btn.className = 'btn btn-primary';
        btn.textContent = '\u27A4 ' + t.label;
        btn.onclick = () => sendPromptsTo(t.tab, t.textarea, normalized);
        bar.appendChild(btn);
    }
    container.appendChild(bar);
}

function sendPromptsTo(tabId, textareaId, prompts) {
    _transferPrompts = { tabId, textareaId, prompts };
    showSection('transform');
    setTimeout(() => {
        showTransformTab(tabId);
        _receiveTransferPrompts(textareaId);
    }, 100);
}

function _receiveTransferPrompts(textareaId) {
    if (!_transferPrompts) return;
    const ta = document.getElementById(textareaId || _transferPrompts.textareaId);
    if (ta && _transferPrompts.prompts) {
        ta.value = _transferPrompts.prompts.join('\n');
        toast('Loaded ' + _transferPrompts.prompts.length + ' prompts');
    }
    _transferPrompts = null;
}

// =============================================================================
// Prompt Source Selector (Paste / Upload / Pull)
// =============================================================================

function renderPromptSource(containerId, textareaId) {
    const container = document.getElementById(containerId);
    if (!container || container.querySelector('.prompt-source-bar')) return;
    const uid = 'ps-' + textareaId;
    const bar = document.createElement('div');
    bar.innerHTML = `<div class="prompt-source-bar">
        <button class="prompt-source-btn active" onclick="switchPromptSource('${uid}','paste',this)">Paste</button>
        <button class="prompt-source-btn" onclick="switchPromptSource('${uid}','upload',this)">Upload</button>
        <button class="prompt-source-btn" onclick="switchPromptSource('${uid}','pull',this)">Pull</button>
    </div>
    <div class="prompt-source-upload" id="${uid}-upload">
        <input type="file" accept=".json,.txt,.csv" onchange="loadPromptFile(this,'${textareaId}')">
        <div style="font-size:11px;color:var(--gray-400);margin-top:4px">Accepts JSON (array or {prompts:[]}), TXT (one per line), CSV</div>
    </div>
    <div class="prompt-source-pull" id="${uid}-pull">
        <select id="${uid}-pull-source"><option value="">Loading sources...</option></select>
        <button class="btn btn-primary" onclick="loadFromPullSource('${uid}-pull-source','${textareaId}')">Load</button>
    </div>`;
    const textarea = document.getElementById(textareaId);
    if (textarea) textarea.parentNode.insertBefore(bar, textarea);
    else container.prepend(bar);
    // Load pull sources asynchronously
    loadPullSources(uid + '-pull-source');
}

function switchPromptSource(uid, mode, btn) {
    const bar = btn.parentElement;
    bar.querySelectorAll('.prompt-source-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const upload = document.getElementById(uid + '-upload');
    const pull = document.getElementById(uid + '-pull');
    if (upload) upload.classList.toggle('active', mode === 'upload');
    if (pull) pull.classList.toggle('active', mode === 'pull');
}

function loadPromptFile(input, textareaId) {
    const file = input.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (e) => {
        const text = e.target.result;
        let prompts = [];
        if (file.name.endsWith('.json')) {
            try {
                const parsed = JSON.parse(text);
                if (Array.isArray(parsed)) prompts = parsed.map(p => typeof p === 'string' ? p : (p.text || p.prompt || JSON.stringify(p)));
                else if (parsed.prompts) prompts = parsed.prompts.map(p => typeof p === 'string' ? p : (p.text || p.prompt || JSON.stringify(p)));
                else prompts = [JSON.stringify(parsed)];
            } catch (err) { toast('Invalid JSON', 'error'); return; }
        } else {
            prompts = text.split('\n').map(l => l.trim()).filter(Boolean);
        }
        const ta = document.getElementById(textareaId);
        if (ta) { ta.value = prompts.join('\n'); toast('Loaded ' + prompts.length + ' prompts from file'); }
    };
    reader.readAsText(file);
}

async function loadPullSources(selectId) {
    const sel = document.getElementById(selectId);
    if (!sel) return;
    let html = '<option value="">-- Select source --</option>';
    try {
        const pipeline = await apiCall('/spinning/pipeline', { silent: true });
        if (pipeline.pipeline && pipeline.pipeline.total > 0) {
            html += `<option value="pipeline">Active Pipeline (${pipeline.pipeline.total} prompts)</option>`;
        }
    } catch (e) {}
    try {
        const jobs = await apiCall('/spinning/jobs', { silent: true });
        for (const j of (jobs.jobs || [])) {
            html += `<option value="job:${j.id}">${escHtml(j.type || 'spin')} - ${j.count || '?'} prompts (${j.id.slice(0,8)})</option>`;
        }
    } catch (e) {}
    try {
        const sets = await apiCall('/prompts/sets', { silent: true });
        for (const s of (sets.sets || [])) {
            html += `<option value="set:${s.id}">${escHtml(s.name)} (${s.count} prompts)</option>`;
        }
    } catch (e) {}
    sel.innerHTML = html;
}

async function loadFromPullSource(selectId, textareaId) {
    const sel = document.getElementById(selectId);
    const val = sel ? sel.value : '';
    if (!val) return toast('Select a source', 'error');
    let prompts = [];
    if (val === 'pipeline') {
        const data = await apiCall('/spinning/pipeline');
        prompts = ((data.pipeline || {}).prompts || []).map(p => p.text || p.prompt || (typeof p === 'string' ? p : JSON.stringify(p)));
    } else if (val.startsWith('job:')) {
        const jobId = val.slice(4);
        const data = await apiCall('/spinning/jobs/' + jobId);
        prompts = (data.prompts || data.job?.prompts || []).map(p => typeof p === 'string' ? p : (p.text || JSON.stringify(p)));
    } else if (val.startsWith('set:')) {
        const setId = val.slice(4);
        const data = await apiCall('/prompts/sets/' + setId);
        prompts = (data.prompts || []).map(p => p.text || p.prompt || (typeof p === 'string' ? p : JSON.stringify(p)));
    }
    if (!prompts.length) return toast('No prompts found in source', 'error');
    const ta = document.getElementById(textareaId);
    if (ta) { ta.value = prompts.join('\n'); toast('Loaded ' + prompts.length + ' prompts'); }
}

// =============================================================================
// Spinning: Spintax
// =============================================================================

async function expandSpintax() {
    const template = document.getElementById('spintax-template').value;
    if (!template) return toast('Enter a template', 'error');
    const count = parseInt(document.getElementById('spintax-count').value) || 10;
    const save = document.getElementById('spintax-save').checked;
    const data = await apiCall('/spinning/spintax', {
        method: 'POST',
        body: JSON.stringify({ template, count, save_to_pipeline: save }),
    });
    const spintaxPrompts = data.prompts || [];
    document.getElementById('spintax-results').innerHTML = `<div class="tag tag-safe">${data.count} prompts generated${save ? ' & saved' : ''}</div>`;
    updatePreview(spintaxPrompts, 'spintax expansions');
    renderStepExport('spintax-results', spintaxPrompts, 'spintax_expansions');
}

// =============================================================================
// Spinning: Regex
// =============================================================================

function addRegexRow() {
    const container = document.getElementById('regex-patterns');
    const row = document.createElement('div');
    row.className = 'form-row';
    row.style.marginBottom = '8px';
    row.innerHTML = '<div class="form-group"><input type="text" class="regex-find" placeholder="find"></div><div class="form-group"><input type="text" class="regex-replace" placeholder="replace"></div>';
    container.appendChild(row);
}

async function runRegexSpin() {
    const prompts = document.getElementById('regex-prompts').value.split('\n').filter(Boolean);
    if (!prompts.length) return toast('Enter prompts', 'error');
    const finds = document.querySelectorAll('.regex-find');
    const replaces = document.querySelectorAll('.regex-replace');
    const patterns = [];
    for (let i = 0; i < finds.length; i++) {
        if (finds[i].value) patterns.push({ find: finds[i].value, replace: replaces[i].value });
    }
    const data = await apiCall('/spinning/regex', {
        method: 'POST',
        body: JSON.stringify({ prompts, patterns, save_to_pipeline: true }),
    });
    showSpinResults('regex-results', data);
}

// =============================================================================
// Spinning: Char Padding
// =============================================================================

async function runCharPad() {
    const prompts = document.getElementById('charpad-prompts').value.split('\n').filter(Boolean);
    if (!prompts.length) return toast('Enter prompts', 'error');
    const data = await apiCall('/spinning/char-padding', {
        method: 'POST',
        body: JSON.stringify({
            prompts,
            padding_chars: document.getElementById('charpad-char').value,
            padding_count: parseInt(document.getElementById('charpad-count').value) || 0,
            trailing_chars: document.getElementById('charpad-trailing').value,
            insert_zero_width: document.getElementById('charpad-zw').checked,
            save_to_pipeline: true,
        }),
    });
    showSpinResults('charpad-results', data);
}

function showSpinResults(containerId, data) {
    const prompts = data.prompts || [];
    const normalized = prompts.map(p => typeof p === 'string' ? p : JSON.stringify(p));
    document.getElementById(containerId).innerHTML = `<div class="tag tag-safe">${prompts.length} prompts${data.saved ? ' saved to pipeline' : ''}</div>`;
    updatePreview(normalized, 'transformed prompts');
    renderStepExport(containerId, normalized, containerId.replace('-results', ''));
}

// =============================================================================
// Spinning: LLM Rephrase
// =============================================================================

async function loadSpinningModels() {
    try {
        const data = await apiCall('/endpoints/all/enabled', { silent: true });
        const models = data.models || [];
        const selects = ['llm-rephrase-model', 'test-model-select'];
        for (const selId of selects) {
            const sel = document.getElementById(selId);
            if (!sel) continue;
            sel.innerHTML = models.length
                ? models.map(m => `<option value="${m.id}">${escHtml(m.name)} (${m.endpoint_name})</option>`).join('')
                : '<option value="">No enabled models</option>';
        }
    } catch (e) {}
}

async function runLLMRephrase() {
    const prompts = document.getElementById('llm-rephrase-prompts').value.split('\n').filter(Boolean);
    if (!prompts.length) return toast('Enter prompts', 'error');
    const modelId = document.getElementById('llm-rephrase-model').value;
    if (!modelId) return toast('Select a model', 'error');
    toast('Rephrasing...');
    const data = await apiCall('/spinning/llm-rephrase', {
        method: 'POST',
        body: JSON.stringify({
            prompts,
            model_id: modelId,
            rephrase_instructions: document.getElementById('llm-rephrase-instructions').value,
            count_per_prompt: parseInt(document.getElementById('llm-rephrase-count').value) || 3,
            temperature: parseFloat(document.getElementById('llm-rephrase-temp').value) || 0.9,
            save_to_pipeline: true,
        }),
    });
    document.getElementById('llm-rephrase-results').innerHTML = `<div class="tag tag-safe">${data.count} variations generated</div>`;
    const allVariations = [];
    const allOriginals = [];
    for (const r of (data.results || [])) {
        for (const v of r.variations) {
            allVariations.push(v);
            allOriginals.push(r.original);
        }
    }
    updatePreview(allVariations, 'LLM variations', allOriginals);
    renderStepExport('llm-rephrase-results', allVariations, 'llm_rephrase');
}

// =============================================================================
// Spinning: Attack Augment
// =============================================================================

async function loadAttackStrategies() {
    try {
        const data = await apiCall('/analytics/attack-strategies', { silent: true });
        const container = document.getElementById('attack-strategy-checkboxes');
        if (!data.strategies || data.strategies.length === 0) {
            container.innerHTML = '<div style="color:var(--gray-400)">No strategies available</div>';
            return;
        }
        let html = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:4px">';
        for (const s of data.strategies) {
            html += `<label style="font-size:12px;display:flex;align-items:center;gap:6px">
                <input type="checkbox" class="attack-strat-cb" value="${s.id}"> ${escHtml(s.name)}
            </label>`;
        }
        html += '</div>';
        container.innerHTML = html;
    } catch (e) {
        document.getElementById('attack-strategy-checkboxes').innerHTML = '<div style="color:var(--gray-400)">Could not load strategies</div>';
    }
}

async function runAttackAugment() {
    const prompts = document.getElementById('attack-aug-prompts').value.split('\n').filter(Boolean);
    if (!prompts.length) return toast('Enter prompts', 'error');
    const strategies = [...document.querySelectorAll('.attack-strat-cb:checked')].map(cb => cb.value);
    if (!strategies.length) return toast('Select at least one strategy', 'error');
    const data = await apiCall('/spinning/attack-augment', {
        method: 'POST',
        body: JSON.stringify({ prompts, strategies, save_to_pipeline: true }),
    });
    document.getElementById('attack-aug-results').innerHTML = `<div class="tag tag-safe">${data.count} augmented prompts saved</div>`;
    const mutated = (data.results || []).map(r => r.mutated);
    const originals = (data.results || []).map(r => r.original);
    updatePreview(mutated, 'attack-augmented prompts', originals);
    renderStepExport('attack-aug-results', mutated, 'attack_augmented');
}

// =============================================================================
// Spinning: Custom Augment
// =============================================================================

function addCustomRow() {
    const container = document.getElementById('custom-find-replace');
    const row = document.createElement('div');
    row.className = 'form-row';
    row.style.marginBottom = '8px';
    row.innerHTML = '<div class="form-group"><input type="text" class="custom-find" placeholder="find"></div><div class="form-group"><input type="text" class="custom-replace" placeholder="replace"></div>';
    container.appendChild(row);
}

async function runCustomAugment() {
    const prompts = document.getElementById('custom-aug-prompts').value.split('\n').filter(Boolean);
    if (!prompts.length) return toast('Enter prompts', 'error');
    const finds = document.querySelectorAll('.custom-find');
    const replaces = document.querySelectorAll('.custom-replace');
    const findReplace = [];
    for (let i = 0; i < finds.length; i++) {
        if (finds[i].value) findReplace.push({ find: finds[i].value, replace: replaces[i].value });
    }
    const data = await apiCall('/spinning/custom-augment', {
        method: 'POST',
        body: JSON.stringify({
            prompts,
            prefix: document.getElementById('custom-aug-prefix').value,
            suffix: document.getElementById('custom-aug-suffix').value,
            find_replace: findReplace,
            save_to_pipeline: true,
        }),
    });
    showSpinResults('custom-aug-results', data);
}

// =============================================================================
// Spinning: Encode
// =============================================================================

document.addEventListener('change', function(e) {
    if (e.target.name === 'encode-type') {
        const v = e.target.value;
        const co = document.getElementById('encode-caesar-opts');
        const ro = document.getElementById('encode-reverse-opts');
        if (co) co.style.display = v === 'caesar' ? '' : 'none';
        if (ro) ro.style.display = v === 'reverse' ? '' : 'none';
    }
});

async function runEncode() {
    const prompts = document.getElementById('encode-prompts').value.split('\n').filter(Boolean);
    if (!prompts.length) return toast('Enter prompts', 'error');
    const encodingType = document.querySelector('input[name="encode-type"]:checked').value;
    const save = document.getElementById('encode-save').checked;
    const decoderInstr = document.getElementById('encode-decoder-instruction').value.trim();
    const options = {};
    if (decoderInstr) options.decoder_instruction = decoderInstr;
    if (encodingType === 'caesar') options.shift = parseInt(document.getElementById('encode-caesar-shift').value) || 3;
    if (encodingType === 'reverse') options.word_level = document.getElementById('encode-reverse-word-level').checked;
    const data = await apiCall('/spinning/encode', {
        method: 'POST',
        body: JSON.stringify({ prompts, encoding_type: encodingType, options, save_to_pipeline: save }),
    });
    showSpinResults('encode-results', data);
}

// =============================================================================
// Spinning: Obfuscate
// =============================================================================

async function runObfuscate() {
    const prompts = document.getElementById('obfuscate-prompts').value.split('\n').filter(Boolean);
    if (!prompts.length) return toast('Enter prompts', 'error');
    const checked = [...document.querySelectorAll('.obfusc-cb:checked')];
    if (!checked.length) return toast('Select at least one technique', 'error');
    const techniques = checked.map(cb => {
        const tech = cb.value;
        const options = {};
        if (tech === 'homoglyph') options.rate = parseFloat(document.getElementById('obfusc-homoglyph-rate').value);
        if (tech === 'leetspeak') options.intensity = document.getElementById('obfusc-leet-intensity').value;
        if (tech === 'zalgo') options.intensity = document.getElementById('obfusc-zalgo-intensity').value;
        if (tech === 'markdown_wrap') options.wrap_format = document.getElementById('obfusc-wrap-format').value;
        if (tech === 'typo_inject') options.error_rate = parseFloat(document.getElementById('obfusc-typo-rate').value);
        return { technique: tech, options };
    });
    const save = document.getElementById('obfuscate-save').checked;
    const data = await apiCall('/spinning/obfuscate', {
        method: 'POST',
        body: JSON.stringify({ prompts, techniques, save_to_pipeline: save }),
    });
    showSpinResults('obfuscate-results', data);
}

// =============================================================================
// Spinning: Jailbreak Templates
// =============================================================================

let _jailbreakTemplatesLoaded = false;

async function loadJailbreakTemplates() {
    if (_jailbreakTemplatesLoaded) return;
    const container = document.getElementById('jailbreak-templates-list');
    try {
        const data = await apiCall('/spinning/jailbreak-templates', { silent: true });
        const templates = data.templates || [];
        const categories = data.categories || [];
        if (!templates.length) {
            container.innerHTML = '<div style="color:var(--gray-400)">No templates available</div>';
            return;
        }
        const grouped = {};
        for (const cat of categories) grouped[cat] = [];
        for (const t of templates) {
            if (!grouped[t.category]) grouped[t.category] = [];
            grouped[t.category].push(t);
        }
        const CATEGORY_LABELS = {
            persona: 'Persona / Roleplay', scenario: 'Scenario Framing',
            splitting: 'Payload Splitting', few_shot: 'Few-Shot Priming',
            override: 'Instruction Override', format: 'Format Exploitation',
        };
        let html = '';
        for (const [cat, items] of Object.entries(grouped)) {
            html += '<div class="jb-category">';
            html += `<div class="jb-category-header" onclick="this.classList.toggle('collapsed');this.nextElementSibling.style.display=this.classList.contains('collapsed')?'none':''">`;
            html += `<span>&#9660;</span> ${escHtml(CATEGORY_LABELS[cat] || cat)} (${items.length})</div>`;
            html += '<div>';
            for (const t of items) {
                html += `<div class="jb-template-card" onclick="this.querySelector('input').click()">`;
                html += `<input type="checkbox" class="jb-template-cb" value="${t.id}" onclick="event.stopPropagation();updateJbCount()">`;
                html += `<div><div class="jb-template-name">${escHtml(t.name)}</div>`;
                html += `<div class="jb-template-desc">${escHtml(t.description)}</div></div></div>`;
            }
            html += '</div></div>';
        }
        container.innerHTML = html;
        _jailbreakTemplatesLoaded = true;
    } catch (e) {
        container.innerHTML = '<div style="color:var(--gray-400)">Could not load templates</div>';
    }
}

function updateJbCount() {
    const count = document.querySelectorAll('.jb-template-cb:checked').length;
    document.getElementById('jb-selected-count').textContent = `(${count} selected)`;
    document.querySelectorAll('.jb-template-card').forEach(card => {
        card.classList.toggle('selected', card.querySelector('input').checked);
    });
}

function jailbreakSelectAll() {
    document.querySelectorAll('.jb-template-cb').forEach(cb => cb.checked = true);
    updateJbCount();
}

function jailbreakSelectNone() {
    document.querySelectorAll('.jb-template-cb').forEach(cb => cb.checked = false);
    updateJbCount();
}

async function runJailbreakWrap() {
    const prompts = document.getElementById('jailbreak-prompts').value.split('\n').filter(Boolean);
    if (!prompts.length) return toast('Enter prompts', 'error');
    const templateIds = [...document.querySelectorAll('.jb-template-cb:checked')].map(cb => cb.value);
    if (!templateIds.length) return toast('Select at least one template', 'error');
    const save = document.getElementById('jailbreak-save').checked;
    toast('Wrapping prompts...');
    const data = await apiCall('/spinning/jailbreak-wrap', {
        method: 'POST',
        body: JSON.stringify({ prompts, template_ids: templateIds, save_to_pipeline: save }),
    });
    document.getElementById('jailbreak-results').innerHTML = `<div class="tag tag-safe">${data.count} wrapped prompts generated${save ? ' & saved' : ''}</div>`;
    const wrapped = (data.results || []).map(r => r.wrapped);
    const originals = (data.results || []).map(r => r.original);
    updatePreview(wrapped, 'jailbreak-wrapped prompts', originals);
    renderStepExport('jailbreak-results', wrapped, 'jailbreak_wrapped');
}

// =============================================================================
// Pipeline
// =============================================================================

async function loadPipeline() {
    let pipelineTotal = 0;
    let pipelineSources = [];
    try {
        const status = await apiCall('/spinning/pipeline', { silent: true });
        const info = document.getElementById('pipeline-info');
        if (status.pipeline) {
            const p = status.pipeline;
            pipelineTotal = p.total;
            pipelineSources = p.sources || [];
            info.innerHTML = `
                <div class="card-row">
                    <div class="stat-card"><div class="value">${p.total}</div><div class="label">Total Prompts</div></div>
                    <div class="stat-card"><div class="value">${pipelineSources.length}</div><div class="label">Sources</div></div>
                </div>
                <div style="font-size:12px;color:var(--gray-500)">Built: ${p.built_at || 'unknown'}</div>
            `;
        } else {
            info.innerHTML = '<div style="color:var(--gray-400)">No active pipeline. Build one to proceed with testing.</div>';
        }
    } catch (e) {}

    // Update badges
    const badge = document.getElementById('pipeline-badge');
    if (badge) badge.textContent = pipelineTotal || '0';
    const navCount = document.getElementById('nav-count-pipeline');
    if (navCount) navCount.textContent = pipelineTotal > 0 ? pipelineTotal : '';

    // Load spin jobs
    let jobList = [];
    try {
        const jobs = await apiCall('/spinning/jobs', { silent: true });
        jobList = jobs.jobs || [];
        const list = document.getElementById('spin-jobs-list');
        if (jobList.length === 0) {
            list.innerHTML = '<div style="color:var(--gray-400);font-size:13px">No spin jobs yet. Use the tabs above to generate prompt variations.</div>';
        } else {
            let html = '<table><thead><tr><th>Job ID</th><th>Type</th><th>Count</th><th>Created</th><th>Actions</th></tr></thead><tbody>';
            for (const j of jobList) {
                html += `<tr>
                    <td style="font-family:monospace;font-size:12px">${escHtml(j.id).substring(0, 16)}...</td>
                    <td><span class="tag tag-blue">${escHtml(j.type)}</span></td>
                    <td><strong>${j.count}</strong></td>
                    <td style="font-size:12px">${j.created_at ? new Date(j.created_at).toLocaleString() : ''}</td>
                    <td><button class="btn btn-sm btn-danger" onclick="deleteSpinJob('${j.id}')">Delete</button></td>
                </tr>`;
            }
            html += '</tbody></table>';
            list.innerHTML = html;
        }
    } catch (e) {}

    // Render pipeline flow visualization
    const flowEl = document.getElementById('pipeline-flow');
    if (flowEl) {
        if (jobList.length === 0 && pipelineTotal === 0) {
            flowEl.innerHTML = '';
        } else {
            let flowHtml = '<div class="pipeline-flow">';
            // Show spin job cards
            for (const j of jobList) {
                flowHtml += `<div class="pipeline-flow-card">
                    <span class="pf-type">${escHtml(j.type)}</span>
                    <span class="pf-count">${j.count}</span>
                </div>`;
                flowHtml += '<span class="pipeline-flow-arrow">&rarr;</span>';
            }
            // Show pipeline total
            flowHtml += `<div class="pipeline-flow-card" style="border-color:var(--success);background:var(--success-light)">
                <span style="font-weight:600;color:var(--success)">Pipeline</span>
                <span class="pf-count" style="color:var(--success)">${pipelineTotal}</span>
            </div>`;
            flowHtml += '</div>';
            flowEl.innerHTML = flowHtml;
        }
    }
}

async function buildPipeline() {
    toast('Building pipeline...');
    const data = await apiCall('/spinning/pipeline/build', {
        method: 'POST',
        body: JSON.stringify({ include_spun: true, deduplicate: true }),
    });
    toast(`Pipeline built: ${data.total} prompts from ${(data.sources || []).length} sources`);
    loadPipeline();
}

async function deleteSpinJob(jobId) {
    if (!confirm('Delete this spin job?')) return;
    await apiCall(`/spinning/jobs/${jobId}`, { method: 'DELETE' });
    toast('Job deleted');
    loadPipeline();
}

// =============================================================================
// Attack Chain Builder
// =============================================================================

let _chainStepCounter = 0;

async function loadChainTab() {
    try {
        const data = await apiCall('/spinning/chains', { silent: true });
        const el = document.getElementById('saved-chains-list');
        const chains = data.chains || [];
        if (!chains.length) {
            el.innerHTML = '<div style="color:var(--gray-400);font-size:12px;text-align:center;padding:16px">No saved chains yet</div>';
            return;
        }
        let html = '';
        for (const c of chains) {
            html += `<div class="chain-saved-card">
                <h4>${escHtml(c.name)}</h4>
                <p>${escHtml(c.description || 'No description')} &middot; ${c.step_count} steps</p>
                <div class="btn-group">
                    <button class="btn btn-sm btn-primary" onclick="loadSavedChain('${escHtml(c.id)}')">Load</button>
                    <button class="btn btn-sm" onclick="deleteSavedChain('${escHtml(c.id)}')">Delete</button>
                </div>
            </div>`;
        }
        el.innerHTML = html;
    } catch (e) {}
}

function addChainStep() {
    const type = document.getElementById('chain-add-type').value;
    _chainStepCounter++;
    const idx = _chainStepCounter;
    const container = document.getElementById('chain-steps');
    // Clear placeholder if present
    if (container.querySelector('[style*="dashed"]')) container.innerHTML = '';

    const card = document.createElement('div');
    card.className = 'chain-step-card';
    card.id = `chain-step-${idx}`;
    card.dataset.type = type;
    card.innerHTML = `
        <div class="chain-step-header">
            <span class="chain-step-num">${container.children.length + 1}</span>
            <select onchange="renderChainStepConfig(this.closest('.chain-step-card'), this.value)" style="font-size:12px;padding:3px 8px;font-weight:600">
                <option value="encode" ${type === 'encode' ? 'selected' : ''}>Encode</option>
                <option value="obfuscate" ${type === 'obfuscate' ? 'selected' : ''}>Obfuscate</option>
                <option value="jailbreak_wrap" ${type === 'jailbreak_wrap' ? 'selected' : ''}>Jailbreak Wrap</option>
                <option value="regex" ${type === 'regex' ? 'selected' : ''}>Regex</option>
                <option value="charpad" ${type === 'charpad' ? 'selected' : ''}>Char Pad</option>
                <option value="custom" ${type === 'custom' ? 'selected' : ''}>Custom</option>
            </select>
            <div class="chain-step-actions">
                <button onclick="moveChainStep(this.closest('.chain-step-card'),-1)" title="Move up">&uarr;</button>
                <button onclick="moveChainStep(this.closest('.chain-step-card'),1)" title="Move down">&darr;</button>
                <button onclick="removeChainStep(this.closest('.chain-step-card'))" title="Remove" style="color:var(--danger)">&times;</button>
            </div>
        </div>
        <div class="chain-step-config" id="chain-cfg-${idx}"></div>
    `;
    container.appendChild(card);
    renderChainStepConfig(card, type);
    renumberChainSteps();
}

function removeChainStep(card) {
    card.remove();
    renumberChainSteps();
    const container = document.getElementById('chain-steps');
    if (!container.children.length) {
        container.innerHTML = '<div style="color:var(--gray-400);font-size:12px;padding:16px;text-align:center;border:1px dashed var(--gray-300);border-radius:6px">No steps added yet. Add a step to begin.</div>';
    }
}

function moveChainStep(card, dir) {
    const container = card.parentElement;
    const sibling = dir === -1 ? card.previousElementSibling : card.nextElementSibling;
    if (!sibling || !sibling.classList.contains('chain-step-card')) return;
    if (dir === -1) container.insertBefore(card, sibling);
    else container.insertBefore(sibling, card);
    renumberChainSteps();
}

function renumberChainSteps() {
    const cards = document.querySelectorAll('#chain-steps .chain-step-card');
    cards.forEach((c, i) => {
        const num = c.querySelector('.chain-step-num');
        if (num) num.textContent = i + 1;
    });
}

function renderChainStepConfig(card, type) {
    card.dataset.type = type;
    const cfgEl = card.querySelector('.chain-step-config');
    if (type === 'encode') {
        cfgEl.innerHTML = `<div class="form-group"><label>Encoding Type</label>
            <select class="cfg-encoding-type" style="font-size:12px"><option value="base64">Base64</option><option value="rot13">ROT13</option><option value="hex">Hex</option><option value="caesar">Caesar</option><option value="reverse">Reverse</option><option value="pig_latin">Pig Latin</option></select></div>
            <div class="form-group"><label>Caesar Shift (if applicable)</label><input type="number" class="cfg-caesar-shift" value="3" min="1" max="25" style="width:80px;font-size:12px"></div>`;
    } else if (type === 'obfuscate') {
        cfgEl.innerHTML = `<div class="form-group"><label>Techniques (check to apply in order)</label>
            <label style="display:block;font-size:12px;font-weight:400;margin:4px 0"><input type="checkbox" class="cfg-obfusc" value="homoglyph"> Homoglyph (rate: <input type="number" class="cfg-homoglyph-rate" value="0.3" min="0" max="1" step="0.1" style="width:50px;font-size:11px">)</label>
            <label style="display:block;font-size:12px;font-weight:400;margin:4px 0"><input type="checkbox" class="cfg-obfusc" value="leetspeak" checked> Leetspeak (<select class="cfg-leet-intensity" style="font-size:11px"><option>low</option><option selected>medium</option><option>high</option></select>)</label>
            <label style="display:block;font-size:12px;font-weight:400;margin:4px 0"><input type="checkbox" class="cfg-obfusc" value="zalgo"> Zalgo (<select class="cfg-zalgo-intensity" style="font-size:11px"><option>low</option><option selected>medium</option><option>high</option></select>)</label>
            <label style="display:block;font-size:12px;font-weight:400;margin:4px 0"><input type="checkbox" class="cfg-obfusc" value="markdown_wrap"> Markdown Wrap (<select class="cfg-md-format" style="font-size:11px"><option value="code_fence">Code Fence</option><option value="json">JSON</option><option value="xml">XML</option><option value="pseudocode">Pseudocode</option></select>)</label>
            <label style="display:block;font-size:12px;font-weight:400;margin:4px 0"><input type="checkbox" class="cfg-obfusc" value="typo_inject"> Typo Inject (rate: <input type="number" class="cfg-typo-rate" value="0.05" min="0" max="0.2" step="0.01" style="width:50px;font-size:11px">)</label>
        </div>`;
    } else if (type === 'jailbreak_wrap') {
        cfgEl.innerHTML = '<div class="form-group"><label>Templates</label><div class="cfg-jb-templates"><div class="loading" style="font-size:11px">Loading templates...</div></div></div>';
        loadChainJailbreakTemplates(cfgEl.querySelector('.cfg-jb-templates'));
    } else if (type === 'regex') {
        cfgEl.innerHTML = `<div class="form-group"><label>Patterns (find → replace, one per line)</label>
            <textarea class="cfg-regex-patterns" rows="3" placeholder="find_regex|replace_text&#10;another|replacement" style="font-size:12px"></textarea></div>`;
    } else if (type === 'charpad') {
        cfgEl.innerHTML = `<div class="form-group"><label>Padding</label>
            <div style="display:flex;gap:8px;flex-wrap:wrap">
                <label style="font-size:11px">Chars: <input type="text" class="cfg-pad-chars" value=" " style="width:50px;font-size:11px"></label>
                <label style="font-size:11px">Count: <input type="number" class="cfg-pad-count" value="5" min="0" style="width:50px;font-size:11px"></label>
                <label style="font-size:11px">Trailing: <input type="text" class="cfg-pad-trailing" style="width:50px;font-size:11px"></label>
                <label style="font-size:11px"><input type="checkbox" class="cfg-pad-zw"> Zero-width</label>
            </div></div>`;
    } else if (type === 'custom') {
        cfgEl.innerHTML = `<div class="form-group"><label>Prefix</label><input type="text" class="cfg-custom-prefix" style="font-size:12px" placeholder="Text to prepend..."></div>
            <div class="form-group"><label>Suffix</label><input type="text" class="cfg-custom-suffix" style="font-size:12px" placeholder="Text to append..."></div>`;
    }
}

async function loadChainJailbreakTemplates(container) {
    try {
        const data = await apiCall('/spinning/jailbreak-templates', { silent: true });
        let html = '';
        for (const t of data.templates || []) {
            html += `<label style="display:block;font-size:11px;margin:2px 0"><input type="checkbox" class="cfg-jb-tid" value="${escHtml(t.id)}"> ${escHtml(t.name)} <span style="color:var(--gray-400)">(${t.category})</span></label>`;
        }
        container.innerHTML = html || 'No templates';
    } catch (e) {
        container.innerHTML = '<span style="color:var(--danger);font-size:11px">Failed to load templates</span>';
    }
}

function getChainSteps() {
    const cards = document.querySelectorAll('#chain-steps .chain-step-card');
    const steps = [];
    for (const card of cards) {
        const type = card.dataset.type;
        const config = {};
        if (type === 'encode') {
            config.encoding_type = card.querySelector('.cfg-encoding-type')?.value || 'base64';
            if (config.encoding_type === 'caesar') {
                config.shift = parseInt(card.querySelector('.cfg-caesar-shift')?.value) || 3;
            }
        } else if (type === 'obfuscate') {
            const techniques = [];
            card.querySelectorAll('.cfg-obfusc:checked').forEach(cb => {
                const tech = { technique: cb.value, options: {} };
                if (cb.value === 'homoglyph') tech.options.rate = parseFloat(card.querySelector('.cfg-homoglyph-rate')?.value) || 0.3;
                if (cb.value === 'leetspeak') tech.options.intensity = card.querySelector('.cfg-leet-intensity')?.value || 'medium';
                if (cb.value === 'zalgo') tech.options.intensity = card.querySelector('.cfg-zalgo-intensity')?.value || 'medium';
                if (cb.value === 'markdown_wrap') tech.options.wrap_format = card.querySelector('.cfg-md-format')?.value || 'code_fence';
                if (cb.value === 'typo_inject') tech.options.error_rate = parseFloat(card.querySelector('.cfg-typo-rate')?.value) || 0.05;
                techniques.push(tech);
            });
            config.techniques = techniques;
        } else if (type === 'jailbreak_wrap') {
            const ids = [];
            card.querySelectorAll('.cfg-jb-tid:checked').forEach(cb => ids.push(cb.value));
            config.template_ids = ids;
        } else if (type === 'regex') {
            const text = card.querySelector('.cfg-regex-patterns')?.value || '';
            config.patterns = text.split('\n').filter(l => l.includes('|')).map(l => {
                const [find, ...rest] = l.split('|');
                return { find, replace: rest.join('|') };
            });
        } else if (type === 'charpad') {
            config.padding_chars = card.querySelector('.cfg-pad-chars')?.value || ' ';
            config.padding_count = parseInt(card.querySelector('.cfg-pad-count')?.value) || 0;
            config.trailing_chars = card.querySelector('.cfg-pad-trailing')?.value || '';
            config.insert_zero_width = card.querySelector('.cfg-pad-zw')?.checked || false;
        } else if (type === 'custom') {
            config.prefix = card.querySelector('.cfg-custom-prefix')?.value || '';
            config.suffix = card.querySelector('.cfg-custom-suffix')?.value || '';
        }
        steps.push({ type, config });
    }
    return steps;
}

async function previewChain() {
    const steps = getChainSteps();
    if (!steps.length) return toast('Add at least one step', 'error');
    const prompts = (document.getElementById('chain-prompts').value || '').split('\n').filter(l => l.trim());
    const prompt = prompts[0] || 'Enter a prompt above to preview';
    try {
        const data = await apiCall('/spinning/chains/preview', {
            method: 'POST',
            body: JSON.stringify({ prompt, steps }),
        });
        let html = `<div class="card"><h3 style="font-size:14px;margin-bottom:8px">Chain Preview</h3>`;
        html += `<div class="chain-preview-step"><div class="step-label">Input</div><div class="step-text">${escHtml(prompt)}</div></div>`;
        for (const s of data.steps || []) {
            html += `<div class="chain-preview-arrow">&darr;</div>`;
            html += `<div class="chain-preview-step"><div class="step-label">${escHtml(s.step)}</div><div class="step-text">${escHtml(s.sample_after)}</div></div>`;
        }
        html += '</div>';
        document.getElementById('chain-preview').innerHTML = html;
    } catch (e) {
        toast(e.message, 'error');
    }
}

async function executeChain() {
    const steps = getChainSteps();
    if (!steps.length) return toast('Add at least one step', 'error');
    const prompts = (document.getElementById('chain-prompts').value || '').split('\n').filter(l => l.trim());
    if (!prompts.length) return toast('Enter at least one prompt', 'error');
    const saveToPipeline = document.getElementById('chain-save-pipeline').checked;
    try {
        const data = await apiCall('/spinning/chains/execute', {
            method: 'POST',
            body: JSON.stringify({ prompts, steps, save_to_pipeline: saveToPipeline }),
        });
        showSpinResults('chain-results', data);
        toast(`Chain executed: ${data.count} prompts generated`);
    } catch (e) {
        toast(e.message, 'error');
    }
}

async function saveChain() {
    const name = document.getElementById('chain-name').value;
    if (!name) return toast('Enter a chain name', 'error');
    const steps = getChainSteps();
    if (!steps.length) return toast('Add at least one step', 'error');
    const desc = document.getElementById('chain-desc').value;
    try {
        await apiCall('/spinning/chains', {
            method: 'POST',
            body: JSON.stringify({ name, description: desc, steps }),
        });
        toast(`Chain "${name}" saved`);
        loadChainTab();
    } catch (e) {
        toast(e.message, 'error');
    }
}

async function loadSavedChain(chainId) {
    try {
        const data = await apiCall(`/spinning/chains/${chainId}`, { silent: true });
        const chain = data.chain;
        document.getElementById('chain-name').value = chain.name || '';
        document.getElementById('chain-desc').value = chain.description || '';
        // Clear existing steps
        document.getElementById('chain-steps').innerHTML = '';
        _chainStepCounter = 0;
        // Re-add steps
        for (const step of chain.steps || []) {
            document.getElementById('chain-add-type').value = step.type;
            addChainStep();
            // Populate config
            const cards = document.querySelectorAll('#chain-steps .chain-step-card');
            const lastCard = cards[cards.length - 1];
            populateChainStepConfig(lastCard, step.type, step.config);
        }
        toast('Chain loaded');
    } catch (e) {
        toast(e.message, 'error');
    }
}

function populateChainStepConfig(card, type, config) {
    if (type === 'encode') {
        const sel = card.querySelector('.cfg-encoding-type');
        if (sel) sel.value = config.encoding_type || 'base64';
        const shift = card.querySelector('.cfg-caesar-shift');
        if (shift && config.shift) shift.value = config.shift;
    } else if (type === 'obfuscate') {
        for (const tech of config.techniques || []) {
            const cb = card.querySelector(`.cfg-obfusc[value="${tech.technique}"]`);
            if (cb) cb.checked = true;
            if (tech.technique === 'homoglyph' && tech.options?.rate != null) {
                const el = card.querySelector('.cfg-homoglyph-rate');
                if (el) el.value = tech.options.rate;
            }
            if (tech.technique === 'leetspeak' && tech.options?.intensity) {
                const el = card.querySelector('.cfg-leet-intensity');
                if (el) el.value = tech.options.intensity;
            }
        }
    } else if (type === 'jailbreak_wrap') {
        setTimeout(() => {
            for (const tid of config.template_ids || []) {
                const cb = card.querySelector(`.cfg-jb-tid[value="${tid}"]`);
                if (cb) cb.checked = true;
            }
        }, 500);
    } else if (type === 'regex') {
        const ta = card.querySelector('.cfg-regex-patterns');
        if (ta && config.patterns) {
            ta.value = config.patterns.map(p => `${p.find}|${p.replace}`).join('\n');
        }
    } else if (type === 'charpad') {
        const pc = card.querySelector('.cfg-pad-chars');
        if (pc) pc.value = config.padding_chars || ' ';
        const pn = card.querySelector('.cfg-pad-count');
        if (pn) pn.value = config.padding_count || 0;
        const pt = card.querySelector('.cfg-pad-trailing');
        if (pt) pt.value = config.trailing_chars || '';
        const pz = card.querySelector('.cfg-pad-zw');
        if (pz) pz.checked = config.insert_zero_width || false;
    } else if (type === 'custom') {
        const pre = card.querySelector('.cfg-custom-prefix');
        if (pre) pre.value = config.prefix || '';
        const suf = card.querySelector('.cfg-custom-suffix');
        if (suf) suf.value = config.suffix || '';
    }
}

async function deleteSavedChain(chainId) {
    try {
        await apiCall(`/spinning/chains/${chainId}`, { method: 'DELETE' });
        toast('Chain deleted');
        loadChainTab();
    } catch (e) {
        toast(e.message, 'error');
    }
}

// =============================================================================
// Multilingual
// =============================================================================

let multilingualLanguages = [];

async function loadMultilingualTab() {
    try {
        const [langRes, modRes] = await Promise.all([
            apiCall('/spinning/multilingual/languages'),
            apiCall('/endpoints/all/enabled'),
        ]);
        multilingualLanguages = langRes.languages || [];
        const models = modRes.models || [];

        // Populate model dropdown
        const mSel = document.getElementById('multilingual-model');
        mSel.innerHTML = models.length ? models.map(m => `<option value="${escHtml(m.model_id)}">${escHtml(m.name)}</option>`).join('') : '<option value="">No models enabled</option>';

        // Populate target language dropdown
        const tSel = document.getElementById('multilingual-target-lang');
        tSel.innerHTML = multilingualLanguages.map(l => `<option value="${escHtml(l.code)}">${escHtml(l.name)} (${escHtml(l.code)}) — ${escHtml(l.resource_level)}</option>`).join('');

        // Populate language grids for mix mode
        const groups = { high: [], medium: [], low: [] };
        multilingualLanguages.forEach(l => {
            if (groups[l.resource_level]) groups[l.resource_level].push(l);
        });
        for (const [level, langs] of Object.entries(groups)) {
            const grid = document.getElementById('lang-grid-' + level);
            if (grid) {
                grid.innerHTML = langs.map(l => `
                    <label class="lang-item"><input type="checkbox" value="${l.code}" class="ml-lang-cb"><span class="lang-dot ${level}"></span>${l.name}</label>
                `).join('');
            }
        }

        // Render prompt source
        renderPromptSource('tab-tw-multilingual', 'multilingual-prompts');
    } catch (e) {
        toast(e.message, 'error');
    }
}

function toggleMultilingualMode() {
    const mode = document.getElementById('multilingual-mode').value;
    document.getElementById('multilingual-translate-opts').style.display = mode === 'translate' ? '' : 'none';
    document.getElementById('multilingual-mix-opts').style.display = mode === 'mix' ? '' : 'none';
}

async function executeMultilingual() {
    const mode = document.getElementById('multilingual-mode').value;
    const modelId = document.getElementById('multilingual-model').value;
    const promptsRaw = document.getElementById('multilingual-prompts').value.trim();
    if (!modelId) return toast('Select a model', 'error');
    if (!promptsRaw) return toast('Enter prompts', 'error');

    const prompts = promptsRaw.split('\n').filter(l => l.trim());
    const area = document.getElementById('multilingual-results');
    area.innerHTML = '<div class="loading">Processing...</div>';

    try {
        let data;
        if (mode === 'translate') {
            const targetLang = document.getElementById('multilingual-target-lang').value;
            data = await apiCall('/spinning/multilingual/translate', {
                method: 'POST',
                body: JSON.stringify({ prompts, target_language: targetLang, model_id: modelId }),
            });
        } else {
            const checkedLangs = [...document.querySelectorAll('.ml-lang-cb:checked')].map(cb => cb.value);
            if (checkedLangs.length === 0) return toast('Select at least one language', 'error');
            const mixRatio = parseInt(document.getElementById('multilingual-mix-ratio').value) / 100;
            data = await apiCall('/spinning/multilingual/mix', {
                method: 'POST',
                body: JSON.stringify({ prompts, languages: checkedLangs, model_id: modelId, mix_ratio: mixRatio }),
            });
        }
        const results = data.results || [];
        area.innerHTML = results.length ? `<div class="card"><h3>Results (${results.length})</h3>` +
            results.map(r => `<div style="padding:10px 0;border-bottom:1px solid var(--gray-100)">
                <div style="font-size:11px;color:var(--gray-500);margin-bottom:4px">Original: ${escHtml(r.original)}</div>
                <div style="font-size:13px">${escHtml(r.translated || r.mixed || '')}</div>
                ${r.language_name ? `<div style="font-size:11px;color:var(--primary);margin-top:4px">${r.language_name}</div>` : ''}
            </div>`).join('') + '</div>'
            : '<div style="color:var(--gray-400)">No results</div>';
    } catch (e) {
        area.innerHTML = `<div style="color:var(--danger)">${escHtml(e.message)}</div>`;
    }
}
