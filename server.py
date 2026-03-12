import http.server
import os

APPS_DIR = "apps"
DEFAULT_APP = "example-app"

class AppHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Step 1: remove leading slash
        path = path.lstrip("/")
        # Step 2: default to DEFAULT_APP if path is empty
        if path == "":
            path = DEFAULT_APP
        # Step 3: map to APPS_DIR
        parts = path.split("/")
        app = parts[0]
        subpath = "/".join(parts[1:])

        if subpath == "":
            subpath = "index.html"
            
        # Step 4: return full path
        full_path = os.path.join(APPS_DIR, app, subpath)

        return os.path.abspath(full_path)

import socketserver

PORT = 8000

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), AppHandler) as httpd:
        print(f"MiniDeploy running at http://localhost:{PORT}")
        httpd.serve_forever()