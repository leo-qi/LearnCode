import os
from http.server import HTTPServer, CGIHTTPRequestHandler

os.chdir("Python/Head_First_Python/Chapter7/webapp/")
port = 8080

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

