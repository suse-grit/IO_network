# 基于UDP传输服务的网络套接字实现（server）
from socket import *
import sys

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)
# 创建UDP套接字
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(ADDR)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 0)
# 循环收发客户端消息并处理（不需要与客户端建立连接）
while True:
    try:
        data, addr = server_socket.recvfrom(1024)
        print("connect from:", addr)
        if not data:
            continue
        print(data.decode())
        server_socket.sendto(b"OK!", addr)
    except KeyboardInterrupt:
        sys.exit("服务器退出！")
    except Exception as e:
        print(e)
        continue
