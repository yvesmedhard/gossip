
# -*- coding: utf-8 -*-

from __future__ import print_function

import socket
import sys

HOST, PORT = "localhost", 9090
data = " ".join(sys.argv[1:])  # Grab CLI args for a message to send

# Create a socket (SOCK_DGRAM means datagrams, aka UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Send some data
    sock.sendto((data  + "\n").encode(), (HOST, PORT))
    received = sock.recv(1024) # 1024 bytes = 1KB
except KeyboardInterrupt:
    print("Forcefully shutting down client...")
    sys.exit(1)

print("Sent: {}".format(data))
print("Received: {}".format(received.decode()))