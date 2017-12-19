# -*- coding:utf-8 -*-
import socket
import struct
import os


class BaseServer(object):
    """
        基础服务类
    """
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.tftp = None
        self.appoint_ip = None
        self.appoint_port = None
        pass

    def set_appoint(self, appoint_ip, appoint_port):
        self.appoint_ip = appoint_ip
        self.appoint_port = appoint_port
        pass

    def creat_tftp(self):
        if self.tftp is None:
            self.tftp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.tftp.bind((self.ip, self.port))


class DownloadServer(BaseServer):
    """
        tftp协议下载类
    """
    def download(self, file_name):
        self.creat_tftp()

        # 1.组装数据
        fmt = '!H%dsb5sb' % len(file_name)
        a = (1, bytes(file_name, encoding='utf-8'), 0, bytes('octet', encoding='utf-8'), 0)
        send_data = struct.pack(fmt, *a)
        self.tftp.sendto(send_data, (self.appoint_ip, self.appoint_port))
        p_num = 0
        recv_file = None
        while True:
            recv_data, recv_dev = self.tftp.recvfrom(1024)
            # print('----得到的结果:%s----' % str(recv_data))
            recv_types = recv_data[:4]
            recv_type, recv_page = struct.unpack('!HH', recv_types)
            # print('----得到的recv_type:%d----recv_page:%d' % (recv_type, recv_page))
            # 判断响应码, 3 -- 正常响应数据
            if recv_type == 3:
                p_num += 1
                # 判断是否是第一次接收数据,如果是第一次则创建新文件
                if p_num == 1:
                    recv_file = open(file_name, 'ab+')

                # 避免重写
                if p_num == recv_page:
                    recv_file.write(recv_data[4:])

                # 给服务器返回数据
                any_data = struct.pack('!HH', 4, p_num)
                self.tftp.sendto(any_data, recv_dev)

                # 判断是否接收完毕
                if len(recv_data) < 516:
                    print('----下载完成----')
                    recv_file.flush()
                    recv_file.close()
                    break

            elif recv_type == 5:
                print('----未找到你要下载的文件----')
                break


class UploadServer(BaseServer):
    """
        tftp协议上传类
    """

    def upload(self, file_name):

        self.creat_tftp()

        if not os.path.exists(file_name):
            print('----请输入一个存在的文件或文件夹----')
        # 发送上传请求
        fmt = '!H%dsb5sb' % len(file_name)
        a = (2, bytes(file_name, encoding='utf-8'), 0, bytes('octet', encoding='utf-8'), 0)
        send_data = struct.pack(fmt, *a)
        self.tftp.sendto(send_data, (self.appoint_ip, self.appoint_port))

        send_file = None
        p_num = 0
        while True:
            recv_data, recv_dev = self.tftp.recvfrom(1024)
            recv_type, recv_page = struct.unpack('!HH', recv_data[:4])
            print('----收到的回应：%s,%s' % (str(recv_type), str(recv_page)))
            if recv_type == 4:
                if send_file is None:
                    send_file = open(file_name, 'br+')
                ret = send_file.read(512)
                # 避免重复上传数据包
                if p_num == recv_page:
                    p_num += 1
                    any_data = struct.pack('!HH', 3, p_num)
                    self.tftp.sendto(any_data + ret, recv_dev)

                if len(ret) < 512:
                    print('----上传成功----')
                    send_file.close()
                    break

                pass
            elif recv_type == 5:
                print('----上传失败----')
                send_file.close()
                break




def f1():
    d_server = DownloadServer('', 7788)
    d_server.set_appoint('172.21.150.1', 69)
    d_server.download('test.pdf')


def f2():
    up_server = UploadServer('', 7788)
    up_server.set_appoint('172.21.150.1', 69)
    up_server.upload('用面向对象的方式实现下载.py')
    pass


def main():
    # f1()
    f2()
    pass


if __name__ == '__main__':
    main()
