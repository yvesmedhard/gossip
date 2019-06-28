# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import socketserver

class UDPHandler(socketserver.BaseRequestHandler):
    """
    The UDP RequestHandler for the server. We pass this to the
    server instance, don't directly initialize this class. The 
    server instance will call it each time it needs.
    It is instantiated once per connection to the server, and must 
    override the handle() method to implement communication to the
    client.
    """

    def __init__(self, *args):
        """Pass along any arguments to our parent."""
        socketserver.BaseRequestHandler.__init__(self, *args)

    def handle(self):
        """
        Overrides BaseRequestHandler.handle() to process requests.
        self.request is a tuple == (data socket, client socket)
        """
        data = self.request[0].strip()
        socket = self.request[1]

        # print what we received from client
        print("{} wrote:".format(self.client_address[0]))
        print(data.decode())

        # send back in upper case
        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9090

    # Create server instance
    server = socketserver.UDPServer((HOST, PORT), UDPHandler)

    try:
        print("Serving on port {}. CTRL-c to end...".format(PORT))
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server shutting down...")
sys.exit()