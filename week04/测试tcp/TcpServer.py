# -*- coding:utf-8 -*-
import socket
from threading import Thread


class ServerThread(Thread):
    """
        服务端线程类
    """
    def __init__(self, sock, c_addr):
        super().__init__()
        self.__sock = sock
        self.__c_addr = c_addr

    def run(self):
        while True:
            ret = self.__sock.recv(1024)
            print(ret)
            self.__sock.send(b'gg')


class TcpServer(object):
    """
        TcpServer
    """

    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        self.__server = None

    def create_server(self):
        """
            创建一个tcp服务端
        :return: 返回对象自身
        """
        if self.__server is None:
            self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__server.bind((self.__ip, self.__port))
            self.__server.listen(5)

        return self

    def start(self):
        """
            开始处理客户端的连接
        :return:
        """
        while True:
            s_server, c_addr = self.__server.accept()
            # print(c_addr)
            server_thread = ServerThread(s_server, c_addr)
            server_thread.start()
            pass


def f1():
    tcp_server = TcpServer('172.21.150.1', 7788)
    tcp_server.create_server().start()
    pass


def main():
    f1()
    pass

if __name__ == '__main__':
    main()
