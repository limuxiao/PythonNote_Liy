# -*- coding:utf-8 -*-
from multiprocessing import Process
import time
import os


def test():
    for i in range(10):
        print('----%d----' % i)
        time.sleep(1)


def f1():
    p = Process(target=test)
    p.start()

    # time.sleep(6)
    # p.terminate()  # 直接结束子进程

    # help(p.join)
    p.join(timeout=4)        # 中断主进程，等待子进程，等子进程结束后才会在主进程中打印，如果不等待则主进程不会中断，直接打印
    print('----子进程结束----')

    # help(Process)
    pass


def f2():
    """
        测试fork，os.fork()在window系统上不可用
    :return:
    """
    ret = os.fork()
    print(ret)


def main():
    f1()
    # f2()


if __name__ == '__main__':
    main()