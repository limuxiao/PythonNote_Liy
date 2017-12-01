# -*- coding:utf-8 -*-
from week01.CarStore.CarFactoryMenu import CarFactoryMenu
from week01.CarStore.CarManager import CarManager
from week01.CarStore.XianDaiFactory import XianDaiFactory


class CarStore(object):
    def __init__(self):
        self.car_manager = CarManager()
        pass

    def order(self, name):
        return self.car_manager.get_car_with_name(name)

    def get_all_cars(self):
        return self.car_manager.get_all_cars()

    def add_cars(self):
        car_factory = CarFactoryMenu.get_car_factory(XianDaiFactory().get_factory_name())
        # print(car_factory)
        if car_factory:
            cars = car_factory['factory_cars']
            if cars:
                mt = cars[0]()
                self.__add_cars(mt, 10)
                ld = cars[1]()
                self.__add_cars(ld, 5)

        # self.__add_cars()
        pass

    def __add_cars(self, car, num):
        """新增一批车到库存"""
        self.car_manager.add_car(car, num)



def main():
    car_store = CarStore()
    car_store.add_cars()
    car_store.get_all_cars()
    car = car_store.order('名图')
    print(car)
    pass


if __name__ == '__main__':
    main()