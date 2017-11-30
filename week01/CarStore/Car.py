# -*- coding:utf-8 -*-
class Car(object):

    def __init__(self, car_type, car_name):
        self.car_type = car_type
        self.car_name = car_name
        pass

    def move(self):
        print('-----%s moving-----[%s]' % (self.car_name, self.car_type))

    def stop(self):
        print('-----%s stopping-----[%s]' % (self.car_name, self.car_type))

    def music(self):
        print('-----%s musicing-----[%s]' % (self.car_name, self.car_type))

    def get_name(self):
        return self.car_name

    def get_type(self):
        return self.car_type

class XianDai(Car):
    def __init__(self):
        super().__init__('四驱', '现代')

class MingTu(XianDai):
    def __init__(self):
        pass

class Linken(Car):
    pass

class Mkz(Linken):
    pass