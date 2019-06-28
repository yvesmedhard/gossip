# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import socket
import socketserver
import peer_addresses
import logging
import threading
import time
import random

HOST = sys.argv[1]
PORT = sys.argv[2]

print(HOST, PORT)

SEND_DATA_TIMEOUT = 2000


class UDPHandler(socketserver.BaseRequestHandler):
  def __init__(self, *args):
      socketserver.BaseRequestHandler.__init__(self, *args)
  
  def handle(self):
    data = self.request[0].strip()
    socket = self.request[1]

    print("{} wrote:".format(self.client_address[0]))
    print(data.decode())

    socket.sendto(data.upper(), self.client_address)
    

def choose_random_peer():
  return random.choice(
    [peer for i, peer in enumerate(peer_addresses.PEERS) if peer['host'] != HOST or peer['port'] != PORT ]
  )

def send_data_to_random_peer(self):
  while(True):
    peer = choose_random_peer()
    data_to_send = 'TODO GET DATA TO SEND'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto((data_to_send).encode(), (peer['host'], peer['port']))
    logging.info("Sent current state to: %s %s", peer['host'], peer['port'])
    received = sock.recv(1024)
    logging.info("Data received by: %s %s and responded %s", peer['host'], peer['port'], received.decode())
    time.sleep(SEND_DATA_TIMEOUT)

choose_random_peer()

# server = socketserver.UDPServer((HOST, PORT), UDPHandler)
# try:
#     print("Serving on port {}. CTRL-c to end...".format(PORT))
#     server.serve_forever()
# except KeyboardInterrupt:
#     print("Server shutting down...")
# sys.exit()