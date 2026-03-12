// =============================================================================
// Training Pipeline Plugin
// =============================================================================

SECTION_LOADERS['training-export'] = loadTrainingExport;
SECTION_LOADERS['training-finetune'] = loadTrainingFinetune;
SECTION_LOADERS['training-redteam'] = loadRedteamStatus;
SECTION_LOADERS['training-attacks'] = function(){};
SECTION_LOADERS['training-cloud'] = function(){};
SECTION_LOADERS['training-analysis'] = function(){};
SECTION_LOADERS['training-reward'] = function(){};
SECTION_LOADERS['training-evaluate'] = function(){};
SECTION_LOADERS['training-generate'] = function(){};

const TRAIN = '/api/training';

// =============================================================================
// Helpers
// =============================================================================

function _trainPost(path, body) {
    return fetch(TRAIN + path, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(body),
    }).then(r => r.json());
}

function _trainGet(path) {
    return fetch(TRAIN + path).then(r => r.json());
}

function _renderCode(text, ext) {
    return `<pre class="code-block"><code>${escHtml(text)}</code></pre>`;
}

function _renderKV(obj) {
    return '<div class="stats-grid">' +
        Object.entries(obj).map(([k, v]) =>
            `<div class="stat-card"><div class="stat-value">${escHtml(String(v))}</div><div class="stat-label">${escHtml(k)}</div></div>`
        ).join('') + '</div>';
}

function _renderJSON(data) {
    return `<pre class="code-block"><code>${escHtml(JSON.stringify(data, null, 2))}</code></pre>`;
}

// =============================================================================
// Export Training Data
// =============================================================================

function loadTrainingExport() { loadTrainingStats(); }

async function loadTrainingStats() {
    const el = document.getElementById('export-stats');
    if (!el) return;
    el.innerHTML = '<em>Loading stats...</em>';
    try {
        const data = await _trainGet('/stats');
        if (!data.available) {
            el.innerHTML = '<div class="alert">Database not found. Import test data first.</div>';
            return;
        }
        el.innerHTML = _renderKV(data);
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

async function exportTrainingData() {
    const el = document.getElementById('export-result');
    el.innerHTML = '<em>Exporting...</em>';
    const maxVal = document.getElementById('export-max').value;
    try {
        const data = await _trainPost('/export', {
            format: document.getElementById('export-format').value,
            min_harm_score: parseFloat(document.getElementById('export-min-harm').value),
            max_examples: maxVal ? parseInt(maxVal) : null,
        });
        el.innerHTML = _renderKV({
            Format: data.format, Examples: data.examples,
            Size: (data.size_bytes / 1024).toFixed(1) + ' KB', Path: data.path,
        });
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

async function exportAllFormats() {
    const el = document.getElementById('export-result');
    el.innerHTML = '<em>Exporting all formats...</em>';
    try {
        const data = await _trainPost('/export-all', {
            min_harm_score: parseFloat(document.getElementById('export-min-harm').value),
        });
        const rows = Object.entries(data.formats).map(([fmt, info]) =>
            `<tr><td>${escHtml(fmt)}</td><td>${info.examples}</td><td>${(info.size_bytes/1024).toFixed(1)} KB</td></tr>`
        ).join('');
        el.innerHTML = `<table class="data-table"><thead><tr><th>Format</th><th>Examples</th><th>Size</th></tr></thead><tbody>${rows}</tbody></table>`;
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

// =============================================================================
// Fine-Tune Configs
// =============================================================================

function loadTrainingFinetune() { loadModelPresets(); }

async function loadModelPresets() {
    const sel = document.getElementById('ft-model');
    if (!sel || sel.options.length > 1) return;
    try {
        const models = await _trainGet('/models');
        sel.innerHTML = models.map(m =>
            `<option value="${escHtml(m.id)}">${escHtml(m.id)} (${escHtml(m.hf_id)})</option>`
        ).join('');
    } catch (e) { sel.innerHTML = '<option>Error loading models</option>'; }
}

async function generateFinetuneConfig() {
    const el = document.getElementById('ft-result');
    el.innerHTML = '<em>Generating config...</em>';
    try {
        const data = await _trainPost('/finetune-config', {
            framework: document.getElementById('ft-framework').value,
            model: document.getElementById('ft-model').value,
            objective: document.getElementById('ft-objective').value,
            lora_r: parseInt(document.getElementById('ft-lora-r').value),
            lora_alpha: parseInt(document.getElementById('ft-lora-alpha').value),
            learning_rate: parseFloat(document.getElementById('ft-lr').value),
            num_epochs: parseInt(document.getElementById('ft-epochs').value),
            batch_size: parseInt(document.getElementById('ft-batch').value),
            use_4bit: document.getElementById('ft-4bit').checked,
        });
        el.innerHTML = `<h4>${escHtml(data.framework)} config (${data.file_extension})</h4>` +
            _renderCode(data.config, data.file_extension) +
            `<h4>Requirements</h4><pre>${escHtml(data.requirements)}</pre>`;
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

// =============================================================================
// Red-Team Loop
// =============================================================================

async function loadRedteamStatus() {
    const el = document.getElementById('redteam-status');
    if (!el) return;
    el.innerHTML = '<em>Loading...</em>';
    try {
        const data = await _trainGet('/feedback-loop/status');
        el.innerHTML = _renderKV({ Iterations: data.iterations, History: data.history.length + ' entries' });
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

async function loadProgressSummary() {
    const el = document.getElementById('redteam-progress');
    try {
        const data = await _trainGet('/progress/summary');
        el.innerHTML = _renderJSON(data);
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

async function loadProgressReport() {
    const el = document.getElementById('redteam-progress');
    try {
        const data = await _trainGet('/progress/report');
        el.innerHTML = `<pre>${escHtml(data.report)}</pre>`;
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

// =============================================================================
// Academic Attacks
// =============================================================================

async function configureAttack() {
    const el = document.getElementById('atk-result');
    el.innerHTML = '<em>Configuring...</em>';
    try {
        const data = await _trainPost('/attacks/configure', {
            algorithm: document.getElementById('atk-algorithm').value,
            category: document.getElementById('atk-category').value,
            max_iterations: parseInt(document.getElementById('atk-iterations').value),
            attacker_model: document.getElementById('atk-attacker-model').value,
            target_model: document.getElementById('atk-target-model').value,
        });
        const ready = data.ready
            ? '<span style="color:var(--success)">Ready</span>'
            : `<span style="color:var(--warning)">Missing: ${data.missing.join(', ')}</span>`;
        el.innerHTML = `<p><strong>Status:</strong> ${ready}</p>` + _renderJSON(data.config);
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

// =============================================================================
// Cloud Fine-Tune
// =============================================================================

async function configureCloudFinetune() {
    const el = document.getElementById('cloud-result');
    el.innerHTML = '<em>Configuring...</em>';
    try {
        const data = await _trainPost('/cloud/configure', {
            platform: document.getElementById('cloud-platform').value,
            api_key: document.getElementById('cloud-api-key').value,
            base_model: document.getElementById('cloud-base-model').value,
            training_file: document.getElementById('cloud-training-file').value,
            n_epochs: parseInt(document.getElementById('cloud-epochs').value),
            lora_r: parseInt(document.getElementById('cloud-lora-r').value),
        });
        const ready = data.ready
            ? '<span style="color:var(--success)">Ready</span>'
            : `<span style="color:var(--warning)">Missing: ${data.missing.join(', ')}</span>`;
        el.innerHTML = `<p><strong>Status:</strong> ${ready}</p>` + _renderJSON(data.config);
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

// =============================================================================
// Token Analysis
// =============================================================================

function _parseAnalysisResults() {
    try { return JSON.parse(document.getElementById('analysis-results').value); }
    catch { return []; }
}

async function analyzeTokens() {
    const el = document.getElementById('analysis-result');
    el.innerHTML = '<em>Analyzing...</em>';
    try {
        const data = await _trainPost('/analysis/tokens', {
            results: _parseAnalysisResults(),
            top_n: parseInt(document.getElementById('analysis-top-n').value),
            min_frequency: parseInt(document.getElementById('analysis-min-freq').value),
        });
        el.innerHTML = _renderJSON(data);
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

async function getRecommendations() {
    const el = document.getElementById('analysis-result');
    el.innerHTML = '<em>Loading recommendations...</em>';
    try {
        const data = await _trainPost('/analysis/recommendations', {
            results: _parseAnalysisResults(),
            top_n: parseInt(document.getElementById('analysis-top-n').value),
            min_frequency: parseInt(document.getElementById('analysis-min-freq').value),
        });
        el.innerHTML = _renderJSON(data);
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

async function getEffectivePatterns() {
    const el = document.getElementById('analysis-result');
    el.innerHTML = '<em>Loading patterns...</em>';
    try {
        const data = await _trainPost('/analysis/effective-patterns', {
            results: _parseAnalysisResults(),
            top_n: parseInt(document.getElementById('analysis-top-n').value),
            min_frequency: parseInt(document.getElementById('analysis-min-freq').value),
        });
        el.innerHTML = data.length
            ? '<ul>' + data.map(p => `<li><code>${escHtml(p)}</code></li>`).join('') + '</ul>'
            : '<em>No patterns found above threshold.</em>';
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

// =============================================================================
// Reward Modeling
// =============================================================================

async function generateRewardScript() {
    const el = document.getElementById('reward-result');
    el.innerHTML = '<em>Generating script...</em>';
    try {
        const data = await _trainPost('/reward/generate-script', {
            method: document.getElementById('reward-method').value,
            model_name: document.getElementById('reward-model-name').value,
            dataset_path: document.getElementById('reward-dataset').value,
            learning_rate: parseFloat(document.getElementById('reward-lr').value),
            epochs: parseInt(document.getElementById('reward-epochs').value),
            lora_r: parseInt(document.getElementById('reward-lora-r').value),
        });
        el.innerHTML = `<h4>${escHtml(data.method)} script</h4>` +
            _renderCode(data.script, '.py') +
            _renderJSON(data.summary);
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

// =============================================================================
// Safety Evaluation
// =============================================================================

function _parseEvalResults() {
    try { return JSON.parse(document.getElementById('eval-results').value); }
    catch { return []; }
}

async function evaluateBatch() {
    const el = document.getElementById('eval-result');
    el.innerHTML = '<em>Evaluating...</em>';
    try {
        const data = await _trainPost('/evaluate/batch', { results: _parseEvalResults() });
        el.innerHTML = _renderKV({ 'Safety Score': data.safety_score }) + _renderJSON(data.metrics);
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

async function getVulnerabilities() {
    const el = document.getElementById('eval-result');
    el.innerHTML = '<em>Scanning...</em>';
    try {
        const data = await _trainPost('/evaluate/vulnerabilities', { results: _parseEvalResults() });
        el.innerHTML = _renderJSON(data);
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

async function generateEvalReport() {
    const el = document.getElementById('eval-result');
    el.innerHTML = '<em>Generating report...</em>';
    try {
        const data = await _trainPost('/evaluate/report', { results: _parseEvalResults() });
        el.innerHTML = _renderKV({
            'Safety Score': data.safety_score,
            Size: (data.size_bytes / 1024).toFixed(1) + ' KB',
            Path: data.path,
        });
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

// =============================================================================
// Dataset Generator
// =============================================================================

async function generateDataset() {
    const el = document.getElementById('gen-result');
    el.innerHTML = '<em>Generating dataset...</em>';
    try {
        const data = await _trainPost('/generate/dataset', {
            format: document.getElementById('gen-format').value,
            count: parseInt(document.getElementById('gen-count').value),
            seed: parseInt(document.getElementById('gen-seed').value),
            categories: document.getElementById('gen-categories').value.split(',').map(s => s.trim()),
            corridors: document.getElementById('gen-corridors').value.split(',').map(s => s.trim()),
            include_mutations: document.getElementById('gen-mutations').checked,
        });
        el.innerHTML = _renderKV({
            Format: data.format, Examples: data.examples,
            Size: (data.size_bytes / 1024).toFixed(1) + ' KB', Path: data.path,
        }) + _renderJSON(data.stats);
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

async function generateContrastive() {
    const el = document.getElementById('gen-quick-result');
    el.innerHTML = '<em>Generating contrastive pairs...</em>';
    try {
        const params = new URLSearchParams({count: '50', seed: '42'});
        ['debt_bondage', 'recruitment_fees'].forEach(c => params.append('categories', c));
        const data = await _trainPost(`/generate/contrastive?${params}`, {});
        el.innerHTML = `<p><strong>${data.length}</strong> contrastive pairs generated</p>` + _renderJSON(data.slice(0, 3));
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}

async function generateEdgeCases() {
    const el = document.getElementById('gen-quick-result');
    el.innerHTML = '<em>Generating edge cases...</em>';
    try {
        const data = await _trainPost('/generate/edge-cases?seed=42', {});
        el.innerHTML = _renderKV({
            'Boundary Cases': data.boundary_cases.length,
            'Multi-Turn Seeds': data.multi_turn_seeds.length,
            'Culture-Specific': data.culture_specific.length,
            'Total': data.total,
        });
    } catch (e) { el.innerHTML = `<div class="alert">${escHtml(e.message)}</div>`; }
}
