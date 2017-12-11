# -*- coding:utf-8 -*-
from multiprocessing import Process
import time


class MyProcess(Process):

    def run(self):
        for i in range(10):
            print('----%d----' % i)
            time.sleep(1)


def f1():
    p = MyProcess()
    p.start()
    p.join()
    print('----子进程结束----')
    pass


def main():
    f1()


if __name__ == '__main__':
    main()
