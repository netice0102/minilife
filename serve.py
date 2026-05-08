import http.server
import socketserver
import os

os.chdir(r"C:\Users\EYU\Documents\worktest\minilife")
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 8000), handler) as httpd:
    print(f"Serving at port 8000")
    httpd.serve_forever()
