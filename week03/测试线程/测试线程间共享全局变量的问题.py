# -*- coding:utf-8 -*-
from threading import Thread
import time


g_num = 0


def work01():
    global g_num
    for i in range(1000000):
        g_num += 1
    print('----work01 : g_num=%d---' % g_num)


def work02():
    global g_num
    for i in range(1000000):
        g_num += 1
    print('----work02 : g_num=%d---' % g_num)


def f1():
    t1 = Thread(target=work01)
    t2 = Thread(target=work02)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # time.sleep(3)
    print('----主线程 : g_num=%d---' % g_num)


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
