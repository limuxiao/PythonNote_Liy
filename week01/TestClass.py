# -*- coding:utf-8 -*-
from week01.Cat import Cat


def testClass01():
    c = Cat()
    c.test()
    c.sleep()
    c.name = 'Tom'
    c.printName()
    pass


def main():
    testClass01()
    pass


if __name__ == '__main__':
    main()
