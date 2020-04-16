# 基于UDP传输服务的网络套接字实现（client）
from socket import *
import sys

ADDR = ("127.0.0.1", 8888)
client = socket(AF_INET, SOCK_DGRAM)
# 设置客户端套接字IO为超时非阻塞（如果服务端无响应，则客户端程序退出！）
client.settimeout(3)
while True:
    try:
        data = input("meg>>").encode()
        client.sendto(data, ADDR)
        meg, addr = client.recvfrom(1024)
        print(addr, meg.decode(), sep=":")
    except timeout:
        sys.exit("服务器无响应,程序退出！")
