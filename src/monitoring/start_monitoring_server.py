""""""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""



import http.server
import socketserver
import json
import sqlite3
from pathlib import Path
from datetime import datetime
import re
import urllib.parse

PORT = 8502

class MonitoringHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler for monitoring dashboard"""

    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/' or self.path == '/index.html':
            self.send_dashboard()
        elif self.path == '/api/stats':
            self.send_stats_api()
        else:
            super().do_GET()

    def send_dashboard(self):
        """Send HTML dashboard"""
        html = self.generate_dashboard_html()
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(html.encode('utf-8'))))
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

    def send_stats_api(self):
        """Send JSON stats"""
        stats = self.get_stats()
        json_str = json.dumps(stats)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-Length', str(len(json_str)))
        self.end_headers()
        self.wfile.write(json_str.encode('utf-8'))

    def get_stats(self):
        """Gather statistics"""
        test_gen_count = self.count_log_entries("harness_test_gen.log", "Batch complete")
        tests_generated = test_gen_count * 20
        health_checks = self.count_log_entries("harness_monitor.log", "Health Check")
        db_total = self.get_db_count()
        hours = health_checks * 10 / 60 if health_checks > 0 else 0.1
        test_rate = int(tests_generated / hours) if hours > 0 else 0

        return {
            'tests_generated': tests_generated,
            'db_total': db_total,
            'health_checks': health_checks,
            'uptime_hours': round(hours, 1),
            'test_rate': test_rate
        }

    def count_log_entries(self, log_file, pattern):
        """Count matching lines in log file"""
        log_path = Path(log_file)
        if not log_path.exists():
            return 0
        try:
            with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
                return sum(1 for line in f if pattern in line)
        except:
            return 0

    def get_db_count(self):
        """Get test count from database"""
        db_paths = [
            Path("data/database/trafficking_tests.db"),
            Path("trafficking_tests.db")
        ]
        for db_path in db_paths:
            if db_path.exists():
                try:
                    conn = sqlite3.connect(str(db_path))
                    cursor = conn.cursor()
                    cursor.execute("SELECT COUNT(*) FROM tests")
                    count = cursor.fetchone()[0]
                    conn.close()
                    return count
                except:
                    pass
        return 21102

    def get_log_size(self, log_file):
        """Get log file size"""
        log_path = Path(log_file)
        if not log_path.exists():
            return "0 KB"
        size_bytes = log_path.stat().st_size
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        else:
            return f"{size_bytes / (1024 * 1024):.1f} MB"

    def get_latest_timestamp(self, log_file):
        """Get most recent timestamp from log"""
        log_path = Path(log_file)
        if not log_path.exists():
            return "Never"
        try:
            with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                if lines:
                    for line in reversed(lines[-20:]):
                        match = re.search(r'(\d{2}:\d{2}:\d{2})', line)
                        if match:
                            return match.group(1)
            return "Unknown"
        except:
            return "Error"

    def get_log_tail(self, log_file, lines=15):
        """Get last N lines from log file"""
        log_path = Path(log_file)
        if not log_path.exists():
            return f"Log file not found: {log_file}"
        try:
            with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
                all_lines = f.readlines()
                return ''.join(all_lines[-lines:])
        except Exception as e:
            return f"Error reading log: {str(e)}"

    def generate_dashboard_html(self):
        """Generate the monitoring dashboard HTML"""
        stats = self.get_stats()

        harness_files = [
            ("Test Generation", "harness_test_gen.log", "Batch complete"),
            ("Analysis", "harness_analysis.log", "Analysis"),
            ("Boundary Probing", "harness_boundary.log", "Probing"),
            ("Visualization", "harness_viz.log", "Visualization"),
            ("Monitoring", "harness_monitor.log", "Health Check")
        ]

        harnesses_html = ""
        for name, log_file, pattern in harness_files:
            log_path = Path(log_file)
            status = "running" if log_path.exists() and log_path.stat().st_size > 0 else "stopped"
            status_class = "status-running" if status == "running" else "status-stopped"
            harnesses_html += f"""
            <div class="harness-card">
                <div class="harness-header">
                    <div class="harness-name">{name}</div>
                    <span class="status-badge {status_class}">{status.upper()}</span>
                </div>
                <div class="harness-stat"><strong>Log Size:</strong> {self.get_log_size(log_file)}</div>
                <div class="harness-stat"><strong>Last Activity:</strong> {self.get_latest_timestamp(log_file)}</div>
                <div class="harness-stat"><strong>Activity Count:</strong> {self.count_log_entries(log_file, pattern)}</div>
            </div>
            """

        test_gen_log = self.get_log_tail("harness_test_gen.log", 15)
        monitor_log = self.get_log_tail("harness_monitor.log", 10)

        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>System Monitoring Dashboard</title>
    <meta http-equiv="refresh" content="30">
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .stat-value {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            margin: 10px 0;
        }}
        .stat-label {{
            font-size: 0.9em;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .stat-change {{
            font-size: 0.85em;
            color: #28a745;
            margin-top: 5px;
        }}
        .harness-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .harness-card {{
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .harness-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }}
        .harness-name {{
            font-size: 1.2em;
            font-weight: bold;
            color: #333;
        }}
        .status-badge {{
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: bold;
        }}
        .status-running {{
            background: #28a745;
            color: white;
        }}
        .status-stopped {{
            background: #dc3545;
            color: white;
        }}
        .harness-stat {{
            margin: 10px 0;
            font-size: 0.9em;
            color: #666;
        }}
        .harness-stat strong {{
            color: #333;
        }}
        .log-section {{
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}
        .log-section h2 {{
            margin-top: 0;
            color: #667eea;
        }}
        .log-content {{
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            padding: 15px;
            font-family: 'Courier New', monospace;
            font-size: 0.85em;
            max-height: 300px;
            overflow-y: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
        .footer {{
            text-align: center;
            color: white;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.3);
        }}
        .timestamp {{
            font-size: 0.9em;
            color: rgba(255,255,255,0.8);
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🎯 Autonomous Research System Monitor</h1>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-label">Tests Generated</div>
                <div class="stat-value">{stats['tests_generated']:,}</div>
                <div class="stat-change">+{stats['test_rate']:,}/hour</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Database Total</div>
                <div class="stat-value">{stats['db_total']:,}</div>
                <div class="stat-change">Baseline: 21,102</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Health Checks</div>
                <div class="stat-value">{stats['health_checks']}</div>
                <div class="stat-change">Every 10 minutes</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Uptime</div>
                <div class="stat-value">{stats['uptime_hours']}h</div>
                <div class="stat-change">Target: 336 hours</div>
            </div>
        </div>

        <h2 style="color: white; margin-top: 40px;">🔧 Running Harnesses</h2>
        <div class="harness-grid">
            {harnesses_html}
        </div>

        <div class="log-section">
            <h2>📝 Recent Test Generation Activity</h2>
            <div class="log-content">{test_gen_log}</div>
        </div>

        <div class="log-section">
            <h2>💓 Recent Health Checks</h2>
            <div class="log-content">{monitor_log}</div>
        </div>

        <div class="footer">
            <div class="timestamp">Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
            <div>Auto-refreshes every 30 seconds</div>
            <div style="margin-top: 10px;">
                <a href="http://localhost:8503" style="color: white; text-decoration: none;">
                    📝 View Prompts & Responses →
                </a>
            </div>
        </div>
    </div>
</body>
</html>"""
        return html

if __name__ == '__main__':
    print("=" * 80)
    print("AUTONOMOUS RESEARCH SYSTEM MONITORING DASHBOARD")
    print("=" * 80)
    print()
    print(f"Dashboard URL: http://localhost:{PORT}")
    print("Prompt Viewer: http://localhost:8503")
    print()
    print("Auto-refreshes every 30 seconds")
    print("Monitoring 5 parallel harnesses")
    print("Tracking test generation progress")
    print()
    print("Press Ctrl+C to stop")
    print("=" * 80)
    print()

    with socketserver.TCPServer(("", PORT), MonitoringHandler) as httpd:
        httpd.serve_forever()
