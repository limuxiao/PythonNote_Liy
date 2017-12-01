# -*- coding:utf-8 -*-
class CarFactoryMenu:

    # 定义一个类属性，用于接收所有的汽车生产厂商

    __car_factorys = []

    """
        车的生产厂商清单类
    """
    def __init__(self):
        pass

    @classmethod
    def add_car_factory(cls, factory_name, factory_cars):
        """
            添加一个汽车生产厂商到清单中去
        :param factory_name:   汽车厂商的名字
        :param factory_cars:   汽车厂商生产的车类型列表
        :return:
        """
        car_factory_dict = {'factory_name': factory_name, 'factory_cars': factory_cars}
        cls.__car_factorys.append(car_factory_dict)


    @classmethod
    def get_car_factorys(cls):
        """获取汽车生产厂商的列表"""
        msg = '现有的生产厂商有：\n'
        for car_factory_dict in cls.__car_factorys:
            msg += '\t%s,%s能生产的车产品有%s\n' % (car_factory_dict['factory_name'], car_factory_dict['factory_name'], str(car_factory_dict['factory_cars']))
        return msg

    @classmethod
    def get_car_factory(cls, factory_name):
        """
            根据汽车生产厂商的名字，获取一个汽车生产厂商的信息
        :param factory_name:    汽车生产厂商的名字
        :return:
        """
        for car_factory_dict in cls.__car_factorys:
            if car_factory_dict['factory_name'] == factory_name:
                return car_factory_dict
        else:
            raise MenuException('未找到您要查找的汽车生产厂商')


class MenuException(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return self.__msg

