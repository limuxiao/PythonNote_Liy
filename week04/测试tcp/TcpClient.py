# -*- coding:utf-8 -*-
import socket


class TcpClient(object):
    """
        tcp 客户端类
    """

    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        self.__sock = None
        pass

    def start(self):
        if self.__sock is None:
            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__sock.connect((self.__ip, self.__port))

    def send(self, msg):
        if self.__sock is not None:
            self.__sock.send(bytes(msg, encoding='utf-8'))
            ret = self.__sock.recv(1024)
            print('----服务器返回：%s----' % str(ret, encoding='utf-8'))

    def close(self):
        if self.__sock is not None:
            self.__sock.close()
            self.__sock = None


def f1():
    tcp_client = TcpClient('172.21.150.1', 7788)
    tcp_client.start()
    for i in range(10):
        tcp_client.send('h' * i)
    tcp_client.close()
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
