# -*- coding:utf-8 -*-
class SingleTon:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        print('----init----')


def main():
    a = SingleTon()
    b = SingleTon()
    print(id(a))
    print(id(b))
    pass


if __name__ == '__main__':
    main()
