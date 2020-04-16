# 基于TCP传输服务的网络套接字实现（server）
from socket import *
import sys

# 设置全局变量
HOST = "127.0.0.1"
PORT = 8888
ADDR = (HOST, PORT)
server_socket = socket(AF_INET, SOCK_STREAM)
# 绑定地址
server_socket.bind(ADDR)
# 设置监听
server_socket.listen(3)
# 设置监听套接字端口退出后可以立即重用
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 0)
# 循环接受客户端的连接,且处理客户端消息
while True:
    try:
        con_fd, addr = server_socket.accept()
        print("connect from:", addr)
        data = con_fd.recv(1024)
        if not data:
            break
        print(data.decode())
        con_fd.send(b"OK!")
        con_fd.close()
    except KeyboardInterrupt:
        sys.exit("服务端退出！")
    except Exception as e:
        print(e)
        continue
