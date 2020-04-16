# 基于TCP传输服务的网络套接字（client）
from socket import *
import sys

ADDR = ("127.0.0.1", 8888)
# 创建客户端tcp套接字
client = socket(AF_INET, SOCK_STREAM)
# 建立与服务端的连接
client.connect(ADDR)
meg = input("meg>>")
client.send(meg.encode())
data = client.recv(1024)
if not data:
    sys.exit("服务器错误！")
else:
    print(data.decode())
