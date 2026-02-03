#!/usr/bin/env python3
"""
LLM Safety Framework - Web Server Startup Script

Starts the web dashboard server for:
- Configuring API keys and model endpoints
- Running safety tests against LLMs
- Viewing test results and conversations
- Importing/exporting test data

Usage:
    python scripts/start_server.py
    python scripts/start_server.py --port 8080
    python scripts/start_server.py --host 0.0.0.0 --port 8080
"""

import os
import sys
import argparse
import webbrowser
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def main():
    parser = argparse.ArgumentParser(
        description="Start the LLM Safety Testing Framework web dashboard"
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host to bind to (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="Port to listen on (default: 8080)"
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload for development"
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Don't open browser automatically"
    )

    args = parser.parse_args()

    # Print startup banner
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║     LLM Safety Testing Framework - Web Dashboard             ║
    ║                                                              ║
    ║     Testing AI safety against human trafficking and          ║
    ║     labor exploitation scenarios                             ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

    url = f"http://{args.host}:{args.port}"
    print(f"    Starting server at: {url}")
    print(f"    API Documentation: {url}/api/docs")
    print()
    print("    Press Ctrl+C to stop the server")
    print()

    # Open browser
    if not args.no_browser:
        webbrowser.open(url)

    # Start uvicorn server
    try:
        import uvicorn
        from src.web.app import app

        uvicorn.run(
            "src.web.app:app",
            host=args.host,
            port=args.port,
            reload=args.reload,
            log_level="info"
        )
    except ImportError:
        print("Error: uvicorn not installed. Install with: pip install uvicorn")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n    Server stopped.")


if __name__ == "__main__":
    main()
