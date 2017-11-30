# -*- coding:utf-8 -*-

import week01.CarStore.Car as Car

class CarStore(object):
    def __init__(self):
        pass

    def order(self):
        return Car.Car()



def main():
    car_store = CarStore()
    car_store.order()
    pass


if __name__ == '__main__':
    main()