import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# print(wlan.scan())
while not wlan.isconnected():
    wlan.connect('TP-LINK', 'abcdef123456')
    time.sleep(1)
# get the interface's IP/netmask/gw/DNS addresses
print(wlan.ifconfig())

import urequests as request

resp = request.get("http://192.168.0.100:8080")
print(resp.text)

headers = {'Content-Type': 'application/json'}
resp = request.post("http://192.168.0.100:8080",data='{"name":"waro"}',headers=headers)

# import json
# resp = request.post("http://192.168.0.100:8080",data=json.dumps({"name":"waro"}),headers=headers)

# request.put
# request.patch
# request.delete