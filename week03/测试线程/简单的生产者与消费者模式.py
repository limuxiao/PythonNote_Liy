# -*- coding:utf-8 -*-
from threading import Thread
from queue import Queue


class Factory(Thread):
    """
        工厂类
    """
    def __init__(self, queue):
        self.__queue = queue
    pass


class Producer(Factory):
    """
        生产者类
    """

    def run(self):
        super().run()


class Consumer(Factory):
    """
        消费者类
    """

    def run(self):
        super().run()


def f1():
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
