# -*- coding:utf-8 -*-
instances = {}  # 全局变量，管理实例


def decorator(cls):
    class New_Class:
        def __init__(self):
            print('----new class __init__----')

        pass

    return New_Class


def getInstance(aClass, *args):
    if aClass not in instances:
        instances[aClass] = aClass(*args)
    return instances[aClass]  # 每一个类只能存在一个实例


def singleton(cls):
    def on_call(*args):
        return getInstance(cls, *args)

    return on_call


@decorator
class Bird(object):
    def __init__(self, name):
        print('----bird class __init__----')
        self.__name = name

    def get_name(self):
        return self.__name


@singleton
class Person(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


def f1():
    bird = Bird()
    # print(bird.get_name())
    print(bird.__class__)


def f2():
    p1 = Person('朗照')
    p2 = Person('哈哈')
    print(p1.get_name())
    print(p2.get_name())
    print(id(p1))
    print(id(p2))
    print(help(Person.__bases__))

def main():
    # f1()
    f2()


if __name__ == '__main__':
    main()
