#!/usr/bin/env python3

import socket
import time
from time import gmtime, strftime   


MCAST_GRP = '239.255.255.250' #'224.1.1.1'
MCAST_PORT = 1900 # 5007

MCAST_GRP_IPV6 = 'FF05::C'

myipaddress = socket.gethostbyname(socket.gethostname())

# regarding socket.IP_MULTICAST_TTL
# ---------------------------------
# for all packets sent, after two hops on the network the packet will not 
# be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
MULTICAST_TTL = 2


mymessage = b'NOTIFY * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nCACHE-CONTROL: max-age=60\r\nLOCATION: http://192.168.1.171:8080/description.xml\r\nSERVER: blablaserver 123\r\nNT: upnp:rootdevice\r\nUSN: uuid:11105501-bf96-4bdf-a60f-382e39a0f84c::upnp:rootdevice\r\nNTS: ssdp:alive\r\nOPT: "http://schemas.upnp.org/upnp/1/0/"; ns=01\r\n01-NLS: 1600778333\r\nBOOTID.UPNP.ORG: 1600778333\r\nCONFIGID.UPNP.ORG: 1337\r\n\r\n'
 

while True:
	print(strftime("\n%Y-%m-%d %H:%M:%S", gmtime()))
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sock:
		print("Sending:", mymessage)
		sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
		sock.sendto(mymessage, (MCAST_GRP, MCAST_PORT))
		
	with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sock:
		print("Sending:", mymessage)
		sock.setsockopt(socket.IPPROTO_IPV6, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
		sock.sendto(mymessage, (MCAST_GRP_IPV6, MCAST_PORT))

		
	time.sleep(2)



'''
#mymessage = b"robot"

mymessage = b"""NOTIFY * HTTP/1.1
HOST: 239.255.255.250:1900
CACHE-CONTROL: max-age=60
LOCATION: http://192.168.1.101:8080/
SERVER: Blablaserver
USN: uuid:54405501-bf96-4bdf-a60f-382ddddd84e::urn:schemas-upnp-org:service:WANPPPConnection:1
NTS: ssdp:alive
OPT: "http://schemas.upnp.org/upnp/1/0/"; ns=01
01-NLS: 1600778555
BOOTID.UPNP.ORG: 1600778555
CONFIGID.UPNP.ORG: 1337

"""

mymessage = b"""NOTIFY * HTTP/1.1
HOST: 239.255.255.250:1900
CACHE-CONTROL: max-age=60
LOCATION: http://192.168.1.101:8080/
SERVER: Blablaserver
USN: uuid:54405501-bf96-4bdf-a60f-382ddddd84e::urn:schemas-upnp-org:service:WANPPPConnection:1
NTS: ssdp:alive
OPT: "http://schemas.upnp.org/upnp/1/0/"; ns=01
01-NLS: 1600778555
BOOTID.UPNP.ORG: 1600778555
CONFIGID.UPNP.ORG: 1337

"""
'''


'''
mymessage = b"""NOTIFY * HTTP/1.1
HOST: 239.255.255.250:1900
CACHE-CONTROL: max-age=60
LOCATION: http://192.168.1.254:5000/rootDesc.xml
SERVER: OpenWRT/OpenWrt UPnP/1.1 MiniUPnPd/2.0
NT: urn:schemas-upnp-org:service:WANPPPConnection:1
USN: uuid:54405501-bf96-4bdf-a60f-382e39a0f84e::urn:schemas-upnp-org:service:WANPPPConnection:1
NTS: ssdp:alive
OPT: "http://schemas.upnp.org/upnp/1/0/"; ns=01
01-NLS: 1600778333
BOOTID.UPNP.ORG: 1600778333
CONFIGID.UPNP.ORG: 1337

"""
'''

