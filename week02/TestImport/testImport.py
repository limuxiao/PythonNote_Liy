# -*- coding:utf-8 -*-
import sys
import copy


def test01():
    """
        测试 == 和 is
    :return:
    """
    a = [11, 22, 33]
    b = [11, 22, 33]
    c = a
    print(a == b)
    print(a is b)
    print(a == c)
    print(a is c)

    d = 100
    f = 100
    print(d is f)
    g = 10000
    i = 10000
    print(g is i)

    a = 10000
    b = 10000
    print(a == b)


def test02():
    """
        测试深拷贝和浅拷贝
    :return:
    """
    # 浅拷贝
    a = [11, 22, 33]
    b = a
    print(a is b)
    print(id(a))
    print(id(b))
    # 深拷贝
    c = copy.deepcopy(a)
    print(a is c)
    print(id(c))

    d = copy.copy(a)
    print(id(d))
    print(a is d)
    a.append(44)
    print(a)
    print(b)
    print(c)
    print(d)

    a = [11, 22]
    b = [33, 44]
    c = [a, b]
    d = c
    print(c is d)
    e = copy.deepcopy(c)
    print(c is e)
    f = copy.copy(c)
    print(c is f)
    a.append(66)
    print(c)
    print(e)
    print(f)


def test03():
    """
        测试深拷贝和浅拷贝
    :return:
    """
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = (a, b)
    d = copy.copy(c)
    e = copy.deepcopy(c)
    print(id(c))
    print(id(d))
    print(id(e))


def test04():
    pass


def main():
    # print(sys.path)
    # test01()
    # test02()
    test03()
    pass


if __name__ == '__main__':
    main()
