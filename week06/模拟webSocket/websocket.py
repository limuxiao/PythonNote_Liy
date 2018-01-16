# -*- coding:utf-8 -*-
import socket
from threading import Thread
import hashlib
import base64


class ClientThread(Thread):

    def __init__(self, client_sock):
        super().__init__()
        self.client_sock = client_sock

    def run(self):
        ret = self.client_sock.recv(1024)
        # print('收到的结果:%s' % str(ret, 'utf-8'))
        headers = self.parse_headers(str(ret, 'utf-8'))
        token = self.generate_token(headers['Sec-WebSocket-Key'])
        result = 'HTTP/1.1 101 WebSocket Protocol Hybi-10\r\n'
        result += 'Upgrade: WebSocket\r\n'
        result += 'Connection: Upgrade\r\n'
        result += 'Sec-WebSocket-Accept: %s\r\n\r\n' % str(token, 'utf-8')
        # print("服务器返回：%s" % str(result))
        self.client_sock.send(bytes(result, 'utf-8'))

        recv_b = bytes('4321', encoding='utf-8')
        recv_last = [0x81, 0x4]
        for r in recv_b:
            recv_last.append(r)
        self.client_sock.send(bytes(recv_last))

        while True:
            try:
                data = self.client_sock.recv(1024)

                if len(data) > 0:

                    if data[0] == 0x88:
                        break

                    real_data = self.parse_data(data)
                    print(str(real_data, 'utf-8'))

                else:
                    self.client_sock.close()
                    print('关闭连接')
                    break

            except socket.error as e:
                print('异常', e)


    def generate_token(self, msg):
        key = msg + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
        ser_key = hashlib.sha1(bytes(key, encoding='utf-8')).digest()
        return base64.b64encode(ser_key)

    def parse_headers(self, msg):
        headers = {}
        header, data = msg.split('\r\n\r\n', 1)
        for line in header.split('\r\n')[1:]:
            key, value = line.split(': ', 1)
            headers[key] = value
        headers['data'] = data
        return headers

    def parse_data(self, msg):
        v = msg[1] & 0x7f
        if v == 0x7e:
            p = 4
        elif v == 0x7f:
            p = 10
        else:
            p = 2
        mask = msg[p:p + 4]
        data = msg[p + 4:]
        b = bytes([v ^ mask[k % 4] for k, v in enumerate(data)])
        return b


class WebSocket(object):
    def __init__(self, port):
        self.sock = None
        self.port = port
        pass

    def start(self):
        if self.sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind(('', self.port))
            self.sock.listen(5)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        while True:
            client_sock, client_addr = self.sock.accept()
            ClientThread(client_sock).start()


def f1():
    ws = WebSocket(7788)
    ws.start()


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
