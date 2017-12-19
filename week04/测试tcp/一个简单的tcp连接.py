# -*- coding:utf-8 -*-
import socket


def f1():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect(('172.21.150.1', 8088))
    tcp.send(b'haha')
    recv = tcp.recv(1024)
    print(recv)
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
