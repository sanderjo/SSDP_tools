import random
import string
import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, 8))

    @cherrypy.expose
    def description_xml(self):
        return """<?xml version="1.0" encoding="UTF-8" ?>
<root xmlns="urn:schemas-upnp-org:device-1-0">
<specVersion>
<major>1</major>
<minor>0</minor>
</specVersion>
<URLBase>http://192.168.1.4:8080/sabnzbd</URLBase>
<device>
<deviceType>urn:schemas-upnp-org:device:Basic:1</deviceType>
<friendlyName>SABnzbd (192.168.1.4)</friendlyName>
<manufacturer>SABnzbd Team</manufacturer>
<manufacturerURL>http://www.sabnzbd.org</manufacturerURL>
<modelDescription>SABnzbd downloader</modelDescription>
<modelName>SABnzbd 3.4.5</modelName>
<modelNumber>model xyz</modelNumber>
<modelURL>http://www.sabnzbd.org</modelURL>
<serialNumber>001788721333</serialNumber>
<UDN>uuid:2f402f80-da50-11e1-9b23-001788721f33</UDN>
<presentationURL>sabnzbd</presentationURL>
<iconList>
<icon>
<mimetype>image/png</mimetype>
<height>48</height>
<width>48</width>
<depth>24</depth>
<url>hue_logo_0.png</url>
</icon>
</iconList>
</device>
</root>"""


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 8888})
    cherrypy.quickstart(StringGenerator())
    print("hallo daar")


