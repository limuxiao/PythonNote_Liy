# -*- coding:utf-8 -*-


instance = {}


def singleton(cls):
    def inner(*args):
        if cls not in instance:
            instance[cls] = cls(*args)
        return instance[cls]
    return inner


@singleton
class Bird:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


def f1():
    bird1 = Bird('haha')
    bird2 = Bird('hehe')
    print(id(bird1))
    print(id(bird2))
    print(bird1.__class__)
    print(bird2.__class__)
    print(bird1.get_name())
    print(bird2.get_name())


def main():
    f1()
    pass


if __name__ == '__main__':
    main()