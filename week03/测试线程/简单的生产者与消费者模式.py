# -*- coding:utf-8 -*-
import threading
from threading import Thread
from queue import Queue
import time


class Factory(Thread):
    """
        工厂类
    """
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
    pass


class Producer(Factory):
    """
        生产者类
    """

    def run(self):
        while True:
            if self.queue.qsize() < 1000:
                print('----需要生产----生产线程id:%s----生产产品id:%d----' % (threading.current_thread().name, self.queue.qsize()+1))
                self.queue.put(self.queue.qsize() + 1)
                time.sleep(0.1)
            else:
                print('----不需要生产----生产线程id:%s----' % threading.current_thread().name)
                time.sleep(0.5)


class Consumer(Factory):
    """
        消费者类
    """

    def run(self):
        while True:
            if self.queue.qsize() > 100:
                print('----可以消费----消费线程id:%s----消费产品id:%d----' % (threading.current_thread().name, self.queue.get()))
                time.sleep(0.2)
            else:
                print('----不可以消费----消费线程id:%s----' % threading.current_thread().name)
                time.sleep(0.5)


def f1():
    queue = Queue()
    for i in range(5):
        p = Producer(queue)
        p.start()
    for i in range(3):
        c = Consumer(queue)
        c.start()


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
