# -*- coding:utf-8 -*-
class Dog:
    def __init__(self, name, age):
        self.name = name
        if 0 <= age <= 100:
            self.__age = age

    def __sleep(self):
        """
            私有方法
        :return:
        """
        print('%s is sleeping' % self.name)

    def sleep(self, time):
        """
            供外部调用的sleep方法
        :param time:    时间
        :return:
        """
        if 18 <= time <= 24 or 0 <= time <= 6:
            self.__sleep()
        else:
            print('%s is not sleeping' % self.name)

    def set_age(self, age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            print('The Dog\'s age must in 0 - 100')

    def get_age(self):
        return self.__age
