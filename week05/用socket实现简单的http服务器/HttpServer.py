# -*- coding:utf-8 -*-
import socket
from multiprocessing import Process


def func(client_sock):
    ret = client_sock.recv(1024)
    print('----收到的内容：%s----' % str(ret))
    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "hello itcast"
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response data:", response)

    # 向客户端返回响应数据
    client_sock.send(bytes(response, "utf-8"))

    # 关闭客户端连接
    client_sock.close()


def f1():
    # 1.创建tcp
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 7788))
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        p = Process(target=func, args=(client_sock,))
        p.start()
        client_sock.close()
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
