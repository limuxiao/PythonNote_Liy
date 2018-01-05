# -*- coding:utf-8 -*-


class A:
    def __init__(self):
        self.a = 100


class B(A):
    pass


class C(A):
    def __init__(self):
        super().__init__()
        self.a = 200
    pass


class D(B, C):
    pass


def f1():
    d = D()
    print(d.a)


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
