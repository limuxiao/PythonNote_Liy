# -*- coding:utf-8 -*-
import os
import sys


def copy_file(file_old, file_new):
    """
        复制一个文件
    :param file_old:    原文件路径
    :param file_new:    新文件路径
    :return:
    """
    file_read = open(file_old, 'r')
    file_write = open(file_new, 'w')
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
    files = os.listdir(dir_old)
    print(len(files))
    pass


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


def main():
    args = sys.argv
    print(args)
    copy(*args[1::])
    pass


if __name__ == '__main__':
    main()
