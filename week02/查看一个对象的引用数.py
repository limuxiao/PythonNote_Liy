# -*- coding:utf-8 -*-
import sys


class Dog:
    def __init__(self):
        pass

    def __del__(self):
        print('----Dog del----')


def test01():
    a = Dog()
    b = a
    print(sys.getrefcount(b))
    a = Dog()
    print(sys.getrefcount(b))
    print(id(a))
    print(id(b))

def test02():
    a = 100
    print(sys.getrefcount(a))
    dog1 = Dog()
    print(sys.getrefcount(dog1))
    dog2 = Dog()
    dog1 = dog2
    print(sys.getrefcount(dog1))


def main():
    test01()


if __name__ == '__main__':
    main()
