# -*- coding:utf-8 -*-

a = 100
b = [100]

def testL():
    """
        方法简介
    :return:
    """
    nums = [11, 2, 333, 4454, 56455, 3322, 333]
    nums.sort()
    print(nums)
    print(nums[::-1])
    nums.sort()
    print(nums)
    nums.sort(reverse=True)
    print(nums)
    pass


def testDict():
    infors = [{'name': 'laowang'}, {'name': 'banzhang'}, {'name': 'xiaoming'}]
    print(infors)
    infors.sort(key=lambda y : y['name'],reverse=True)
    print(infors)
    pass


def testSum(a, b, func):
    result = func(a, b)
    return result


def testSum01(num):
    num += num
    print(num)


def testSum02(num):
    num = num + num
    print(num)



def main():
    # testL()
    # testDict()
    # g = lambda x, y: x ** y
    # print(testSum(11, 2, g))
    # testSum01(a)
    # print(a)
    # testSum01(b)
    # print(b)
    testSum02(a)
    print(a)
    testSum02(b)
    print(b)
    c = [200]
    testSum02(c)
    print(c)
    pass


if __name__ == '__main__':
    main()
