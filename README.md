# SSDP_tools
low level python3 SSDP tools for sending and listening

You can send SSDP broadcasts


You can listen for SSDP broadcasts

For example: Google Chrome (looking for a Google Chromecast?):
```
M-SEARCH * HTTP/1.1
HOST: 239.255.255.250:1900
MAN: "ssdp:discover"
MX: 1
ST: urn:dial-multiscreen-org:service:dial:1
USER-AGENT: Google Chrome/86.0.4240.75 Linux
```


A device (in this case: a router) broadcasting it's there:
```
NOTIFY * HTTP/1.1
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
```


This was handy for me reverse engineering & debugging SSDP / XML discovery on Windows

