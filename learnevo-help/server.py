"""
Start the LearnEVO help server.

- Picks the first free port starting at 8765 (so accidental duplicates
  never share the port and start returning empty responses).
- Binds to 127.0.0.1 only (not exposed on the LAN).
- Opens the browser automatically.
- Prints a clean banner with the URL.
- Ctrl+C to stop.
"""
import http.server
import socket
import socketserver
import sys
import threading
import time
import webbrowser
from pathlib import Path


def find_free_port(start=8765, end=8800):
    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind(("127.0.0.1", port))
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
    import os
    os.chdir(here)

    try:
        port = find_free_port()
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    url = f"http://localhost:{port}"
    print(f"""
 ============================================================
  LearnEVO Help
  Serving on {url}
  Opening your browser in 1 second...
  Press Ctrl+C to stop the server.
 ============================================================
""")

    # Open the browser after a short delay so the server has a moment.
    def open_browser():
        time.sleep(1.0)
        webbrowser.open(url)

    threading.Thread(target=open_browser, daemon=True).start()

    with socketserver.TCPServer(("127.0.0.1", port), QuietHandler) as httpd:
        httpd.allow_reuse_address = True
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down. Bye.")


if __name__ == "__main__":
    main()
