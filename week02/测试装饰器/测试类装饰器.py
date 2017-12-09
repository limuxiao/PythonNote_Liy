# -*- coding:utf-8 -*-


def decorator(cls):
    class New_Class:
        def __init__(self):
            print('----new class __init__----')
        pass
    return New_Class


@decorator
class Bird(object):
    def __init__(self, name):
        print('----bird class __init__----')
        self.__name = name

    def get_name(self):
        return self.__name


def f1():
    bird = Bird()
    print(bird.get_name())

def main():
    f1()


if __name__ == '__main__':
    main()
