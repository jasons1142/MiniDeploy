import http.server
import socketserver
import sys
import os

PORT = 8000

# Get folder from command line
folder = sys.argv[1]

# Change working directory to the folder
os.chdir(folder)

# Start HTTP server
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving '{folder}' at http://localhost:{PORT}")
    httpd.serve_forever()