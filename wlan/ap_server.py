import network

# create access-point interface
ap = network.WLAN(network.AP_IF)
# set the ESSID of the access point
# ap.config(essid='ESP32-AP',channel=11,password="123abc")
ap.config(essid='ESP32-AP')
# set how many clients can connect to the network
ap.config(max_clients=10)
# activate the interface
ap.active(True)

print(ap.ifconfig())

import socket
addr = socket.getaddrinfo('0.0.0.0', 8080)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(10)
print('listening on', addr)
while True:
    conn, addr = s.accept()
    print('client connected from', addr)

    data = conn.readline()
    print("get:",data)
    # 发送数据函数
    response = "hello world\r\n"
    conn.send(response)
    conn.close()