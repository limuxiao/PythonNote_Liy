# -*- coding:utf-8 -*-
import threading
from threading import Thread


def f1():
    print(threading.current_thread())
    print(threading.current_thread().name)
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
