#!/usr/bin/env python3

# Send a M-SEARCH, and then listen

import socket

msg = \
    'M-SEARCH * HTTP/1.1\r\n' \
    'HOST:239.255.255.250:1900\r\n' \
    'ST:upnp:rootdevice\r\n' \
    'MX:2\r\n' \
    'MAN:"ssdp:discover"\r\n' \
    'USER-AGENT:Python\r\n\r\n'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
s.bind(('ip of interface',1901))
s.settimeout(10)
print(msg,len(msg))
print(s.sendto(msg, ('239.255.255.250', 1900) ))
resp, (addr, port) = s.recvfrom(1024)
print(resp)
s.close()

