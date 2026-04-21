"""
Start the LearnEVO help server.

Defaults (local dev, unchanged):
- Binds to 127.0.0.1 only, picks the first free port at/after 8765,
  opens your browser.

Container / LAN deploy overrides via env vars:
- HOST=0.0.0.0        bind on all interfaces
- PORT=8765           pin a fixed port (no free-port scan)
- NO_BROWSER=1        skip the automatic browser launch (also auto-
                      skipped whenever HOST is not 127.0.0.1)

Ctrl+C to stop.
"""
import http.server
import os
import socket
import socketserver
import sys
import threading
import time
import webbrowser
from pathlib import Path


def find_free_port(host, start=8765, end=8800):
    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((host, port))
            s.close()
            return port
        except OSError:
            s.close()
            continue
    raise RuntimeError(f"No free port in {start}..{end}")


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        # Silence routine GETs; keep errors visible.
        if args and ("200" in str(args[1]) or "304" in str(args[1])):
            return
        super().log_message(fmt, *args)

    def end_headers(self):
        # Edge/Chrome heuristically cache responses without Cache-Control
        # for hours when only Last-Modified is sent. Force no-store so CSS
        # and JS edits show up on the next plain reload.
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


def main():
    here = Path(__file__).parent.resolve()
    os.chdir(here)

    host = os.environ.get("HOST", "127.0.0.1")
    port_env = os.environ.get("PORT")
    no_browser = os.environ.get("NO_BROWSER") or host != "127.0.0.1"

    if port_env:
        try:
            port = int(port_env)
        except ValueError:
            print(f"Error: PORT={port_env!r} is not an integer", file=sys.stderr)
            sys.exit(1)
    else:
        try:
            port = find_free_port(host)
        except RuntimeError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    display_host = "localhost" if host == "127.0.0.1" else host
    url = f"http://{display_host}:{port}"
    print(f"""
 ============================================================
  LearnEVO Help
  Serving on {url}   (bind {host}:{port})
  Press Ctrl+C to stop the server.
 ============================================================
""")

    if not no_browser:
        def open_browser():
            time.sleep(1.0)
            webbrowser.open(url)
        threading.Thread(target=open_browser, daemon=True).start()

    with socketserver.ThreadingTCPServer((host, port), QuietHandler) as httpd:
        httpd.allow_reuse_address = True
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down. Bye.")


if __name__ == "__main__":
    main()
