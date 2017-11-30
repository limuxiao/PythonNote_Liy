# -*- coding:utf-8 -*-
from week01.Cat import Cat


def testClass01():
    c = Cat(age=20, name='Tom')
    c.test()
    c.sleep()
    print(c.getName())
    print(c.getAge())
    c.setName('Hehe')
    c.setAge(365)
    print(c.getName())
    print(c.getAge())
    print(c)

    a = Cat(name='LanMao', age=15)
    print(a)
    pass


def main():
    testClass01()
    pass


if __name__ == '__main__':
    main()
