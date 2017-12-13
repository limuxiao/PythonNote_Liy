# -*- coding: utf8 -*-

import socket
import time
from threading import Thread
import hashlib
import base64


class returnCrossDomain(Thread):
    def __init__(self, connection):
        Thread.__init__(self)
        self.con = connection
        self.isHandleShake = False

    def run(self):
        while True:
            if not self.isHandleShake:  # 握手
                clientData = self.con.recv(1024)
                clientData = str(clientData)
                dataList = clientData.split("\\r\\n")
                header = {}
                for i in dataList:
                    print(i)
                clientData
                for data in dataList:
                    if ": " in data:
                        unit = data.split(": ")
                        header[unit[0]] = unit[1]
                secKey = header['Sec-WebSocket-Key']
                # resKey = base64.encodestring(
                #     hashlib.new("sha1", secKey + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").digest()).replace('\n', '')

                resKey = secKey

                response = '''''HTTP/1.1 101 Switching Protocols\r\n'''
                response += '''''Upgrade: websocket\r\n'''
                response += '''''Connection: Upgrade\r\n'''
                response += '''''Sec-WebSocket-Accept: %s\r\n''' % (resKey,)
                response += '''''Sec-WebSocket-Protocol: chat\r\n\r\n'''
                print('----准备返回----')
                self.con.send(response.encode(encoding='utf-8'))
                self.isHandleShake = True
            else:
                data = self.con.recv(1024)
                print('得到的消息：%s' % str(data))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 8889))
    sock.listen(100)
    while True:
        try:
            connection, address = sock.accept()
            returnCrossDomain(connection).start()
        except:
            time.sleep(1)


if __name__ == "__main__":
    main()
