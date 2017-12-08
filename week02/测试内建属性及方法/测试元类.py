# -*- coding:utf-8 -*-

Foo = type('Foo', (), {})

class MySun(object):

    pass

def create_class():
    pass


def f1():
    # create_class()
    Foo = type('Foo', (), {'name': 'laowang'})
    f = Foo()
    print(Foo.name)
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
