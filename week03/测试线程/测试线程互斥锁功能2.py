# -*- coding:utf-8 -*-
from threading import Thread, Lock
import time


g_num = 0
mutex = Lock()


def work01():
    global g_num
    start_time = time.time() * 1000
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()
    end_time = time.time() * 1000
    print('----work01 : g_num=%d---' % g_num)
    print('----work01耗时：%s----' % str(end_time - start_time))


def work02():
    global g_num
    start_time = time.time() * 1000
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()
    end_time = time.time() * 1000
    print('----work02 : g_num=%d---' % g_num)
    print('----work02耗时：%s----' % str(end_time - start_time))


def work03():
    global g_num
    start_time = time.time() * 1000
    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    end_time = time.time() * 1000
    print('----work03 : g_num=%d---' % g_num)
    print('----work03耗时：%s----' % str(end_time - start_time))


def work04():
    global g_num
    start_time = time.time() * 1000
    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    end_time = time.time() * 1000
    print('----work03 : g_num=%d---' % g_num)
    print('----work03耗时：%s----' % str(end_time - start_time))


def f1():
    t1 = Thread(target=work01)
    t2 = Thread(target=work02)
    t1.start()
    t2.start()
    # time.sleep(3)
    print('----主线程 : g_num=%d---' % g_num)


def f2():
    # help(time)
    # print(time.time())
    t1 = Thread(target=work03)
    t2 = Thread(target=work04)
    t1.start()
    t2.start()
    # time.sleep(3)
    print('----主线程 : g_num=%d---' % g_num)


def main():
    # f1()
    f2()
    pass


if __name__ == '__main__':
    main()
