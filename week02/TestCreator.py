# -*- coding:utf-8 -*-
import time

def createNum(max):
    for i in range(max):
        if i == max:
            has_next = False
        yield i


def test01():
    a = createNum()
    # print(next(a))
    # print(a.__next__())
    print(type(a))
    for n in a:
        print(n)
    pass


def test_a():
    while True:
        print('----testA----')
        yield None


def test_b():
    while True:
        print('----testB----')
        yield None


def test_c():
    i = 0
    while i < 10:
        time.sleep(1)
        next(test_a())
        next(test_b())
        i += 1


def main():
    # test01()
    test_c()
    pass


if __name__ == '__main__':
    main()
