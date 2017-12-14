# -*- coding:utf-8 -*-
from threading import Thread, Lock
import time


g_num = 0
mutex = Lock()


def work01():
    global g_num
    # 这个线程和work02线程都在抢着　对这个锁　进行上锁，如果有１方成功的上锁，那么导致另外
    # 一方会堵塞（一直等待）到这个锁被解开为止
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    # 用来对mutex指向的这个锁　进行解锁，，，只要开了锁，那么接下来会让所有因为
    # 这个锁　被上了锁　而堵塞的线程　进行抢着上锁
    mutex.release()
    print('----work01 : g_num=%d---' % g_num)


def work02():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()
    print('----work02 : g_num=%d---' % g_num)


def f1():
    t1 = Thread(target=work01)
    t2 = Thread(target=work02)
    t1.start()
    t2.start()
    # time.sleep(3)
    print('----主线程 : g_num=%d---' % g_num)


def f2():
    help(mutex)


def main():
    f1()
    # f2()
    pass


if __name__ == '__main__':
    main()
