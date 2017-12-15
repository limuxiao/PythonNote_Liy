# -*- coding:utf-8 -*-
import socket


def f1():
    """
        利用socket的udp发送消息
    :return:
    """
    # 创建一个socket,udp
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口，参数为一个tuple，第一个元素为ip，第二个元素为端口
    s.bind(('', 7788))

    # 发送一条消息，第一个参数为要发送的内容，第二个参数是一个tuple
    s.sendto(b'hahaha', ('172.21.150.1', 8080))


def f2():
    """
        利用socket的udp接收消息
    :return:
    """
    # 创建一个socket udp
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    s.bind(('', 8889))

    # 接收消息,1024 表示一次最多接收1024个字节
    ret = s.recvfrom(1024)
    print(ret)


def test01():
    tt = '哈哈'.encode(encoding='utf-8')
    print(type(tt))
    print(tt)
    content = str(tt, encoding='utf-8')
    print(content)
    pass


def main():
    # f1()
    # f2()
    test01()
    pass


if __name__ == '__main__':
    main()
