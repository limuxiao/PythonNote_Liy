# -*- coding:utf-8 -*-
import week01.CarStore.Car as Car
from week01.CarStore.CarManager import CarManager


class CarStore(object):
    def __init__(self):
        self.car_manager = CarManager()
        self.car_manager.add_car(Car.MingTu(), 10)
        pass

    def order(self):
        pass



def main():
    car_store = CarStore()
    car_store.order()
    pass


if __name__ == '__main__':
    main()