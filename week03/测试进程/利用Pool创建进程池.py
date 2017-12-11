# -*- coding:utf-8 -*-
from multiprocessing import Pool
import time
import os


def pool_test(n):
    print('----n=%d----pid:%d' % (n, os.getpid()))
    time_start = time.time()
    for i in range(5):
        print('----%d----' % i)
        time.sleep(1)
    time_end = time.time()
    print('----%d----耗时：%d' % (n, time_end - time_start))


def f1():
    pool = Pool(3)
    for i in range(10):
        pool.apply_async(pool_test, (i,))
    pool.close()
    ret = pool.join()
    print('----进程池执行完毕----')


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
