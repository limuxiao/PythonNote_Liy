# -*- coding:utf-8 -*-


def decorator(fn):
    """
        这是一个简单的装饰器，只能用来装饰无参无返回值的函数。
    :param fn:
    :return:
    """
    def inner():
        print('----inner----')
        fn()
    return inner


# 当被装饰器装饰后，会执行装饰器的方法
@decorator
def f1():
    print('----f1----')


def main():
    f1()
    pass


if __name__ == '__main__':
    main()