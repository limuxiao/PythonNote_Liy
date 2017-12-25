# -*- coding:utf-8 -*-
import socket

# 全局变量
socket_list = []


def f1():
    # 1.创建tcp socket，绑定端口，设置监听
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('172.21.150.1', 7788))
    s.listen(5)

    # 2.设置非堵塞
    s.setblocking(False)

    # 3.开启循环
    while True:
        try:
            client_sock, client_addr = s.accept()
            # 将client_sock也设置成非堵塞
            client_sock.setblocking(False)
            # 将client_sock放入列表
            socket_list.append(client_sock)
            print(len(socket_list))
        except:
            pass

        # 4.循环遍历列表
        for sock in socket_list:
            try:
                ret = sock.recv(1024)
                if len(ret) > 0:
                    print('----收到消息：%s----sock id：%d----' %(str(ret), id(sock)))
                    sock.send(b'hhhh')
                    pass
                else:
                    socket_list.remove(sock)
                    sock.close()
            except:
                pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
