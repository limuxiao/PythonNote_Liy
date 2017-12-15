# -*- coding:utf-8 -*-
import socket


def f1():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('172.21.150.1', 7788))
    while True:
        ret = s.recvfrom(1024)
        print(ret)
        tt, dev = ret
        content = str(tt, encoding='utf-8')
        print(content)


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
