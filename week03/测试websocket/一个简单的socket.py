# -*- coding:utf-8 -*-
import socket


def f1():
    # help(socket.socket)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # help(s.bind)
    # s.sendto(b'haha', ('172.27.190.1', 8080))
    s.bind(('', 8881))
    recv = s.recvfrom(1024)
    print(recv)
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()