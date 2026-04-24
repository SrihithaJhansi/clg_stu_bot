#!/usr/bin/env python3
"""
Simple HTTP server to serve the College Assistant frontend
Run this script from the frontend directory to serve the web interface
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from pathlib import Path

def serve_frontend(port=3000, open_browser=True):
    """Serve the frontend on specified port"""

    # Change to frontend directory
    frontend_dir = Path(__file__).parent / "frontend"
    if not frontend_dir.exists():
        print("❌ Error: frontend directory not found!")
        print("Make sure you're running this from the project root directory.")
        sys.exit(1)

    os.chdir(frontend_dir)

    # Create handler
    handler = http.server.SimpleHTTPRequestHandler

    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print("🚀 College Assistant Frontend Server")
            print(f"📁 Serving from: {frontend_dir.absolute()}")
            print(f"🌐 URL: http://localhost:{port}")
            print(f"🔗 Backend API: http://localhost:8000")
            print("📱 Mobile: Use your phone's browser to access the same URL")
            print("\n💡 Tips:")
            print("   - Make sure the backend is running on port 8000")
            print("   - Press Ctrl+C to stop the server")
            print("   - The interface will automatically check backend status")
            print("\n" + "="*50)

            if open_browser:
                webbrowser.open(f"http://localhost:{port}")

            httpd.serve_forever()

    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {port} is already in use. Try a different port:")
            print(f"   python serve_frontend.py {port + 1}")
        else:
            print(f"❌ Error starting server: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    port = 3000

    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ Invalid port number. Using default port 3000.")

    serve_frontend(port)