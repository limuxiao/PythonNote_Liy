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

    def del_car(self, car):
        for car_dict in self.cars:
            if car_dict['name'] == car.get_name():
                self.cars.remove(car_dict)
        pass

    def update_car(self, car, num):
        for car_dict in self.cars:
            if car_dict['name'] == car.get_name():
                car_dict['num'] = num

    def get_car_with_name(self, name):
        for car_dict in self.cars:
            if car_dict['name'] == name:    # 找到车,查看库存
                num = car_dict['num']
                if num > 0:
                    car = car_dict['car']
                    num -= 1
                    if num <= 0:            # 如果库存为零了，将该车从库存中删除
                        self.del_car(car)
                    else:
                        self.update_car(car,num)
                    return car
                else:
                    return
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


def main():
    print('Test Carmanager')
    car_manager = CarManager()

    pass

if __name__ == "__main__":
    main()