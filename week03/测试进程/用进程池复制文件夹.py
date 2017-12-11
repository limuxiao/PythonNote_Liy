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
    pass


def copy_dir(dir_old, dir_new):
    """
        复制一个文件夹
    :param dir_old:     要复制的文件夹路径
    :param dir_new:     新的文件夹路径
    :return:
    """
    pass


def copy(*args):
    if args is None or len(args) <= 0:
        print('请选择要复制的文件或文件夹')
        return

    dir_old = None
    dir_new = None

    if len(args) == 1:
        dir_old = args[0]
        dir_new = dir_old + '[附件]'
    else:
        dir_old = args[0]
        dir_new = args[1]

    copy_dir(dir_old, dir_new)


def main():
    args = sys.argv
    print(args)
    copy(*args[1::])
    pass


if __name__ == '__main__':
    main()
