# -*- coding:utf-8 -*-
class CarManager(object):
    """
        车库管理类
    """
    def __init__(self):
        self.cars = []

    def add_car(self, car, num):
        """
            新增一批汽车
        :param car: 汽车对象
        :param num: 库存
        :return:
        """

        car_dict = {'name': car.get_name(), 'car': car, 'num': num, 'price': car.get_price()}
        self.cars.append(car_dict)
        print('-----新进：%s,库存：%s----' % (car.get_name(), num))

    def del_car(self, car, num):

        pass

    def get_car_with_name(self, name):
        for car_dict in self.cars:
            if car_dict['name'] == name:
                return car_dict['car']
        else:
            print('未找到您要的车')
            return

    def get_all_cars(self):
        """
            获取到库存里所有的车
        :return:
        """
        msg = '当前车库有：\n'
        for car_dict in self.cars:
                msg += '\t%s\t库存：%s\t售价：%s\n' % (car_dict['name'], car_dict['num'], car_dict['price'])
        return msg