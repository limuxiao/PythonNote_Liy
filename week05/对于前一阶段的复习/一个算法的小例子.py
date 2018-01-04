# -*- coding:utf-8 -*-
import time


def f1():
    start_time = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            for c in range(0, 1001):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print('a:%d,b:%d,c:%d' % (a, b, c))
    end_time = time.time()
    print('time cost: %s' % str(end_time - start_time))


def f2():
    start_time = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print('a:%d,b:%d,c:%d' % (a, b, c))
    end_time = time.time()
    print('time cost: %s' % str(end_time - start_time))


def main():
    # f1()
    f2()
    pass


if __name__ == '__main__':
    main()