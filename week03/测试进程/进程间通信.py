# -*- coding:utf-8 -*-
from multiprocessing import Queue, Process
import time


q = Queue(3)


def put_msg(q):
    print('----q size:%d----' % q.qsize())
    # help(q)
    q.put('haha')
    print('----q size:%d----' % q.qsize())


def get_msg(q):
    time.sleep(5)
    print('----q size:%d----' % q.qsize())
    ret = q.get()
    print('----q size:%d----' % q.qsize())
    print('----%s----' % str(ret))


def f1():
    p = Process(target=put_msg, args=(q,))
    p.start()
    p.join()


def f2():
    p = Process(target=get_msg, args=(q,))
    p.start()
    p.join()


def main():
    f1()
    f2()
    pass


if __name__ == '__main__':
    main()