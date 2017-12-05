# -*- coding:utf-8 -*-
class Test(object):

    _＿name = None

    def __init__(self):
        self.__num = 5
        self.__money = 20
        self._type = 'A'

    def test_num(self):
        print(self.__num)

    def set_num(self, num):
        print('----setter----')
        self.__num = num

    def get_num(self):
        print('----getter----')
        return self.__num

    @property
    def money(self):
        print('----get money----')
        return self.__money

    @money.setter
    def money(self, money):
        print('----set money----')
        self.__money = money

    def __del__(self):
        print('----del----')

    num = property(get_num, set_num)


class A(Test):

    def get_type(self):
        return self._type

    def __del__(self):
        print('----A del----')


def test01():
    t = Test()
    t.__num = 6
    print(t.__num)
    t.test_num()


def test02():
    a = A()
    print(a.get_type())
    print(dir(a))
    a.num = 20
    print(a.num)
    a.money = 200
    print(a.money)


def main():
    # test01()
    test02()
    pass


if __name__ == '__main__':
    main()
