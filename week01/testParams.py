# -*- coding:utf-8 -*-

def testParam01(n=5):
    print('传过来的参数是：%s' % n)


def testParam02(a, b=22, c=44):
    result = a + b
    print(a)
    print(b)
    print(c)
    print('result=%d' % result)


def testParam03(a, b, *args):
    print(a)
    print(b)
    print(args)


def testParam04(*a, b, c):
    print(a)
    print(b)
    print(c)
    pass


def testParam05(a, b, c=33, *args):
    print(a)
    print(b)
    print(c)
    print(args)


def testParam06(a, b, c=33, **kwargs):
    print(a)
    print(b)
    print(c)
    print(kwargs)
    print(type(kwargs))
    pass


def sum(a, b, *args):
    result = a + b
    for n in args:
        result += n
    return result


def testParam07(a, *args, b=20, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    print(kwargs['name'])
    pass


def main():
    # testParam01(n=4)
    # testParam02(b=11, c=10, a=33)
    # testParam03(1, 2, 3, 4, 5, 6, 7)
    # testParam04(b=6, c=7)
    # print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9))
    # testParam05(11, 22, 33, 44, 55)
    # testParam06(11, 22, task=33, down=55)
    # help(print)
    A = (11, 22, 33)
    B = {'name': 'laowang', 'args': 17}
    testParam07(22, *A, **B)
    pass


if __name__ == '__main__':
    main()
