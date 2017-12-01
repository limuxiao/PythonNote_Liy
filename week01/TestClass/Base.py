# -*- coding:utf-8 -*-

class Base(object):
    def __init__(self):
        print('----Base init----')

    def get_base(self):
        return 'Base'

    def test(self):
        print('----Base test----')

    @classmethod
    def test_class_method(cls):
        print('----Base class method----')

    @staticmethod
    def test_static_method():
        print('----Base static method----')


class A(Base):
    def __init__(self):
        print('----A init----')

    def test(self):
        print('----A test----')


class B(Base):
    def __init__(self):
        print('----B init----')

    def test(self):
        print('----B test----')

class C(A, B):

    def test(self):
        B.test(self)
        print('----C test----')


def main():
    c = C()
    # print(C.__mro__)
    # C.test_class_method()
    c.test()
    pass


if __name__ == '__main__':
    main()
