import http.server
import socketserver
import os

def serve():
    PORT = 3000

    Handler = http.server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer(("", PORT), Handler)


    os.chdir('output')
    print("serving at port", PORT)
    httpd.serve_forever()


if __name__ == '__main__':
    serve()
