# -*- coding:utf-8 -*-
import functools
import os


class singleton:
    """
        单例类装饰器，装饰的类生成的对象是单例的
    """
    def __init__(self, cls):
        self.__cls = cls
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = self.__cls(*args, **kwargs)
        functools.wraps(self.__cls)
        return self.__instance


# @singleton
class CP(object):

    @classmethod
    def __copy_file(cls, file_old, file_new):
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

    @classmethod
    def __copy_dir(cls, dir_old, dir_new):
        if os.path.isdir(dir_old):
            pass
        elif os.path.isfile(dir_old):
            cls.__copy_file(dir_old, dir_new)
        pass

    @classmethod
    def copy(cls, file_old, file_new):
        pass


def f1():
    cp1 = CP()
    cp2 = CP()
    print(id(cp1))
    print(id(cp2))


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
