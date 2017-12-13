# -*- coding: utf8 -*-
import sys
from week03.测试websocket.server import SocketServer
from week03.测试websocket.BaseIO import BaseIO


class MyIO(BaseIO):

    def __init__(self):
        print('----MyIO init----')
        super().__init__()

    def onData(self, uid, text):
        self.sendData(uid, "我收到了你的消息：%s" % (text,))

    def onConnect(self, uid):
        self.sendData(uid, "你已经成功连接上我了！")


def main():
    try:
        port = sys.argv[1]
    except:
        port = 8181

    port = int(port)
    myIo = MyIO()
    SocketServer(port, myIo).run()
    pass


if __name__ == '__main__':
    sys.argv = ['', 88]
    main()
