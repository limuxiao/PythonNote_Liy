# -*- coding:utf-8 -*-
class T(object):
    def __setattr__(self, key, value):
        return object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        print('----调用__getattribute__----item:%s' % item)
        if item == 'a':
            return 'haha'
        else:
            return self.test

    def test(self):
        return '----test----'


def f1():
    t = T()
    print(t.a)
    print(t.b())  # 会让程序死掉
    # 原因是： 当t.b执⾏时， 会调⽤Person类中定义的__getattribute__⽅法， 但是在
    # if条件不满⾜， 所以 程序执⾏else⾥⾯的代码， 即return self.test 问题就在
    # self.test的值返回， 那么⾸先要获取self.test的值， 因为self此时就是t这个对象
    # t.test 此时要获取t这个对象的test属性， 那么就会跳转到__getattribute__⽅法
    # ⽣了递归调⽤， 由于这个递归过程中 没有判断什么时候推出， 所以这个程序会永⽆休⽌
    # 每次调⽤函数， 就需要保存⼀些数据， 那么随着调⽤的次数越来越多， 最终内存吃光，
    # #
    # 注意： 以后不要在__getattribute__⽅法中调⽤self.xxxx


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
