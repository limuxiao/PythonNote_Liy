# -*- coding:utf-8 -*-


def f1():
    """
        这是最简单的用type方法来创建类
    :return:
    """
    Bird = type('Bird', (), {'name': 'haha'})
    bird1 = Bird()
    print(Bird.name)
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()