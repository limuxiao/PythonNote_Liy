# -*- coding:utf-8 -*-
import types


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass


def test01():
    # print(globals())
    num = 10
    print(locals())


def test02():
    p1 = Person('p1', 20)
    print(p1.name)
    print(p1.age)
    p1.address = '背景'
    print(p1.address)
    # help(types.MethodType)
    p1.get_address = types.MethodType(get_address, p1)
    print(p1.get_address())
    Person.get_person = get_person
    print(Person.get_person())
    print(p1.get_person())
    Person.load_person = load_person
    Person.load_person()

@classmethod
def get_person(cls):
    return 'hha '


@staticmethod
def load_person():
    print('----load person----')


def get_address(self):
    return self.address


def main():
    # test01()
    test02()
    pass


if __name__ == '__main__':
    main()
