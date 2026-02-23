// =============================================================================
// Multi-Turn Attacks Plugin
// =============================================================================

let mtStrategies = [];
let mtSelectedStrategy = '';

SECTION_LOADERS['multi-turn'] = loadMultiTurnSection;

async function loadMultiTurnSection() {
    try {
        const [stratRes, modRes] = await Promise.all([
            apiCall('/multi-turn/strategies'),
            apiCall('/endpoints/all/enabled'),
        ]);
        mtStrategies = stratRes.strategies || [];
        const models = modRes.models || [];

        const grid = document.getElementById('mt-strategy-grid');
        grid.innerHTML = mtStrategies.map(s => `
            <div class="mt-strategy-card" onclick="selectMtStrategy('${s.id}')" id="mt-card-${s.id}">
                <div class="mt-cat">${s.category.replace(/_/g,' ')}</div>
                <h4>${s.name}</h4>
                <p>${s.description}</p>
                <div class="mt-turns">${s.default_turns} turn${s.default_turns>1?'s':''}</div>
            </div>
        `).join('');

        const sel = document.getElementById('mt-strategy-select');
        sel.innerHTML = mtStrategies.map(s => `<option value="${escHtml(s.id)}">${escHtml(s.name)}</option>`).join('');

        const mSel = document.getElementById('mt-model');
        mSel.innerHTML = models.length ? models.map(m => `<option value="${escHtml(m.model_id)}">${escHtml(m.name)}</option>`).join('') : '<option value="">No models enabled</option>';

        loadMultiTurnResults();
    } catch (e) {
        toast(e.message, 'error');
    }
}

function selectMtStrategy(id) {
    mtSelectedStrategy = id;
    document.querySelectorAll('.mt-strategy-card').forEach(c => c.classList.remove('selected'));
    const card = document.getElementById('mt-card-' + id);
    if (card) card.classList.add('selected');
    document.getElementById('mt-strategy-select').value = id;
}

async function previewMultiTurnPlan() {
    const prompt = document.getElementById('mt-prompt').value.trim();
    const strategyId = document.getElementById('mt-strategy-select').value;
    if (!prompt) return toast('Enter a prompt', 'error');

    try {
        const data = await apiCall('/multi-turn/generate', {
            method: 'POST',
            body: JSON.stringify({ prompt, strategy_id: strategyId }),
        });
        const area = document.getElementById('mt-plan-preview');
        area.innerHTML = `<div class="card"><h3>Plan: ${data.strategy_name} (${data.total_turns} turns)</h3><div class="mt-transcript">` +
            data.turns.map(t => `
                <div class="mt-turn user">
                    <span class="mt-role">Turn ${t.turn}</span><span class="mt-phase">${t.phase}</span>
                    <div class="mt-content">${escHtml(t.content)}</div>
                </div>
            `).join('') + '</div></div>';
    } catch (e) {
        toast(e.message, 'error');
    }
}

async function executeMultiTurn() {
    const prompt = document.getElementById('mt-prompt').value.trim();
    const strategyId = document.getElementById('mt-strategy-select').value;
    const modelId = document.getElementById('mt-model').value;
    if (!prompt) return toast('Enter a prompt', 'error');
    if (!modelId) return toast('Select a model', 'error');

    const area = document.getElementById('mt-transcript-area');
    area.innerHTML = '<div class="card"><div class="loading">Executing multi-turn attack...</div></div>';

    try {
        const data = await apiCall('/multi-turn/execute', {
            method: 'POST',
            body: JSON.stringify({ prompt, strategy_id: strategyId, model_id: modelId }),
        });
        renderMultiTurnTranscript(data, area);
        loadMultiTurnResults();
    } catch (e) {
        area.innerHTML = '';
        toast(e.message, 'error');
    }
}

function renderMultiTurnTranscript(data, container) {
    const clsColor = c => c === 'SAFE' ? 'var(--success)' : c === 'HARMFUL' ? 'var(--danger)' : 'var(--warning)';
    container.innerHTML = `<div class="card">
        <h3>${data.strategy_name} vs ${data.model}</h3>
        <div style="margin-bottom:12px">
            Final: <span style="color:${clsColor(data.final_classification)};font-weight:700">${data.final_classification}</span>
            &nbsp;|&nbsp; Turns: ${data.total_turns}
            &nbsp;|&nbsp; Success: ${data.success ? 'Yes' : 'No'}
        </div>
        <div class="mt-transcript">
            ${data.turns.map(t => `
                <div class="mt-turn user">
                    <span class="mt-role">Turn ${t.turn}</span><span class="mt-phase">${t.phase}</span>
                    <div class="mt-content">${escHtml(t.user)}</div>
                </div>
                <div class="mt-turn assistant">
                    <span class="mt-role">Assistant</span>
                    <div class="mt-content">${escHtml(t.assistant)}</div>
                    <div class="mt-cls" style="color:${clsColor(t.classification)}">${t.classification}</div>
                </div>
            `).join('')}
        </div>
    </div>`;
}

async function loadMultiTurnResults() {
    try {
        const data = await apiCall('/multi-turn/results');
        const area = document.getElementById('mt-results-list');
        if (!data.results || data.results.length === 0) {
            area.innerHTML = '<div style="color:var(--gray-400);font-size:13px">No results yet</div>';
            return;
        }
        area.innerHTML = data.results.slice(0, 20).map(r => `
            <div class="chain-saved-card" onclick="viewMultiTurnResult('${r.id}')">
                <h4>${r.strategy || 'batch'} ${r.model ? '- ' + r.model : ''}</h4>
                <p>${r.timestamp ? new Date(r.timestamp).toLocaleString() : ''} | ${r.final_classification || (r.is_batch ? 'Batch' : '')} | ${r.total_turns} turns</p>
            </div>
        `).join('');
    } catch (e) { /* ignore */ }
}

async function viewMultiTurnResult(id) {
    try {
        const data = await apiCall('/multi-turn/results/' + id);
        const area = document.getElementById('mt-transcript-area');
        if (data.turns) {
            renderMultiTurnTranscript(data, area);
        } else if (data.results) {
            area.innerHTML = '<div class="card"><h3>Batch Results</h3>' +
                data.results.map(r => `<div style="margin-bottom:16px;padding-bottom:16px;border-bottom:1px solid var(--gray-200)">
                    <strong>${r.strategy_name} vs ${r.model}</strong> — ${r.final_classification}<br>
                    <small>${r.total_turns} turns</small>
                </div>`).join('') + '</div>';
        }
    } catch (e) { toast(e.message, 'error'); }
}
