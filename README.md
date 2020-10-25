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


This was handy for me reverse engineering & debugging SSDP / XML discovery on Windows

