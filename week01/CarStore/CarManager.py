# -*- coding:utf-8 -*-
class CarManager(object):
    def __init__(self):
        self.cars = []

    def add_car(self, car, num):
        """
            新增一批汽车
        :param car: 汽车对象
        :param num: 库存
        :return:
        """

        car_dict = {car.get_name(): car, 'num': num}
        self.cars.append(car_dict)

    def del_car(self, car, num):
        pass