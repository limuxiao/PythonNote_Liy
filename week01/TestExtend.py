# -*- coding:utf-8 -*-

class A:
    def __init__(self):
        self.num = 100
        self.__num = 200

    def test01(self):
        print('----test01----')

    def __test02(self):
        print('----test02----')

    def test03(self):
        self.__test02()

class B(A):

    def __init__(self):
        super().__init__()

    pass


def main():
    b = B()
    print(b.num)
    # print(b.__num)        不能访问父类的私有属性
    b.test01()
    # b.__test02()          不能访问父类的私有方法
    b.test03()
    pass


if __name__ == '__main__':
    main()
