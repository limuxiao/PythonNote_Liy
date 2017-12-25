# -*- coding:utf-8 -*-
import socket


def f1():
    # 1.创建tcp socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定端口，设置监听
    s.bind(('172.21.150.1', 7788))
    s.listen(5)
    # 3.开启循环监听
    while True:
        client_sock, client_addr = s.accept()
        ret = client_sock.recv(1024)
        if len(ret) > 0:
            print('----收到消息：%s----client_sock id:%d----' % (str(ret), id(client_sock)))
            pass
        else:
            print('----关闭连接----')
            client_sock.close()


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
