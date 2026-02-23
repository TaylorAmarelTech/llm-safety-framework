// =============================================================================
// Endpoints Plugin
// =============================================================================

SECTION_LOADERS['endpoints'] = loadEndpoints;

function showAddEndpoint() {
    document.getElementById('add-endpoint-form').style.display = '';
}

async function createEndpoint() {
    const id = document.getElementById('new-ep-id').value.trim();
    const name = document.getElementById('new-ep-name').value.trim();
    const base_url = document.getElementById('new-ep-url').value.trim();
    const request_format = document.getElementById('new-ep-format').value;
    const api_key = document.getElementById('new-ep-key').value;
    if (!id || !name || !base_url) return toast('ID, Name, and URL are required', 'error');
    await apiCall('/endpoints', {
        method: 'POST',
        body: JSON.stringify({ id, name, base_url, request_format, api_key }),
    });
    toast('Endpoint created');
    document.getElementById('add-endpoint-form').style.display = 'none';
    loadEndpoints();
    refreshContextBar();
}

async function loadEndpoints() {
    const data = await apiCall('/endpoints');
    const list = document.getElementById('endpoints-list');

    if (!data.endpoints || data.endpoints.length === 0) {
        list.innerHTML = '<div class="empty"><div class="icon">&#9881;</div>No endpoints configured</div>';
        return;
    }

    let html = '';
    for (const ep of data.endpoints) {
        html += `<div class="endpoint-card" id="ep-${ep.id}">
            <div class="endpoint-header" onclick="toggleEndpoint('${ep.id}')">
                <span class="arrow">&#9654;</span>
                <span class="name">${escHtml(ep.name)}</span>
                <span class="url">${escHtml(ep.base_url || '')}</span>
                <div class="right">
                    <span class="tag tag-blue">${ep.model_count || 0} models</span>
                    <span style="font-size:12px;color:var(--gray-400)">${ep.api_key_masked || 'No key'}</span>
                </div>
            </div>
            <div class="endpoint-body">
                <div class="form-row" style="margin-bottom:12px">
                    <div class="form-group">
                        <label>Name</label>
                        <div style="display:flex;gap:8px">
                            <input type="text" id="epname-${ep.id}" value="${escHtml(ep.name)}" style="width:200px">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Base URL</label>
                        <div style="display:flex;gap:8px">
                            <input type="text" id="epurl-${ep.id}" value="${escHtml(ep.base_url || '')}" style="width:300px">
                        </div>
                    </div>
                    <div class="form-group" style="align-self:end">
                        <label><input type="checkbox" id="epenabled-${ep.id}" ${ep.enabled !== false ? 'checked' : ''}> Enabled</label>
                    </div>
                </div>
                <div style="display:flex;gap:8px;margin-bottom:12px">
                    <button class="btn btn-sm btn-primary" onclick="saveEndpointSettings('${ep.id}')">Save Settings</button>
                    <button class="btn btn-sm" style="color:var(--warning)" onclick="deleteEndpoint('${ep.id}','${escHtml(ep.name)}')">Delete Endpoint</button>
                </div>
                <div class="form-row" style="margin-bottom:12px">
                    <div class="form-group">
                        <label>API Key</label>
                        <div style="display:flex;gap:8px">
                            <input type="password" id="key-${ep.id}" placeholder="Enter API key" value="">
                            <button class="btn btn-sm btn-primary" onclick="saveEndpointKey('${ep.id}')">Save Key</button>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Preview API Call</label>
                        <button class="btn btn-sm" onclick="previewApiCall('${ep.id}')">Show Preview</button>
                    </div>
                </div>
                <div id="preview-${ep.id}" style="display:none;margin-bottom:12px"></div>
                <h4 style="font-size:13px;margin-bottom:8px;">Models</h4>
                <div id="models-${ep.id}"><div class="loading">Loading models...</div></div>
                <div style="margin-top:8px;display:flex;gap:8px">
                    <input type="text" id="new-model-${ep.id}" placeholder="Model ID (e.g. gpt-4o)" style="width:200px">
                    <button class="btn btn-sm" onclick="addModel('${ep.id}')">+ Add Model</button>
                    ${ep.provider_type === 'openrouter' || ep.id === 'openrouter' ? `<button class="btn btn-sm" onclick="discoverModels('${ep.id}')">Fetch Available Models</button>` : ''}
                </div>
            </div>
        </div>`;
    }
    list.innerHTML = html;

    for (const ep of data.endpoints) {
        loadModelsForEndpoint(ep.id);
    }
}

function toggleEndpoint(id) {
    document.getElementById('ep-' + id).classList.toggle('open');
}

async function saveEndpointKey(epId) {
    const key = document.getElementById('key-' + epId).value;
    if (!key) return toast('Enter an API key', 'error');
    await apiCall(`/endpoints/${epId}/key`, { method: 'PUT', body: JSON.stringify({ api_key: key }) });
    toast('API key saved');
    loadEndpoints();
}

async function saveEndpointSettings(epId) {
    const name = document.getElementById('epname-' + epId).value;
    const base_url = document.getElementById('epurl-' + epId).value;
    const enabled = document.getElementById('epenabled-' + epId).checked;
    if (!name || !base_url) return toast('Name and URL are required', 'error');
    await apiCall(`/endpoints/${epId}`, {
        method: 'PUT',
        body: JSON.stringify({ name, base_url, enabled }),
    });
    toast('Endpoint settings saved');
    loadEndpoints();
}

async function deleteEndpoint(epId, epName) {
    if (!confirm(`Delete endpoint "${epName}"? This will remove all its models too.`)) return;
    await apiCall(`/endpoints/${epId}`, { method: 'DELETE' });
    toast('Endpoint deleted');
    loadEndpoints();
}

async function previewApiCall(epId) {
    const data = await apiCall(`/endpoints/${epId}/preview`);
    const div = document.getElementById('preview-' + epId);
    div.style.display = 'block';
    div.innerHTML = `<div class="preview-box">${escHtml(JSON.stringify(data.preview, null, 2))}</div>`;
}

async function loadModelsForEndpoint(epId) {
    const data = await apiCall(`/endpoints/${epId}/models`, { silent: true });
    const container = document.getElementById('models-' + epId);
    if (!data.models || data.models.length === 0) {
        container.innerHTML = '<div style="color:var(--gray-400);font-size:12px">No models configured</div>';
        return;
    }
    let html = '';
    for (const m of data.models) {
        html += `<div class="model-row">
            <label class="toggle"><input type="checkbox" ${m.enabled ? 'checked' : ''} onchange="toggleModel('${m.id}', this.checked)"><span class="slider"></span></label>
            <span class="model-name">${escHtml(m.name)}</span>
            <span class="model-id">${escHtml(m.model_id)}</span>
            <div class="model-actions">
                <button class="btn btn-sm btn-danger" onclick="deleteModel('${epId}','${m.model_id}')">Remove</button>
            </div>
        </div>`;
    }
    container.innerHTML = html;
}

async function addModel(epId) {
    const modelId = document.getElementById('new-model-' + epId).value;
    if (!modelId) return toast('Enter a model ID', 'error');
    await apiCall(`/endpoints/${epId}/models`, {
        method: 'POST',
        body: JSON.stringify({ name: modelId, model_id: modelId, enabled: false }),
    });
    toast('Model added');
    loadModelsForEndpoint(epId);
}

async function toggleModel(fullId, enabled) {
    const parts = fullId.split('/');
    const epId = parts[0];
    const modelId = parts.slice(1).join('/');
    await apiCall(`/endpoints/${epId}/models/${modelId}`, {
        method: 'PUT',
        body: JSON.stringify({ enabled }),
    });
}

async function deleteModel(epId, modelId) {
    if (!confirm(`Remove model ${modelId}?`)) return;
    await apiCall(`/endpoints/${epId}/models/${modelId}`, { method: 'DELETE' });
    toast('Model removed');
    loadModelsForEndpoint(epId);
}

async function discoverModels(epId) {
    toast('Fetching models...');
    try {
        const data = await apiCall(`/endpoints/${epId}/discover-models`);
        const models = data.models || [];
        let msg = `Found ${models.length} models. `;
        if (models.length > 0) {
            const names = models.slice(0, 5).map(m => m.id).join(', ');
            msg += `First 5: ${names}`;
        }
        toast(msg);
        const container = document.getElementById('models-' + epId);
        let html = container.innerHTML;
        html += '<div style="margin-top:8px;border-top:1px solid var(--gray-200);padding-top:8px"><strong style="font-size:12px">Discovered Models (click to add):</strong><div style="max-height:200px;overflow-y:auto;margin-top:4px">';
        for (const m of models.slice(0, 50)) {
            html += `<div style="padding:4px 8px;font-size:12px;cursor:pointer;border-bottom:1px solid var(--gray-100)" onclick="document.getElementById('new-model-${epId}').value='${escHtml(m.id)}'">${escHtml(m.id)} ${m.context_length ? '(' + m.context_length + ' ctx)' : ''}</div>`;
        }
        html += '</div></div>';
        container.innerHTML = html;
    } catch (e) {
        toast('Failed to fetch models: ' + e.message, 'error');
    }
}

// Helper for other plugins that need enabled models
async function loadEnabledModels() {
    try {
        const data = await apiCall('/endpoints/all/enabled', { silent: true });
        return data.models || [];
    } catch (e) { return []; }
}
