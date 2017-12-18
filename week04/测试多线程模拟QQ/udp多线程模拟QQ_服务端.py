# -*- coding:utf-8 -*-
import socket


class ServerException(Exception):

    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return self.__msg


class Server(object):
    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        self.__udp = None
        pass

    def start(self):
        if self.__udp is None:
            self.__udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if self.__ip is None:
            self.__ip = ''
        if self.__port:
            self.__udp.bind((self.__ip, self.__port))
        while True:
            ret = self.__udp.recvfrom(1024)
            print('----%s----' % str(ret))
            content, dev = ret
            print('content:%s, dev:%s' % (content, dev))
            print(str(content, encoding='utf-8'))
            pass


def f1():
    s = Server('', 7788)
    s.start()


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
