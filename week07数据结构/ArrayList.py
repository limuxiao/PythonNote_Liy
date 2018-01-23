# -*- coding:utf-8 -*-


class ArrayNode(object):

    def __init__(self, index, item):
        pass


class ArrayList(object):
    """
        自定义顺序表的实现
    """
    def __init__(self, size=10):
        """
            init
        :param size:
        """
        self.__size = size
        self.__index = 0
        pass

    def append(self, item):
        """
            在顺序表的末尾添加一个元素
        :param item:
        :return:
        """
        pass

    def insert(self, index, item):
        """
            在顺序表指定索引添加一个元素
        :param index:
        :param item:
        :return:
        """
        pass

    def get(self, index=-1):
        """
            获取指定索引的元素，默认去最后一个
        :param index:
        :return:
        """
        pass

    def delete(self, index=-1):
        """
            根据索引删除一个元素，默认删除最后一个
        :param index:
        :return:
        """
        pass

    def size(self):
        """
            获取顺序表的长度
        :return:
        """
        return self.__index


def main():
    pass


if __name__ == '__main__':
    main()
