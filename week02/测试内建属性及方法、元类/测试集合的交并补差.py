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

    b.add(3)
    b.add(5)
    b.add(10)

    print(a & b)
    print(a | b)
    print(a ^ b)
    print(a - b)
    print(b ^ a)
    print(b - a)
    print()


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
