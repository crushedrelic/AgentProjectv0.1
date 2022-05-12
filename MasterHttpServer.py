from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

hostname = "localhost"  #serve on localhost
port = 443              #serve on port 443

http_serv = HTTPServer((hostname,port),BaseHTTPRequestHandler) #create handler on defined socket

http_serv.socket = ssl.wrap_socket(http_serv.socket, keyfile="key.pem", certfile="cert.pem", server_side=True)  # ssl publish

http_serv.serve_forever()

