# -*- coding:utf-8 -*-
import socket


def f1():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('www.ule.com', 80))
    req_start = 'GET / HTTP/1.1\r\n'
    req_header = 'Host: 14.215.177.38\r\n'
    req_header += 'Connection: keep-alive\r\n'
    req_header += 'Cache-Control: max-age=0\r\n'
    req_header += 'Upgrade-Insecure-Requests: 1\r\n'
    req_header += 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36\r\n'
    req_header += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n'
    req_header +='Accept-Encoding: gzip, deflate, sdch\r\n'
    req_header += 'Accept-Language: zh-CN,zh;q=0.8\r\n'
    # req_header += 'Cookie: BD_HOME=0; __guid=13969463.1713991288051555300.1514342901813.8586; monitor_count=1; BD_UPN=12314353\r\n'
    data = req_start + req_header
    sock.send(bytes(data, encoding='utf-8'))
    ret = sock.recv(10240)
    print('----收到的内容是：%s----' % str(ret))
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
