# -*- coding:utf-8 -*-
class Person:
    __doc__ = """
        人类
    """

    # __dict__ = {'name': 'laowang', 'age': 18, 'gender': 'man'}

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, item):
        print('----调用__getattribute__----item:%s' % item)
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print('----调用__setattr__----')
        print('key:%s, value:%s' % (key, value))
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print('----调用__getattr__----')

    def show(self):
        return '%s,%d' % (self.name, self.age)


def f1():
    p1 = Person('laowang', 18)
    # print(p1.name)
    # p1.gender = 'man'
    # print(p1.gender)
    print(p1.show())


def f2():
    print(dir(Person))
    p1 = Person('老赵', 20)
    print(p1.__class__)
    print(p1.__dict__)
    # print(help(Person))
    print(p1.__class__.__bases__)
    print(Person.__bases__)
    print(Person.__dict__)
    print(hasattr(p1, 'name'))


def main():
    # f1()
    f2()


if __name__ == '__main__':
    main()
