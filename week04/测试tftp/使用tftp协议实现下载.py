# -*- coding:utf-8 -*-
import socket
import struct


def f1():
    # 1.创建udp，绑定端口
    tftp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tftp.bind(('', 7788))

    # 2.构造下载请求
    a = (1, bytes('EUPL-EN.pdf', encoding='utf-8'), 0, bytes('octet', encoding='utf-8'), 0)
    apply_buf = struct.pack("!H11sb5sb", *a)

    # 3.发送请求
    # tftp.sendto(apply_buf, ('172.21.150.1', 69))
    tftp.sendto(apply_buf, ('127.0.0.1', 69))

    recv_file = ''
    p_num = 0

    while True:
        recv_data, recv_dev = tftp.recvfrom(1024)
        # print(recv_dev)
        recv_data_len = len(recv_data)
        cmdTuple = struct.unpack("!HH", recv_data[:4])
        cmd = cmdTuple[0]
        currentPackNum = cmdTuple[1]
        # print(currentPackNum)

        if cmd == 3:

            # 判断是否是第一个数据包
            if currentPackNum == 1:
                recv_file = open('test.pdf', 'ab+')

            # 判断
            if p_num + 1 == currentPackNum:
                # 写入文件
                recv_file.write(recv_data[4:])
                print('(%d)次接收到的数据, 数据长度：%d' % (p_num, recv_data_len))
                p_num += 1

                # 发送给服务器，表示已经收到
                ackBuf = struct.pack("!HH", 4, p_num)
                tftp.sendto(ackBuf, recv_dev)

            # 判断数据大小
            if recv_data_len < 516:
                recv_file.close()
                print('----下载成功----')
                break
        elif cmd == 5:
            break


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
