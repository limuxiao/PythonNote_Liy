# -*- coding:utf-8 -*-
import week02.TestZhuangshiqi as TZ
from week02.TestZhuangshiqi.liy import ZSQ


def test01():
    zsq = ZSQ()
    TZ.liy.ZSQ()


@ZSQ.check()
def test02():
    print('----test02----')


def main():
    # test01()
    test02()
    pass


if __name__ == '__main__':
    main()
