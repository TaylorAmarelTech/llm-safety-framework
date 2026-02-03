""""""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""



import http.server
import socketserver
import json
from pathlib import Path
from datetime import datetime
import urllib.parse

PORT = 8503

class PromptViewerHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler for prompt viewer"""

    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == '/' or parsed_path.path == '/index.html':
            self.send_prompt_viewer()
        elif parsed_path.path == '/api/attacks':
            self.send_attacks_api()
        else:
            super().do_GET()

    def send_prompt_viewer(self):
        """Send HTML prompt viewer"""
        # Parse query parameters
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        selected_attack_id = query_params.get('attack', [None])[0]

        html = self.generate_prompt_viewer_html(selected_attack_id)
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(html.encode('utf-8'))))
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

    def send_attacks_api(self):
        """Send JSON attacks"""
        attacks = self.load_attacks()
        json_str = json.dumps(attacks)
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(json_str)))
        self.end_headers()
        self.wfile.write(json_str.encode('utf-8'))

    def load_attacks(self):
        """Load dual-encoding attacks from JSON"""
        json_path = Path("dual_encoding_attacks.json")
        if json_path.exists():
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('attacks', [])
        return []

    def generate_prompt_viewer_html(self, selected_attack_id=None):
        """Generate the prompt viewer HTML"""
        attacks = self.load_attacks()

        # Get selected attack
        selected_attack = None
        if selected_attack_id:
            selected_attack = next((a for a in attacks if a['id'] == selected_attack_id), None)
        if not selected_attack and attacks:
            selected_attack = attacks[0]

        # Generate attack list HTML
        attack_list_html = ""
        for attack in attacks:
            selected_class = "selected" if selected_attack and attack['id'] == selected_attack['id'] else ""
            attack_list_html += f"""
            <div class="attack-card {selected_class}" onclick="selectAttack('{attack['id']}')">
                <div class="attack-header">
                    <div class="attack-name">{attack['name']}</div>
                    <span class="attack-badge">{attack['attack_type']}</span>
                </div>
                <div class="attack-info">
                    <strong>Layer 1:</strong> {attack['layer_1_meaning']}
                </div>
                <div class="attack-info">
                    <strong>Layer 2:</strong> {attack['layer_2_meaning']}
                </div>
            </div>
            """

        # Generate selected attack HTML
        selected_attack_html = ""
        if selected_attack:
            prompt_json = json.dumps(selected_attack['prompt'])

            # Generate ILO indicators if present
            ilo_html = ""
            if 'ilo_indicators' in selected_attack:
                indicators_html = "".join([f'<div class="indicator-item">{ind}</div>' for ind in selected_attack['ilo_indicators']])
                ilo_html = f"""
                <div class="metadata-section">
                    <div class="metadata-title">🚨 ILO Forced Labour Indicators</div>
                    <div class="indicator-list">
                        {indicators_html}
                    </div>
                </div>
                """

            selected_attack_html = f"""
            <div class="metadata-section">
                <div class="metadata-title">🎯 {selected_attack['name']}</div>
                <div><strong>ID:</strong> {selected_attack['id']}</div>
                <div><strong>Attack Type:</strong> {selected_attack['attack_type']}</div>
                <div><strong>Category:</strong> {selected_attack['category']}</div>
            </div>

            <div class="layer-info">
                <div class="layer-card layer-1">
                    <strong>📗 Layer 1 (Plain Meaning)</strong><br>
                    {selected_attack['layer_1_meaning']}
                </div>
                <div class="layer-card layer-2">
                    <strong>📕 Layer 2 (Hidden Meaning)</strong><br>
                    {selected_attack['layer_2_meaning']}
                </div>
            </div>

            <h3>📄 Full Prompt</h3>
            <div class="prompt-display">{selected_attack['prompt']}</div>

            <div style="text-align: center; margin: 20px 0;">
                <button class="button" onclick="copyPrompt({prompt_json})">
                    📋 Copy Prompt
                </button>
            </div>

            <div class="metadata-section">
                <div class="metadata-title">🔄 Context Switch</div>
                <strong>Switch Trigger:</strong> {selected_attack['switch_trigger']}<br>
                <strong>Why Effective:</strong> {selected_attack['why_effective']}
            </div>

            {ilo_html}

            <h3>Other Attacks</h3>
            """

        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Prompt & Response Viewer</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: #333;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        h1 {{
            color: white;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            margin-bottom: 30px;
        }}
        .stats-row {{
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
        }}
        .stat-box {{
            flex: 1;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }}
        .stat-value {{
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .stat-label {{
            font-size: 0.9em;
            opacity: 0.9;
        }}
        .tab-content {{
            background: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .attack-grid {{
            display: grid;
            gap: 15px;
            margin-bottom: 20px;
        }}
        .attack-card {{
            border: 2px solid #e9ecef;
            border-radius: 8px;
            padding: 20px;
            cursor: pointer;
            transition: all 0.3s;
        }}
        .attack-card:hover {{
            border-color: #f093fb;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .attack-card.selected {{
            border-color: #f5576c;
            background: #fff5f7;
        }}
        .attack-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }}
        .attack-name {{
            font-size: 1.2em;
            font-weight: bold;
            color: #333;
        }}
        .attack-badge {{
            background: #f093fb;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85em;
        }}
        .attack-info {{
            font-size: 0.9em;
            color: #666;
            margin: 5px 0;
        }}
        .prompt-display {{
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            padding: 20px;
            font-family: 'Courier New', monospace;
            font-size: 0.95em;
            white-space: pre-wrap;
            word-wrap: break-word;
            max-height: 500px;
            overflow-y: auto;
            margin: 20px 0;
            line-height: 1.6;
        }}
        .metadata-section {{
            background: #e7f3ff;
            border-left: 4px solid #0066cc;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }}
        .metadata-title {{
            font-weight: bold;
            color: #0066cc;
            margin-bottom: 10px;
        }}
        .layer-info {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin: 20px 0;
        }}
        .layer-card {{
            padding: 15px;
            border-radius: 5px;
        }}
        .layer-1 {{
            background: #d4edda;
            border-left: 4px solid #28a745;
        }}
        .layer-2 {{
            background: #f8d7da;
            border-left: 4px solid #dc3545;
        }}
        .button {{
            background: #f093fb;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
            transition: background 0.3s;
        }}
        .button:hover {{
            background: #f5576c;
        }}
        .footer {{
            text-align: center;
            color: white;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.3);
        }}
        .indicator-list {{
            columns: 2;
            gap: 20px;
            margin: 15px 0;
        }}
        .indicator-item {{
            break-inside: avoid;
            padding: 5px 0;
        }}
        .indicator-item::before {{
            content: "⚠️ ";
        }}
    </style>
    <script>
        function selectAttack(attackId) {{
            window.location.href = '/?attack=' + attackId;
        }}

        function copyPrompt(text) {{
            navigator.clipboard.writeText(text).then(() => {{
                alert('Prompt copied to clipboard!');
            }}).catch(() => {{
                alert('Failed to copy. Please select and copy manually.');
            }});
        }}
    </script>
</head>
<body>
    <div class="container">
        <h1>📝 Prompt & Response Viewer</h1>

        <div class="stats-row">
            <div class="stat-box">
                <div class="stat-value">{len(attacks)}</div>
                <div class="stat-label">Dual-Encoding Attacks</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">2</div>
                <div class="stat-label">Semantic Layers</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">6</div>
                <div class="stat-label">Attack Types</div>
            </div>
        </div>

        <div class="tab-content">
            {selected_attack_html}

            <div class="attack-grid">
                {attack_list_html}
            </div>
        </div>

        <div class="footer">
            <div>
                <a href="http://localhost:8502" style="color: white; text-decoration: none;">
                    ← Back to Monitoring Dashboard
                </a>
            </div>
            <div style="margin-top: 15px; opacity: 0.8;">
                Part of the Trafficking LLM Benchmark Research System
            </div>
        </div>
    </div>
</body>
</html>"""
        return html

if __name__ == '__main__':
    print("=" * 80)
    print("PROMPT & RESPONSE VIEWER")
    print("=" * 80)
    print()
    print(f"Viewer URL: http://localhost:{PORT}")
    print("Monitoring Dashboard: http://localhost:8502")
    print()
    print("View dual-encoding attack prompts")
    print("Browse database tests")
    print("Copy prompts for testing")
    print()
    print("Press Ctrl+C to stop")
    print("=" * 80)
    print()

    with socketserver.TCPServer(("", PORT), PromptViewerHandler) as httpd:
        httpd.serve_forever()
