# -*- coding:utf-8 -*-
from collections import Iterable, Iterator


def test01():
    print(isinstance([], Iterable))
    print(isinstance([], Iterator))
    a = [11, 22, 33, 44]
    b = iter(a)
    print(isinstance(a, Iterator))
    print(isinstance(b, Iterator))
    print(isinstance(b, Iterable))
    print(isinstance((i for i in range(10) if i % 2 == 0), Iterator))
    b = [i for i in range(10)]
    b = (i for i in range(10))
    print(type(a))
    print(type(b))
    print(next(b))
    print(next(b))
    pass


def test02():
    a = (1, 2, 3, 4)
    print(isinstance(a, Iterator))


def main():
    # test01()
    test02()
    pass


if __name__ == '__main__':
    main()
