# -*- coding:utf-8 -*-
import week02.测试装饰器 as TZ
from week02.测试装饰器.liy import ZSQ
import sys
import os


def test01():
    zsq = ZSQ()
    TZ.liy.ZSQ()


@ZSQ.check02
def test02(a):
    print('----test02 a = %d----' % a)
    return a


@ZSQ.check02
def test03():
    print('----test03----')


def main():
    # test01()
    # print(test02(11))
    test03()
    # print(sys.path)
    # print(os.getcwd())
    pass


if __name__ == '__main__':
    main()
