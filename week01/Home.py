# -*- coding:utf-8 -*-
class Home:
    def __init__(self, name, area, addr):
        self.name = name  # 名称
        self.area = area  # 面积
        self.addr = addr  # 地址
        self.left_area = self.area  # 可用面积
        self.contain_items = []  # 家具
        pass

    def __str__(self):
        msg = '%s' % self.name
        msg += '\n地址：%s' % self.addr
        msg += '\n面积:%s' % self.area
        msg += '\n可用面积：%s' % self.left_area
        msg += '\n家具：%s' % (str(self.contain_items))
        return msg

    def addFurniture(self, item):
        self.contain_items.append(item.get_name())
        self.left_area = self.area - item.get_area()


class Bed:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return '我有一个%s，他占用的面积是：%s' % (self.name, self.area)

    def set_name(self, name):
        self.name = name

    def set_area(self, area):
        self.area = area

    def get_name(self):
        return self.name

    def get_area(self):
        return self.area
