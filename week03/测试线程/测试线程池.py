# -*- coding:utf-8 -*-
import threadpool
import threading

pool = threadpool.ThreadPool(10)        # 创建线程池，10是线程个数
request_list = []                       # 任务列表


def add_request(target, args=()):
    """
        添加一个任务
    :param target:
    :return:
    """
    request_list.append(threadpool.makeRequests(target, args))
    map(pool.putRequest, request_list)
    pass


def test(a):
    name = threading.current_thread().getName()
    print('当前线程的名字：%s, 参数：%s' % (name, str(a)))


def f1():
    # for i in range(15):
    #     add_request(target=test, args=(100,))
    # pool.poll()
    s = '111'
    print(s[1] == '1')
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
