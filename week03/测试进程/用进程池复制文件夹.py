# -*- coding:utf-8 -*-
import os
import sys
from multiprocessing import Manager, Pool


def copy_file(file_old, file_new):
    """
        复制一个文件
    :param file_old:    原文件路径
    :param file_new:    新文件路径
    :return:
    """
    file_read = open(file_old, 'rb')
    file_write = open(file_new, 'wb')
    file_write.write(file_read.read())
    file_write.flush()
    file_read.close()
    file_write.close()
    pass


def copy_dir(dir_old, dir_new):
    """
        复制一个文件夹
    :param dir_old:     要复制的文件夹路径
    :param dir_new:     新的文件夹路径
    :return:
    """
    # 1.创建新文件夹
    if not os.path.exists(dir_new):
        os.mkdir(dir_new)

    # 2.创建一个Queue
    queue = Manager().Queue()

    # 3.将文件名放入queue中去
    for file_name in os.listdir(dir_old):
        tup = (dir_old + '/' + file_name, dir_new + '/' + file_name)
        queue.put(tup)

    # 4.创建一个进程池，复制文件到新文件夹下
    pool = Pool(3)
    for i in range(3):
        pool.apply_async(copy_process, args=(queue,))
    pool.close()
    pool.join()

    pass


def copy_process(queue):
    while not queue.empty():
        file_name = queue.get()
        print(file_name)
        copy_file(file_name[0], file_name[1])
        print('%s 复制完成' % str(file_name[0]))

    print('----over----')


def copy(*args):
    if args is None or len(args) <= 0:
        print('请选择要复制的文件或文件夹')
        return

    dir_old = None
    dir_new = None

    if len(args) == 1:
        dir_old = args[0]
        if os.path.isdir(dir_old):
            dir_new = dir_old + '[附件]'
        elif os.path.isfile(dir_old):
            index = str(dir_old).rfind('.')
            print(index)
            dir_new = dir_old[:index] + '[附件]' + dir_old[index:]
            print('复制后的文件名：%s' % str(dir_new))
    else:
        dir_old = args[0]
        dir_new = args[1]

    if os.path.isdir(dir_old):
        copy_dir(dir_old, dir_new)
    elif os.path.isfile(dir_old):
        copy_file(dir_old, dir_new)


def test_copy_file():
    dir_path = sys.argv[1]
    file = os.listdir(dir_path)[0]
    file_old = dir_path + '/' + file
    file_new = dir_path + '[附件]/' + file
    copy_file(file_old, file_new)


def main():
    args = sys.argv
    print(args)
    copy(*args[1::])
    # test_copy_file()
    pass


if __name__ == '__main__':
    sys.argv = ['', 'daiding']
    main()
