# -*- coding:utf-8 -*-
from threading import Thread
import time


def print_say():
    print('----test----')
    time.sleep(1)


def f1():
    # help(Thread)
    t = Thread(target=print_say)
    t.start()
    t.join()
    print(type(t))
    print(type(Thread))
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
