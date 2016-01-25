import http.server
import socketserver
import os

def serve():

    # Serve on port 3000, Todo: let the user choose the port through CLI
    # arguments
    PORT = 3000

    Handler = http.server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer(("", PORT), Handler)

    # Change working directory to output because http.server only serves the
    # working dir
    os.chdir('output')
    print("serving at port", PORT)
    httpd.serve_forever()


if __name__ == '__main__':
    serve()
