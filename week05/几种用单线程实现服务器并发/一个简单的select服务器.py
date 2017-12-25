# -*- coding:utf-8 -*-
import socket
from select import select


# 1.定义一个全局变量
socket_read_list = []


def f1():
    # 2.创建tcp socket 绑定端口，设置监听
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('172.21.150.1', 7788))
    s.listen(5)

    # 3.将服务器socket放入全局列表中
    socket_read_list.append(s)

    # 4.开启循环,通过select获取可监听socket列表
    while True:
        rlist, wlist, xlist = select(socket_read_list, [], [])
        # 5.遍历
        for sock in rlist:
            if sock == s:       # 说明是服务器socket
                print('----开始监听----')
                client_sock, client_addr = s.accept()
                socket_read_list.append(client_sock)
            else:
                ret = sock.recv(1024)
                if len(ret) > 0:
                    print('----收到消息：%s----socket id:%d----' % (str(ret), id(sock)))
                    sock.send(b'hhhh')
                else:
                    socket_read_list.remove(sock)
                    sock.close()


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
