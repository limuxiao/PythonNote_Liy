# -*- coding:utf-8 -*-


def f1():
    a = [i for i in range(10)]
    print(a)
    b = a[::2]
    print(b)
    a = set(a)
    b = set(b)
    print(type(a))
    print(type(b))

    b.

    print(a & b)
    print()


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
