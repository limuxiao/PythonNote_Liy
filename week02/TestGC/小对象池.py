# -*- coding:utf-8 -*-


def test01():
    a = 10
    b = 10
    print(id(a))
    print(id(b))
    c = 10000
    d = 10000
    print(id(c))
    print(id(d))


def main():
    test01()
    pass


if __name__ == '__main__':
    main()
