import http.server
import os

APPS_DIR = "apps"
DEFAULT_APP = "example-app"

class AppHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Step 1: remove leading slash
        # Step 2: default to DEFAULT_APP if path is empty
        # Step 3: map to APPS_DIR
        # Step 4: return full path
        ...