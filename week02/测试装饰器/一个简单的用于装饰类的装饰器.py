# -*- coding:utf-8 -*-


def decorator(cls):
    """
        这是一个简单的类装饰器，它将所有的自定义属性都转为大写
    :param cls:
    :return:
    """
    def inner(*args, **kwargs):
        # print(cls.__dict__)
        instance = cls(*args, **kwargs)
        # print(instance.__dict__)
        for item in instance.__dict__.items():
            # print(item)
            instance.__dict__[item[0]] = str(item[1]).upper()
        return instance
    return inner


@decorator
class Bird:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


def f1():
    bird = Bird('haha')
    print(bird.get_name())


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
