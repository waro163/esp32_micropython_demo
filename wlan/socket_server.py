# http://docs.micropython.org/en/latest/library/socket.html
# 该demo只是一个socket的server示例，直接运行是无法被外界访问，需要开始ap或者sta
import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(10)

print('listening on', addr)

while True:
    conn, addr = s.accept()
    print('client connected from', addr)
    response = "hello world"

    # 发送数据函数 
    conn.send(response)
    # conn.sendall(response)
    # conn.write(response)
    # conn.sendto(response, addr)

    # 读取数据函数
    # data = conn.recv(5)
    # data,src_addr = conn.recvfrom(5)
    # data = conn.read()
    # data = conn.readline()

    # res = bytearray(5)
    # conn.readinto(res, 4)

    # 关闭
    conn.close()