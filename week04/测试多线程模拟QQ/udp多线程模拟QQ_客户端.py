# -*- coding:utf-8 -*-
import socket
import time


class Client(object):
    """
        客户端类
    """
    def __init__(self, ip, port):
        """
            __init__
        :param ip:  客户端ip
        :param port: 客户端端口
        """
        self.__ip = ip
        self.__port = port
        self.__udp = None
        self.__appoint_ip = None
        self.__appoint_port = None

    def set_appoint(self, appoint_ip, appoint_port):
        """
            设置服务端ip和端口，本方法一定要在send()方法调用之前调用
        :param appoint_ip:
        :param appoint_port:
        :return:
        """
        self.__appoint_ip = appoint_ip
        self.__appoint_port = appoint_port

    def send(self, content):
        """
            发送内容
        :param content:
        :return:
        """
        if self.__ip is None or self.__port is None:
            return

        if self.__udp is None:
            self.__udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.__udp.bind((self.__ip, self.__port))

        self.__udp.sendto(content.encode(encoding='utf-8'), (self.__appoint_ip, self.__appoint_port))


def f1():
    client = Client('', 8889)
    client.set_appoint('172.21.150.1', 7788)
    for i in range(10):
        client.send('我就试试看:%d' % i)
        time.sleep(1)


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
