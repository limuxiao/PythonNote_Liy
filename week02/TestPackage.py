# -*- coding:utf-8 -*-

from week02.TestMsg import *
from week02 import TestMsg


def testPackage01():
    print(SendMsg.test())
    print(RecvMsg.test())
    TestMsg.SendMsg.test()
    TestMsg.RecvMsg.test()
    print('----')


def main():
    testPackage01()
    pass


if __name__ == '__main__':
    main()