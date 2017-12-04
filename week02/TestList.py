# -*- coding:utf-8 -*-

import sys


def testList01():
    a = [i for i in range(10)]
    print(a)
    b = [(i, j) for i in range(3) for j in range(4, 6)]
    print(b)
    c = [i for i in range(10) if i % 2 == 0]
    print(c)
    d = [i for i in range(10) if i % 2 == 0]
    print(d)
    pass


def main():
    a = sys.argv
    print(a)
    testList01()
    pass


if __name__ == '__main__':
    main()
