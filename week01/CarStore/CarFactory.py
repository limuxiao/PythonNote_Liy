# -*- coding:utf-8 -*-
from week01.CarStore.CarFactoryMenu import CarFactoryMenu


class CarFactory:
    """
        车子的工厂类
    """

    def __init__(self, factory_name, factory_level, factory_cars):
        """
            __init__
        :param factory_name:    汽车生产厂商的名字
        :param factory_level:   汽车生产厂商的等级
        :param factory_cars:    汽车生产厂商的生产的车类列表
        """
        self.__factory_name = factory_name
        self.__factory_level = factory_level
        self.__factory_cars = factory_cars
        pass

    def get_factory_name(self):
        return self.__factory_name

    def get_factory_type(self):
        return self.__factory_level

    def get_factory_cars(self):
        return self.__factory_cars

    def create_car(self):
        pass
