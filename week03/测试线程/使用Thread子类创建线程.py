# -*- coding:utf-8 -*-
from threading import Thread
import time


class MyThread(Thread):

    def run(self):
        for i in range(5):
            print('----%d----' % i)
            time.sleep(1)


def f1():
    # help(Thread)
    mt_one = MyThread()
    mt_two = MyThread()
    mt_one.start()
    mt_two.start()

    for i in range(5):
        print('----haha----')
        time.sleep(1)


def f2():
    print(MyThread.__dict__)
    mt = MyThread()
    print(mt.__dict__)


def main():
    # f1()
    f2()


if __name__ == '__main__':
    main()
