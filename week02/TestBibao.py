# -*- coding:utf-8 -*-


def test01(num1):
    print("----test01----")
    def test(num2):
        return num1 + num2

    return test


def test02():
    fun1 = test01(100)
    fun2 = test01(1)
    print(fun1(100))
    print(id(fun1))
    print(id(fun2))
    a = test01
    b = test01
    print(a == b)
    print(a is b)
    print(id(a))
    print(id(b))


def test03(func):

    def inner(num=0):
        print('----test03----')
        func(num)
        print('----inner----')
    return inner


@test03
def test04():
    print('----test04----')


@test03
def test05(num):
    print('----test05----%d' % num)


def test06(func):

    def inner():
        print('----test06----')
        func()
    return inner


def test07():
    print('----test07----')


def main():
    # test02()
    # test03()
    # test04()
    test05(50)
    # test07()
    # test07()
    # a = test06(test07)
    # a()
    pass


if __name__ == '__main__':
    main()
    # test07 = test06(test07)
    # test07()
