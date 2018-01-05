# -*- coding:utf-8 -*-
from timeit import Timer


def test01():
    li = []
    for i in range(10000):
        li.append(i)


def f1():
    timer1 = Timer('test01', 'from __main__ import test01')
    print('append:', timer1.timeit(1000))
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
