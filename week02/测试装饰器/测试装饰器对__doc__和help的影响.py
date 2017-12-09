# -*- coding:utf-8 -*-
import functools


def decorator(func):
    """
        声明了一个简单的装饰器
    :return:
    """

    @functools.wraps(func)
    def inner(*args, **kwargs):
        """
            装饰器inner方法
        :param args:
        :param kwargs:
        :return:
        """
        print('*args:%s' % args)
        print('**kwargs:%s' % kwargs)
        return func(args, kwargs)

    return inner


@decorator
def f1():
    """
        这个是被装饰的函数
    :return:
    """
    print('----f1----')


def f2():
    # 通过测试发现：
    # 当一个函数被装饰器装饰之后，在没有使用functools.wraps(func)方法装饰时,
    # 它的__doc__属性会装饰器的__doc__覆盖;
    # 通过help()方法查看看到的也是装饰器的。
    #

    # help(f1)
    print(f1.__doc__)


def main():
    f2()
    pass


if __name__ == '__main__':
    main()
