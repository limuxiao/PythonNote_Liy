# -*- coding:utf-8 -*-


def decorator(fn):
    """
        这是一个通用方法装饰器，可以用来装饰无参无返回值、无参有返回值、有参无返回值、有参有返回值的方法
    :param fn:
    :return:
    """
    def inner(*args, **kwargs):
        print('----inner----')
        return fn(*args, **kwargs)
    return inner


@decorator
def f1():
    print('----f1----')


@decorator
def f2(*args, **kwargs):
    print('----f2----')
    print('args:%s\nkwargs:%s' % (args, kwargs))


@decorator
def f3():
    print('----f3----')
    return 20


@decorator
def f4(*args, **kwargs):
    print('----f4----')
    print('args:%s\nkwargs:%s' % (args, kwargs))
    return args[0]


def main():
    # f1()
    a = [1, 2, 3, 4]
    b = {'name': 'laowang', 'age': 18}
    # f2(*a, **b)
    # print(f3())
    print(f4(*a, **b))
    pass


if __name__ == '__main__':
    main()