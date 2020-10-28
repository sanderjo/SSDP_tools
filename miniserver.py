#!/usr/bin/env python3

# miniserver with ssdp and xml

import random
import string
import cherrypy
import threading
import time


class mywebserver(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def toverdoos(self):
        return "You found Toverdoos!"

    @cherrypy.expose
    def description_xml(self):
        # We're sending XML, so tell that:
        cherrypy.response.headers["Content-Type"] = "text/xml; charset=utf-8"

        return f"""<?xml version="1.0" encoding="UTF-8" ?>
<root xmlns="urn:schemas-upnp-org:device-1-0">
<specVersion>
<major>1</major>
<minor>0</minor>
</specVersion>
<URLBase>http://{myip}:8888/toverdoos</URLBase>
<device>
<deviceType>urn:schemas-upnp-org:device:Basic:1</deviceType>
<friendlyName>Toverdoos</friendlyName>
<manufacturer>Toverdoos Team</manufacturer>
<manufacturerURL>http://www.appelboor.com</manufacturerURL>
<modelDescription>Toverdoos spel</modelDescription>
<modelName>Toverdoos 3.4.5</modelName>
<modelNumber>model xyz</modelNumber>
<modelURL>http://www.appelboor.com</modelURL>
<serialNumber>001788721567</serialNumber>
<UDN>uuid:{selfuuid}</UDN>
<presentationURL>toverdoos</presentationURL>
</device>
</root>"""


def startCherrypy():
    cherrypy.config.update({"server.socket_port": 8888})
    cherrypy.server.socket_host = "0.0.0.0"
    cherrypy.quickstart(mywebserver())


def sendbroadcast():

    mySSDPbroadcast = f"""NOTIFY * HTTP/1.1
HOST: 239.255.255.250:1900
CACHE-CONTROL: max-age=60
LOCATION: {selfurl}/description.xml
SERVER: {selfserver_name}
NT: upnp:rootdevice
USN: uuid:{selfuuid}::upnp:rootdevice
NTS: ssdp:alive
OPT: "http://schemas.upnp.org/upnp/1/0/"; ns=01

"""
    mySSDPbroadcast = mySSDPbroadcast.replace("\n", "\r\n").encode("utf-8")
    print("Sending ", mySSDPbroadcast)

    if True:
        # the standard multicast settings for SSDP:
        MCAST_GRP = "239.255.255.250"
        MCAST_PORT = 1900
        MULTICAST_TTL = 2

        # while 1 and not self.__stop:
        if True:
            # Do network stuff
            # Create socket, send the broadcast with our info, and close the socket again
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sock:
                    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
                    sock.sendto(mySSDPbroadcast, (MCAST_GRP, MCAST_PORT))
            except:
                # probably no network
                pass
            # time.sleep(5)


##########################################################################


if __name__ == "__main__":

    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    myip = s.getsockname()[0]
    s.close()

    selfurl = f"http://{myip}:8888"
    selfserver_name = "toverdoos"
    selfuuid = "71ed2395-71cc-4d5e-b123-485d4490571c"

    # server.socket_host: '0.0.0.0'

    print("Starting ...")

    # Start cherrypy webserver in a seperate thread
    cherrypy_thread = threading.Thread(target=startCherrypy)
    cherrypy_thread.start()
    print("webserver is running now")
    print(f"Start. For example: http://{myip}:8888/description.xml\n\n")

    time.sleep(2)  # wait until cherrypy is ready

    # ... so that we can continue with our stuff
    while True:
        print("Send SSDP broadcast")
        sendbroadcast()
        time.sleep(5)
