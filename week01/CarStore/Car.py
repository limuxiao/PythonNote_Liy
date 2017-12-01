# -*- coding:utf-8 -*-
class Car(object):
    def __init__(self, car_type, car_name, car_price):
        self.__car_type = car_type
        self.__car_name = car_name
        self.__car_price = car_price
        pass

    def move(self):
        print('-----%s moving-----[%s]' % (self.__car_name, self.__car_type))

    def stop(self):
        print('-----%s stopping-----[%s]' % (self.__car_name, self.__car_type))

    def music(self):
        print('-----%s musicing-----[%s]' % (self.__car_name, self.__car_type))

    def set_name(self, car_name):
        self.__car_name = car_name

    def set_type(self, car_type):
        self.__car_type = car_type

    def set_price(self, car_price):
        self.__car_price = car_price

    def get_name(self):
        return self.__car_name

    def get_type(self):
        return self.__car_type

    def get_price(self):
        return self.__car_price


class MingTu(Car):
    def __init__(self):
        super().__init__('四驱', '名图', 80000)


class Mkz(Car):
    def __init__(self):
        super().__init__('SUV', 'MKZ', 280000)
