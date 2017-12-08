# -*- coding:utf-8 -*-
import functools


def f1():
    for l in dir(functools):
        print(l)


def test(*args, **kwargs):
    print(args)
    print(kwargs)


def f2():
    p1 = functools.partial(test, 1, 2, 3)
    p1()
    print('-' * 50)
    p1(25, name='haha', age=18)


def main():
    # f1()
    f2()
    pass


if __name__ == '__main__':
    main()
