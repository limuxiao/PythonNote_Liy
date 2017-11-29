# -*- coding:utf-8 -*-


def testChange01():
    a = 'hello'
    print(a[0])
    a[0] = 'w'
    pass


def testChange02():
    a = [11, 22, 33]
    a[0] = 44
    print(a)
    b = {'name': 'laowang'}
    name = b.get('age')
    print(name)
    pass


def testChange03():
    infos = {'name': 'laowang', 11: 22, (11,22): 34, [11,22]: 11}
    print(infos)
    pass


def main():
    # testChange01()
    # testChange02()
    testChange03()
    pass


if __name__ == '__main__':
    main()
