# -*- coding:utf-8 -*-
from week01.CarStore.Car import Car
from week01.CarStore.CarFactory import CarFactory
from week01.CarStore.CarFactoryMenu import CarFactoryMenu


class XianDaiFactory(CarFactory):
    """现代 Factory"""

    __instance = None
    do_init = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        super().__init__('现代', 5, [MingTu, LingDong])
        if not self.do_init:
            CarFactoryMenu.add_car_factory(self.get_factory_name(), self.get_factory_cars())
            self.do_init = True

class MingTu(Car):
    """名图"""
    def __init__(self):
        super().__init__('四驱', '名图', 80000)

class LingDong(Car):
    """领动"""
    def __init__(self):
        super().__init__('四驱', '领动', 75000)
