# -*- coding:utf-8 -*-


def createNum(max):
    for i in range(max):
        if i == max:
            has_next = False
        yield i


def test01():
    a = createNum()
    # print(next(a))
    # print(a.__next__())
    print(type(a))
    for n in a:
        print(n)
    pass


def main():
    test01()
    pass


if __name__ == '__main__':
    main()
