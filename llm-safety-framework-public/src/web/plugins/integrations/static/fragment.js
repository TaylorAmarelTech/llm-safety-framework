// =============================================================================
// Library Integrations Plugin
// =============================================================================

SECTION_LOADERS['integrations'] = loadIntegrations;

async function loadIntegrations() {
    try {
        const data = await apiCall('/integrations/status');
        const libs = data.libraries || {};
        const grid = document.getElementById('integration-status-grid');
        grid.innerHTML = Object.entries(libs).map(([name, info]) => `
            <div class="integration-card">
                <h4>${name}</h4>
                <div class="int-status ${info.installed ? 'int-installed' : 'int-missing'}">
                    ${info.installed ? 'Installed' : 'Not Installed'}
                </div>
                ${info.installed ? `<div class="int-version">v${info.version}</div>` : ''}
                <div class="int-methods">${info.method_count || 0} methods available</div>
                ${info.description ? `<div style="font-size:11px;color:var(--gray-500);margin-top:4px">${info.description}</div>` : ''}
                ${!info.installed ? `<div class="int-install-cmd" onclick="copyInstallCmd('${info.pip_install}')" title="Click to copy">${info.pip_install}</div>` : ''}
            </div>
        `).join('');
    } catch (e) {
        toast(e.message, 'error');
    }
}

function copyInstallCmd(cmd) {
    navigator.clipboard.writeText(cmd).then(() => toast('Copied: ' + cmd));
}

async function loadLibraryMethods(library) {
    if (!library) {
        document.getElementById('int-methods-area').innerHTML = '';
        return;
    }
    try {
        const data = await apiCall('/integrations/' + library + '/methods');
        const methods = data.methods || [];
        document.getElementById('int-methods-area').innerHTML = methods.length ?
            `<table class="int-method-table"><thead><tr><th>ID</th><th>Name</th><th>Description</th><th>Type</th></tr></thead><tbody>` +
            methods.map(m => `<tr style="cursor:pointer" onclick="document.getElementById('int-method-id').value='${escHtml(m.id)}';document.getElementById('int-exec-library').value='${escHtml(library)}'">
                <td><code>${escHtml(m.id)}</code></td><td>${escHtml(m.name)}</td><td>${escHtml(m.description||'')}</td><td>${escHtml(m.type||m.category||'')}</td>
            </tr>`).join('') + '</tbody></table>'
            : '<div style="color:var(--gray-400);font-size:13px">No methods found</div>';
    } catch (e) {
        toast(e.message, 'error');
    }
}

async function executeIntegration() {
    const library = document.getElementById('int-exec-library').value;
    const methodId = document.getElementById('int-method-id').value.trim();
    const promptsRaw = document.getElementById('int-prompts').value.trim();
    if (!methodId) return toast('Enter a method ID', 'error');
    if (!promptsRaw) return toast('Enter prompts', 'error');

    const prompts = promptsRaw.split('\n').filter(l => l.trim());
    const area = document.getElementById('int-results-area');
    area.innerHTML = '<div class="loading">Executing...</div>';

    try {
        const data = await apiCall('/integrations/' + library + '/execute', {
            method: 'POST',
            body: JSON.stringify({ method_id: methodId, prompts, save_to_pipeline: true }),
        });
        area.innerHTML = `<div class="card"><h3>Results (${data.count || 0})</h3><pre style="font-size:12px;max-height:400px;overflow:auto">${escHtml(JSON.stringify(data.results, null, 2))}</pre></div>`;
    } catch (e) {
        area.innerHTML = `<div style="color:var(--danger)">${escHtml(e.message)}</div>`;
    }
}
