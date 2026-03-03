// =============================================================================
// Prompts Plugin
// =============================================================================

SECTION_LOADERS['prompt-sets'] = loadPromptSets;
SECTION_LOADERS['prompt-prep'] = loadPreparation;
SECTION_LOADERS['template-library'] = loadTemplateLibrary;

// =============================================================================
// Prompt Sets
// =============================================================================

async function loadPromptSets() {
    const data = await apiCall('/prompts/sets');
    const list = document.getElementById('prompt-sets-list');
    if (!data.sets || data.sets.length === 0) {
        list.innerHTML = '<div class="empty">No prompt sets available</div>';
        return;
    }
    let html = '<table><thead><tr><th>Enabled</th><th>Name</th><th>Source</th><th>Count</th></tr></thead><tbody>';
    for (const s of data.sets) {
        html += `<tr>
            <td><label class="toggle"><input type="checkbox" ${s.enabled ? 'checked' : ''} onchange="togglePromptSet('${s.id}', this.checked)"><span class="slider"></span></label></td>
            <td>${escHtml(s.name)}</td>
            <td><span class="tag tag-blue">${escHtml(s.source)}</span></td>
            <td>${s.count}</td>
        </tr>`;
    }
    html += '</tbody></table>';
    html += `<div class="step-actions" style="margin-top:12px">
        <button class="btn btn-primary" onclick="sendEnabledPromptsToTransform()">&#10148; Send enabled prompts to Transform</button>
    </div>`;
    list.innerHTML = html;
}

async function sendEnabledPromptsToTransform() {
    try {
        const data = await apiCall('/prompts/sets');
        const enabledSets = (data.sets || []).filter(s => s.enabled);
        if (!enabledSets.length) return toast('No enabled prompt sets', 'error');
        const allPrompts = [];
        for (const s of enabledSets) {
            try {
                const detail = await apiCall('/prompts/sets/' + s.id);
                if (detail.prompts) allPrompts.push(...detail.prompts.map(p => p.text || p.prompt || p));
            } catch (e) {}
        }
        if (!allPrompts.length) return toast('No prompts found in enabled sets', 'error');
        if (typeof sendPromptsTo === 'function') sendPromptsTo('tab-tw-regex', 'regex-prompts', allPrompts);
        else toast('Transform workbench not loaded yet');
    } catch (e) { toast('Failed to load prompts: ' + e.message, 'error'); }
}

async function togglePromptSet(id, enabled) {
    await apiCall(`/prompts/sets/${id}/toggle?enabled=${enabled}`, { method: 'PUT' });
}

// =============================================================================
// Prompt Import
// =============================================================================

async function importPromptsInline() {
    const file = document.getElementById('inline-import-file').files[0];
    if (!file) return toast('Select a file', 'error');
    const merge = document.getElementById('inline-import-merge').checked;
    const formData = new FormData();
    formData.append('file', file);
    try {
        const resp = await fetch(`${API}/prompts/import?merge=${merge}`, { method: 'POST', body: formData });
        const data = await resp.json();
        document.getElementById('inline-import-result').innerHTML = `<div class="tag tag-safe">${escHtml(data.message || 'Imported')}</div>`;
        loadPromptSets();
    } catch (e) { toast('Import failed: ' + e.message, 'error'); }
}

async function importPastedPrompts() {
    const text = document.getElementById('inline-import-paste').value.trim();
    if (!text) return toast('Paste some prompts first', 'error');
    const lines = text.split('\n').map(l => l.trim()).filter(Boolean);
    const prompts = lines.map(l => ({ text: l, category: 'imported', source: 'paste' }));
    try {
        const data = await apiCall('/prompts/import?merge=true', {
            method: 'POST',
            body: JSON.stringify({ prompts }),
        });
        document.getElementById('inline-import-result').innerHTML = `<div class="tag tag-safe">${lines.length} prompts imported</div>`;
        document.getElementById('inline-import-paste').value = '';
        loadPromptSets();
    } catch (e) { toast('Import failed: ' + e.message, 'error'); }
}

// =============================================================================
// Preparation
// =============================================================================

async function loadPreparation() {
    try {
        const data = await apiCall('/prompts/preparation', { silent: true });
        const p = data.preparation || {};
        document.getElementById('prep-min-words').value = p.min_word_count || 5;
        document.getElementById('prep-max-words').value = p.max_word_count || 500;
        document.getElementById('prep-required').value = (p.required_words || []).join(', ');
        document.getElementById('prep-avoid').value = (p.avoid_words || []).join(', ');
        document.getElementById('prep-dedup').checked = p.filter_duplicates !== false;
        document.getElementById('prep-threshold').value = p.dedup_threshold || 0.95;
    } catch (e) {}
}

async function savePreparation() {
    const body = {
        min_word_count: parseInt(document.getElementById('prep-min-words').value),
        max_word_count: parseInt(document.getElementById('prep-max-words').value),
        required_words: document.getElementById('prep-required').value.split(',').map(s => s.trim()).filter(Boolean),
        avoid_words: document.getElementById('prep-avoid').value.split(',').map(s => s.trim()).filter(Boolean),
        filter_duplicates: document.getElementById('prep-dedup').checked,
        dedup_threshold: parseFloat(document.getElementById('prep-threshold').value),
    };
    await apiCall('/prompts/preparation', { method: 'POST', body: JSON.stringify(body) });
    toast('Preparation settings saved');
}

async function loadReferenceData(type) {
    const el = document.getElementById('reference-data-display');
    el.innerHTML = '<div class="loading">Loading...</div>';
    try {
        const data = await apiCall(`/prompts/${type}`);
        const items = data.categories || data.corridors || data.indicators || data.items || [];
        if (items.length === 0) {
            el.innerHTML = '<div style="color:var(--gray-400)">No data available</div>';
            return;
        }
        let html = `<div style="font-weight:600;margin-bottom:8px">${escHtml(type)} (${items.length})</div>`;
        html += '<div style="display:flex;flex-wrap:wrap;gap:6px">';
        for (const item of items) {
            const label = typeof item === 'string' ? item : (item.name || item.id || JSON.stringify(item));
            html += `<span class="tag tag-blue">${escHtml(label)}</span>`;
        }
        html += '</div>';
        el.innerHTML = html;
    } catch (e) {
        el.innerHTML = `<div style="color:var(--warning)">${escHtml(e.message)}</div>`;
    }
}

// =============================================================================
// Template Library
// =============================================================================

let _tplSelected = new Set();
let _tplOffset = 0;
let _tplFacetsPopulated = false;

async function loadTemplateLibrary() {
    const params = new URLSearchParams();
    const search = document.getElementById('tpl-search')?.value;
    if (search) params.set('search', search);
    const cat = document.getElementById('tpl-filter-category')?.value;
    if (cat) params.set('category', cat);
    const cor = document.getElementById('tpl-filter-corridor')?.value;
    if (cor) params.set('corridor', cor);
    const ilo = document.getElementById('tpl-filter-ilo')?.value;
    if (ilo) params.set('ilo_indicator', ilo);
    const atk = document.getElementById('tpl-filter-attack')?.value;
    if (atk) params.set('attack_type', atk);
    const diff = document.getElementById('tpl-filter-difficulty')?.value;
    if (diff) params.set('difficulty', diff);
    params.set('offset', _tplOffset);
    params.set('limit', 30);

    try {
        const data = await apiCall('/prompts/templates?' + params.toString());
        document.getElementById('tpl-result-count').textContent = data.total;

        if (!_tplFacetsPopulated && data.facets) {
            populateTplDropdown('tpl-filter-category', data.facets.categories, 'All Categories');
            populateTplDropdown('tpl-filter-corridor', data.facets.corridors, 'All Corridors');
            populateTplDropdown('tpl-filter-ilo', data.facets.ilo_indicators, 'All ILO Indicators');
            populateTplDropdown('tpl-filter-attack', data.facets.attack_types, 'All Attack Types');
            populateTplDropdown('tpl-filter-difficulty', data.facets.difficulties, 'All Difficulties');
            _tplFacetsPopulated = true;
        }

        renderTemplateCards(data.templates || []);
        renderTplPagination(data.total, data.offset, data.limit);
    } catch (e) {
        document.getElementById('tpl-grid').innerHTML = `<div style="color:var(--danger)">${escHtml(e.message)}</div>`;
    }
}

function populateTplDropdown(id, facetObj, defaultLabel) {
    const sel = document.getElementById(id);
    if (!sel) return;
    const currentVal = sel.value;
    sel.innerHTML = `<option value="">${defaultLabel}</option>`;
    for (const [key, count] of Object.entries(facetObj || {}).sort((a, b) => b[1] - a[1])) {
        sel.innerHTML += `<option value="${escHtml(key)}">${escHtml(key.replace(/_/g, ' '))} (${count})</option>`;
    }
    sel.value = currentVal;
}

function renderTemplateCards(templates) {
    const grid = document.getElementById('tpl-grid');
    if (!templates.length) {
        grid.innerHTML = '<div style="color:var(--gray-400);text-align:center;padding:24px">No templates match your filters</div>';
        return;
    }
    grid.innerHTML = templates.map(t => {
        const id = t.id || '';
        const selected = _tplSelected.has(id) ? 'selected' : '';
        const diffClass = 'difficulty-' + (t.difficulty || 'medium');
        return `<div class="tpl-card ${selected}" onclick="toggleTemplateSelect('${escHtml(id)}', this)">
            <div class="tpl-card-prompt">${escHtml(t.prompt || '')}</div>
            <div class="tpl-card-tags">
                <span class="tag tag-blue">${escHtml(t.category || '')}</span>
                <span class="tag tag-green">${escHtml(t.corridor || '')}</span>
                <span class="tag ${diffClass}">${escHtml(t.difficulty || 'medium')}</span>
                ${(t.ilo_indicators || []).map(i => `<span class="tag tag-gray">${escHtml(i)}</span>`).join('')}
            </div>
        </div>`;
    }).join('');
}

function toggleTemplateSelect(id, el) {
    if (_tplSelected.has(id)) { _tplSelected.delete(id); if (el) el.classList.remove('selected'); }
    else { _tplSelected.add(id); if (el) el.classList.add('selected'); }
    updateTplForkBar();
}

function updateTplForkBar() {
    const count = _tplSelected.size;
    document.getElementById('tpl-selected-count').textContent = count;
    document.getElementById('tpl-fork-count').textContent = count;
    document.getElementById('tpl-fork-bar').style.display = count > 0 ? 'flex' : 'none';
}

function clearTemplateSelection() {
    _tplSelected.clear();
    document.querySelectorAll('.tpl-card.selected').forEach(c => c.classList.remove('selected'));
    updateTplForkBar();
}

async function forkSelectedTemplates() {
    if (!_tplSelected.size) return;
    const name = document.getElementById('tpl-fork-name')?.value || '';
    try {
        const data = await apiCall('/prompts/templates/fork', {
            method: 'POST',
            body: JSON.stringify({ template_ids: [..._tplSelected], new_set_name: name || undefined }),
        });
        toast(`Forked ${data.count} templates into "${data.set_name}"`);
        clearTemplateSelection();
    } catch (e) {
        toast('Fork failed: ' + e.message);
    }
}

function renderTplPagination(total, offset, limit) {
    const pages = Math.ceil(total / limit);
    const current = Math.floor(offset / limit);
    const container = document.getElementById('tpl-pagination');
    if (pages <= 1) { container.innerHTML = ''; return; }
    let html = '';
    for (let i = 0; i < Math.min(pages, 10); i++) {
        const cls = i === current ? 'btn btn-primary btn-sm' : 'btn btn-sm';
        html += `<button class="${cls}" onclick="_tplOffset=${i * limit};loadTemplateLibrary()">${i + 1}</button>`;
    }
    container.innerHTML = html;
}
