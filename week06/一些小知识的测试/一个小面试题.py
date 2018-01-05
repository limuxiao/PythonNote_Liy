# -*- coding:utf-8 -*-
import sys


class Foo(object):
    """
        实现一个类，可以无限点下去，
        例如：调用print（Foo().think.different.itcast）
        打印结果为：think different itcast
    """
    def __init__(self):
        pass

    def __getattr__(self, item):
        print(item, end=' ')
        return self

    def __setattr__(self, key, value):
        print('----set attr----')
        self.__dict__[key] = value

    def __getattribute__(self, item):
        print('----get attribute----')
        return super().__getattribute__(item)

    def __str__(self):
        return ''


def f1():
    # print(Foo().think.different.itcast)
    # print(Foo().__repr__())
    foo = Foo()
    foo.name = 'haha'
    # print(foo.name)


def main():
    print(sys.argv)
    f1()
    pass


if __name__ == '__main__':
    main()
