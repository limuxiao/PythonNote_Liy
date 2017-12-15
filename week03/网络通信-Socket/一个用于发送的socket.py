# -*- coding:utf-8 -*-
import socket
import time


def f1():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', 8889))
    while True:
        content = '哈哈哈'
        tt = content.encode(encoding='utf-8')
        s.sendto(tt, ('172.21.150.1', 7788))
        print('----发送成功----')
        time.sleep(1)


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
