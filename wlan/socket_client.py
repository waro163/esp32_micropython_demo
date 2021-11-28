import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# print(wlan.scan())
while not wlan.isconnected():
    wlan.connect('ssid-name', 'password')
    time.sleep(1)
# get the interface's IP/netmask/gw/DNS addresses
print(wlan.ifconfig())

import socket
# 获取服务监听地址
addr = socket.getaddrinfo('192.168.4.1', 8080)[0][-1]
s = socket.socket()
s.connect(addr)

while True:
    data = "hello world\n"
    s.send(data)
    resp = s.readline()
    print("get", resp)
    time.sleep(2)