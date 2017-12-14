# -*- coding:utf-8 -*-
from threading import Thread
import time


a = 100


def set_a(val):
    global a
    a = val


def get_a():
    global a
    print('----a=%d----' % a)
    return a


def f1():
    t = Thread(target=set_a, args=(200,))
    t.start()
    t.join()
    pass


def f2():
    time.sleep(2)
    t = Thread(target=get_a)
    t.start()
    t.join()
    pass


def main():
    f1()
    f2()
    # 通过测试发现，线程可以共享全局变量
    pass


if __name__ == '__main__':
    main()
