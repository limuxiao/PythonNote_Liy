# -*- coding:utf-8 -*-
from week01.Cat import Cat
from week01.SwweetPotato import SweetPatato as SP
from week01.Home import Home as Home
from week01.Home import Bed as Bed


def testClass01():
    c = Cat(age=20, name='Tom')
    c.test()
    c.sleep()
    print(c.getName())
    print(c.getAge())
    c.setName('Hehe')
    c.setAge(365)
    print(c.getName())
    print(c.getAge())
    print(c)

    a = Cat(name='LanMao', age=15)
    print(a)
    print(a.compare(c))
    print(c.compare(a))
    pass


def testClass02():
    sp = SP()
    print(sp)
    sp.cook(1)
    print(sp)
    sp.addComp('盐')
    print(sp)
    sp.cook(4)
    sp.addComp('辣椒')
    print(sp)
    pass


def testClass03():
    home = Home('我的家', 130, '北京市朝阳区望京西街112号')
    print(home)
    bed = Bed('席梦思', 4)
    print(bed)
    home.addFurniture(bed)
    print(home)
    pass


def main():
    # testClass01()
    # testClass02()
    testClass03()
    pass


if __name__ == '__main__':
    main()
