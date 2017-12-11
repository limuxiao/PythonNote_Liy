# -*- coding:utf-8 -*-
from multiprocessing import Queue, Pool
import time


q_clear2write = Queue()
q_read2clear = Queue()


def write_file(text):
    """
        将内容写入文件中
    :param text:
    :return:
    """
    file = open('test.txt', 'a+', encoding='utf=8')
    file.write('%s\n' % str(text))
    file.flush()
    file.close()
    pass


def read_file():
    """
        从文件中读取所有内容
    :return:
    """
    file = open('test.txt', 'r+', encoding='utf-8')
    s = file.read()
    print(s)
    file.close()


def clear_file():
    """
        清空文件内容
    :return:
    """

    file = open('test.txt', 'w+', encoding='utf-8')
    file.write('')
    file.flush()
    file.close()


def write_control():
    # while True:
    if not q_clear2write.empty():
        ret = q_clear2write.get()
        if ret == 'writeable':
            print('----write start----')
            time.sleep(5)
            write_file('我是新加的内容!')
            time.sleep(2)
            print('----write over----')
    else:
        write_file('我就试试看')


def read_control():
    # while True:
    print('----read start----')
    q_read2clear.put('can not clear')
    time.sleep(5)
    read_file()
    time.sleep(2)
    q_read2clear.put('can clear')
    print('----read over----')


def clear_control():
    while True:
        q_clear2write.put('write lock')     # 禁止写

        if not q_read2clear.empty():        # 由读进程发过来的消息
            ret = q_read2clear.get()
            print('----%s----' % ret)
            if ret == 'can clear':          # 可删除
                print('----clear start----')
                time.sleep(5)
                clear_file()
                time.sleep(2)
                print('----clear over----')
            else:
                pass

        q_clear2write.put('writeable')      # 放开


def f1():
    # write_file('我就试试看')
    # read_file()

    pool = Pool(3)
    pool.apply_async(read_control)
    pool.apply_async(write_control)
    pool.apply_async(clear_control)

    pool.close()
    pool.join()


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
