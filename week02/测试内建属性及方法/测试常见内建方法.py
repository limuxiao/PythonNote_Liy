# -*- coding:utf-8 -*-
from collections import Iterator, Iterable


def f1():
    print(dir(__builtins__))
    a = dir(__builtins__)
    print(len(a))
    # help(range)
    # help(repr)
    a = range(5)
    print(isinstance(a, Iterator))
    print(isinstance(a, Iterable))


def f2():
    a = map(test_map, [1, 2, 3])
    print(type(a))
    print(isinstance(a, Iterator))
    # for n in a:
    #     print(n)
    print(next(a))
    print(next(a))
    print(next(a))
    # print(next(a))


def test_map(num):
    return num + 2


def main():
    # f1()
    f2()
    pass


if __name__ == '__main__':
    main()
