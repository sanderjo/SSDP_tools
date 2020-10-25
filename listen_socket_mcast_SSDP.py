#!/usr/bin/env python3

# Based on https://stackoverflow.com/a/1794373/1492917

'''
Listen and print unique received SSDP messages
If a SABnzbd broadcast is received, start the webbrowser to the URL
Stop after looptime (default: 60) seconds
'''

import socket
import struct
import sys


# https://en.wikipedia.org/wiki/Simple_Service_Discovery_Protocol
# MyProtocol.MULTICAST_ADDRESS, 1900

MCAST_GRP = "239.255.255.250"
MCAST_PORT = 1900
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
    sock.bind(("", MCAST_PORT))
else:
    # on this port, listen ONLY to MCAST_GRP
    sock.bind((MCAST_GRP, MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


import webbrowser
import requests
import re
import time


ssdpdone = []
done = []

start = time.time()
looptime = 60 # seconds

while time.time()-start < looptime:
    # For Python 3, change next line to "print(sock.recv(10240))"
    # print sock.recv(10240)
    receivedSSDPblock = sock.recv(10240).decode("utf-8")
    # print(type(receivedSSDPblock))
    # print(receivedSSDPblock)
    if receivedSSDPblock not in ssdpdone:
        print(receivedSSDPblock)
        ssdpdone.append(receivedSSDPblock)

    # Find SABnzbd SSDP and XML
    if "sabnzbd" in receivedSSDPblock:
        # print(receivedblock.split("\r\n"))
        for ssdpline in receivedSSDPblock.split("\r\n"):
            if "LOCATION" in ssdpline:
                locationurl = ssdpline.split()[-1]
                # search for something like LOCATION: http://192.168.1.119:8080/sabnzbd/description.xml
                #print("URL is", locationurl)
                xmlmessage = requests.get(locationurl)
                # We should use elementtree to parse the XML, but
                for xmlitem in xmlmessage.content.decode("utf-8").split("\n"):
                    # search for <URLBase>http://192.168.1.119:8080/sabnzbd</URLBase>
                    if "<URLBase>" in xmlitem:
                        saburl = re.findall("\<URLBase\>(.*)\<\/URLBase\>", xmlitem)[0]
                        if saburl not in done:
                            print("Found a SAB instance", saburl)
                            done.append(saburl)
                            webbrowser.open(saburl)


"""
This is what we look for:

 NOTIFY * HTTP/1.1
HOST: 239.255.255.250:1900
CACHE-CONTROL: max-age=60
LOCATION: http://192.168.1.119:8080/sabnzbd/description.xml
SERVER: SABnzbd
NT: upnp:rootdevice
USN: uuid:d62317ed-5ffb-364d-8bd4-c367e999261c::upnp:rootdevice
NTS: ssdp:alive
OPT: "http://schemas.upnp.org/upnp/1/0/"; ns=01

"""
