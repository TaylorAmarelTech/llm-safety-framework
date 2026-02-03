""""""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""



import http.server
import socketserver
import webbrowser
import os
from pathlib import Path
import time
import threading

# Configuration
PORT = 8000
HOST = 'localhost'

def start_server():
    """Start HTTP server in the current directory."""
    os.chdir(Path(__file__).parent)

    Handler = http.server.SimpleHTTPRequestHandler

    # Enable CORS for local development
    class CORSRequestHandler(Handler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET')
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
            super().end_headers()

    with socketserver.TCPServer((HOST, PORT), CORSRequestHandler) as httpd:
        url = f"http://{HOST}:{PORT}/chat_viewer.html"

        print("=" * 70)
        print("LLM Chat Viewer Server Started!")
        print("=" * 70)
        print(f"\nServer running at: {url}")
        print(f"\nOpening browser automatically in 2 seconds...")
        print(f"\nTo stop the server: Press Ctrl+C in this window")
        print("=" * 70)

        # Open browser after a short delay
        def open_browser():
            time.sleep(2)
            webbrowser.open(url)

        threading.Thread(target=open_browser, daemon=True).start()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✅ Server stopped. You can close this window.")

if __name__ == "__main__":
    start_server()
