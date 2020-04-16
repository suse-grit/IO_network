# 搭建一个基本的HTTP服务响应(基于select方法的IO多路复用)
from socket import *
from select import *
import re
import sys

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)
r_list = []
w_list = []
e_list = []
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(ADDR)
server_socket.listen(3)
r_list.append(server_socket)
server_socket.setblocking(False)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 0)


def main():
    """
    主函数
    """
    while True:
        rs, ws, es = select(r_list, w_list, e_list)
        try:
            for r in rs:  # 当IO就绪事件为监听套接字时
                if r is server_socket:
                    create_client()
                else:  # 当IO就绪事件为客户端链接套接字时
                    data = r.recv(1024).decode()
                    if not data:
                        r_list.remove(r)
                        r.close()
                        continue
                    client_response(data, r)
        except KeyboardInterrupt:
            sys.exit("web服务器退出!")
        except Exception as e:
            print(e)
            continue


def create_client():
    """
    创建客户端连接套接字,并将客户端连接套接字设置为非阻塞,将其加入select关注
    """
    con_fd, addr = server_socket.accept()
    print("connect from:", addr)
    con_fd.setblocking(False)
    r_list.append(con_fd)


def client_response(data, r):
    """
    对客户端(浏览器)的http请求作响应
    :param data: 客户段的HTTP请求
    :param r: 客户端连接套接字
    """
    pattern = r"[A-Z]+\s*(\S+)"
    request = re.match(pattern, data).group(1)
    if request == "/":
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n\r\n"
        response += "hello world!"
    else:
        response = "HTTP/1.1 404 NOT FOND\r\n"
        response += "Content-Type:text/html\r\n\r\n"
        response += "Sorry!"
    r.send(response.encode())


if __name__ == '__main__':
    # 启动服务
    main()
