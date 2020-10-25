#!/usr/bin/env python3

# Based on https://stackoverflow.com/a/1794373/1492917

import socket
import struct
import sys


# https://en.wikipedia.org/wiki/Simple_Service_Discovery_Protocol
# MyProtocol.MULTICAST_ADDRESS, 1900

MCAST_GRP = '239.255.255.250 ' #'224.1.1.1'
MCAST_PORT = 1900 # 5007
IS_ALL_GROUPS = True

# the user could overrule the port ...
print(sys.argv)
try:
	port = int(sys.argv[1])
	MCAST_PORT = port
	print("Port overruled to", MCAST_PORT)
except:
	pass

print("Port is", MCAST_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if IS_ALL_GROUPS:
    # on this port, receives ALL multicast groups
    sock.bind(('', MCAST_PORT))
else:
    # on this port, listen ONLY to MCAST_GRP
    sock.bind((MCAST_GRP, MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
  # For Python 3, change next line to "print(sock.recv(10240))"
  #print sock.recv(10240)
  receivedblock = sock.recv(10240).decode("utf-8") 
  #print(type(receivedblock))
  print(receivedblock)
  
  
