import network

# create access-point interface
ap = network.WLAN(network.AP_IF)
# activate the interface
ap.active(True)
# set the ESSID of the access point
# ap.config(essid='ESP32-AP',channel=11,password="123abc")
ap.config(essid='ESP32-AP',password="1234abcd")
# set how many clients can connect to the network
ap.config(max_clients=10)

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

    while True:
        byte_data = conn.readline()
        data = byte_data.decode('utf-8').strip()
        print("get:",data)
        # 发送数据函数
        response = "hello world\n"
        conn.send(response)
        if data == "@close":
            conn.send("good bye:)\n")
            conn.close()
            break
