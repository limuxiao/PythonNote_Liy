# -*- coding:utf-8 -*-
import random
import img_recognize as ir


def test_list():
    # arr = [0] * 5
    # for i in range(5):
    #     arr[i] = i ** 2
    # print(arr)

    arr = [i for i in range(5)]
    print(arr)

    arr = [['%d -- %d' % (i, j) for j in range(3)] for i in range(2)]
    print(arr)

    pass


def test_random():
    random.random()


def test_img():
    print(ir.rgb_2_grey(200, 11, 22))
    pass


def test_max():
    help(max)
    pass


def main():
    # test_list()
    # test_img()
    test_max()
    pass


if __name__ == '__main__':
    main()
