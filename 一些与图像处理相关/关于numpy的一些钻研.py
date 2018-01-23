# -*- coding:utf-8 -*-
import matplotlib.pyplot as mplt
import matplotlib.image as mimg
import numpy as np
from random import random
from threading import Thread


def f1():
    arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    print(arr.shape)


def f2():
    img_arr = mimg.imread('test2.png')
    for img_arr_row in img_arr:
        for img_arr_core in img_arr_row:
            print(img_arr_core)
    pass


def create_arr(width=20, height=20):
    arr = []
    for i in range(width):
        arr_row = []

        for j in range(height):
            arr_core = [random(), random(), random()]
            arr_row.append(arr_core)

        arr.append(arr_row)

    return np.array(arr)


def rgb_2_grey(r, g, b):
    return r * 0.30 + g * 0.59 + b * 0.11


def f3():

    def show_data(img_arr, num):
        img_arr_n = img_arr[:, :, num]
        mplt.imshow(img_arr_n, cmap='Greys_r')
        mplt.show()
        pass

    img_arr = create_arr()
    # 这句话的意思是取每一个像素点色值列表里的第一个元素，既取[1.2.3.4]中的1
    # img_arr_0 = img_arr[:, :, 0]

    t0 = Thread(target=show_data, args=(img_arr, 0))
    t1 = Thread(target=show_data, args=(img_arr, 1))
    t2 = Thread(target=show_data, args=(img_arr, 2))
    t0.start()
    t1.start()
    t2.start()


def f4():
    img_arr = create_arr()
    img_arr_0 = img_arr[:, :, 0]
    img_arr_1 = img_arr[:, :, 1]
    img_arr_2 = img_arr[:, :, 2]
    print(img_arr[0])
    print()
    print(img_arr_0[0])
    print()
    print(img_arr_1[0])
    print()
    print(img_arr_2[0])
    pass


def f5():
    width, height = 20, 20
    img_arr = create_arr(width, height)
    img_arr_0 = img_arr[:, :, 0]
    img_arr_1 = img_arr[:, :, 1]
    img_arr_2 = img_arr[:, :, 2]
    img_width, img_height, deep = img_arr.shape
    img_arr_grey = [[rgb_2_grey(img_arr_0[i][j], img_arr_1[i][j], img_arr_2[i][j]) for j in range(img_height)] for i in range(img_width)]
    # print(img_arr_grey)
    mplt.imshow(img_arr_grey, cmap='Greys_r')
    mplt.show()


def test_random():
    print(random())
    pass


def main():
    # f1()
    # f2()
    # f3()
    # f4()
    f5()
    pass


if __name__ == '__main__':
    main()
