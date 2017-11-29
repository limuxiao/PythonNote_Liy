# -*- coding:utf-8 -*-


def testJie(n):
    if n <= 0:
        return
    elif n == 1:
        return 1
    else:
        return n * testJie(n-1)
    pass


def testD():
    testD()
    pass


def main():
    # print(testJie(8))
    # testD()
    pass


if __name__ == '__main__':
    main()
