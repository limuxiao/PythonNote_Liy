# -*- coding:utf-8 -*-
from multiprocessing import Pool
import os
import time


def test():
    for i in range(3):
        print(os.getpid())
        print('----test----%d' % i)
        time.sleep(1)


def f1():
    # 使用Pool的apply_async方法添加的进程，这种方式为非堵塞的
    # 即
    pool = Pool(3)
    for i in range(10):
        pool.apply_async(test)
    pool.close()
    pool.join()
    print('----pool over----')


def f2():
    # 使用Pool的apply方法添加进程，这种方式是堵塞的
    # 即 通过这种方式添加的，下一个进程要等到上一个进程执行完毕之后才开始
    pool = Pool(3)
    for i in range(10):
        pool.apply_async(test)
    pool.close()
    pool.join()
    print('----pool over----')


def main():
    f2()
    pass


if __name__ == '__main__':
    main()
