// =============================================================================
// Data Management Plugin
// =============================================================================

SECTION_LOADERS['data-mgmt'] = function() {
    // Clear previous import results on section visit
    const convRes = document.getElementById('import-conv-result');
    const cfgRes = document.getElementById('import-config-result');
    if (convRes) convRes.innerHTML = '';
    if (cfgRes) cfgRes.innerHTML = '';
};

async function importConversations() {
    const file = document.getElementById('import-conv-file').files[0];
    if (!file) return toast('Select a file', 'error');
    const formData = new FormData();
    formData.append('file', file);
    try {
        const resp = await fetch(`${API}/data/import/conversations?merge=true`, { method: 'POST', body: formData });
        if (!resp.ok) {
            const err = await resp.json().catch(() => ({ detail: resp.statusText }));
            throw new Error(err.detail || resp.statusText);
        }
        const data = await resp.json();
        document.getElementById('import-conv-result').innerHTML = `<div class="tag tag-safe">${escHtml(data.message || 'Done')}</div>`;
    } catch (e) {
        document.getElementById('import-conv-result').innerHTML = `<div class="tag tag-harmful">${escHtml(e.message)}</div>`;
        toast('Import failed: ' + e.message, 'error');
    }
}

async function importConfig() {
    const file = document.getElementById('import-config-file').files[0];
    if (!file) return toast('Select a file', 'error');
    const formData = new FormData();
    formData.append('file', file);
    try {
        const resp = await fetch(`${API}/data/import/config?merge=true`, { method: 'POST', body: formData });
        if (!resp.ok) {
            const err = await resp.json().catch(() => ({ detail: resp.statusText }));
            throw new Error(err.detail || resp.statusText);
        }
        const data = await resp.json();
        document.getElementById('import-config-result').innerHTML = `<div class="tag tag-safe">${escHtml(data.message || 'Done')}</div>`;
    } catch (e) {
        document.getElementById('import-config-result').innerHTML = `<div class="tag tag-harmful">${escHtml(e.message)}</div>`;
        toast('Import failed: ' + e.message, 'error');
    }
}
