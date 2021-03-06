from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl


class MasterHttpServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type:", "text/html")
        self.end_headers()
        self.wfile.write("Http Server Running")

    def __init__(self, hostIP, port, https):

        self.hostIP = hostIP
        self.port = port
        self.https = https

    def executeServer(self):
        http_serv = HTTPServer((self.hostIP, self.port), SimpleHTTPRequestHandler)  # create handler on defined socket

        if self.https:
            try:

                http_serv.socket = ssl.wrap_socket(http_serv.socket, keyfile="key.pem", certfile="cert.pem",
                                                   server_side=True)  # ssl publish
                print("web server running on: https://%s:%s" % (self.hostIP, self.port))
                http_serv.serve_forever()

            except KeyboardInterrupt:
                print("Keyboard interrupt detected stopping https server...")
                pass
            http_serv.server_close()
            print("Https server stopped.")

        else:
            try:
                print("webserver starting...")
                print("web server running on: http://%s:%s" % (self.hostIP, self.port))
                http_serv.serve_forever()

            except KeyboardInterrupt:
                print("Keyboard interrupt detected stopping http server...")
                pass
            http_serv.server_close()
            print("Http server stopped.")
