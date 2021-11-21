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

import socket
addr = socket.getaddrinfo('0.0.0.0', 8080)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(10)
print('listening on', addr)
while True:
    conn, addr = s.accept()
    print('client connected from', addr)
    
    # 发送数据函数
    response = "hello world\r\n"
    conn.send(response)
    conn.close()