# -*- coding:utf-8 -*-
import gc


class C:
    def __init__(self):
        print('object born,id:%s' % str(hex(id(self))).upper())

    def __del__(self):
        print('object del,id:%s' % str(hex(id(self))).upper())


def f1():
    # gc.set_debug(gc.DEBUG_LEAK)
    print('----0----')
    c1 = C()
    c2 = C()
    c1.t = c2
    c2.t = c1
    print('----1----')
    print(gc.garbage)
    del c1
    print('----1.1----')
    del c2
    print('----2----')
    print(gc.garbage)
    print('----3----')
    print(gc.collect())     # 显示执行垃圾回收
    print('----4----')
    print(gc.garbage)


def f2():
    print(gc.get_threshold())
    print(gc.get_count())
    # help(gc.isenabled)
    print(gc.isenabled())


def main():
    f1()
    # f2()


if __name__ == '__main__':
    main()
