# -*- coding:utf-8 -*-



def testParam01(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    pass


def testParam02():
    pass


def main():
    a = 10,
    b = 20,
    A = (11, 22, 33)
    B = {'name': 'laowang', 'age': 16}
    testParam01(a, b, *A, **B)
    pass


if __name__ == '__main__':
    main()
