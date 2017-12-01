# -*- coding:utf-8 -*-
import week01.CarStore.Car as Car
from week01.CarStore.CarManager import CarManager


class CarStore(object):
    def __init__(self):
        self.car_manager = CarManager()
        self.car_manager.add_car(Car.Mkz(), 3)
        self.car_manager.add_car(Car.MingTu(), 2)
        pass

    def order(self, name):
        return self.car_manager.get_car_with_name(name)

    def get_all_cars(self):
        return self.car_manager.get_all_cars()



def main():
    car_store = CarStore()
    print(car_store.get_all_cars())
    car = car_store.order('MKZ')
    print(car_store.get_all_cars())
    car = car_store.order('MKZ')
    print(car_store.get_all_cars())
    car = car_store.order('MKZ')
    print(car_store.get_all_cars())
    pass


if __name__ == '__main__':
    main()