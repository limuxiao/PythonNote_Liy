# -*- coding:utf-8 -*-

"""
    将 rgb 灰度化
"""


def rgb_2_grey(r, g, b):
    return r * 0.30 + g * 0.59 + b * 0.11


def get_grey(img_arr):
    arr_r, arr_g, arr_b = img_arr[:, :, 0], img_arr[:, :, 1], img_arr[:, :, 2]
    img_width, img_height, img_deep = img_arr.shape
    return [[rgb_2_grey(arr_r[i][j], arr_g[i][j], arr_b[i][j])
             for j in range(img_height)] for i in range(img_width)]


def __test_list():
    a = [i for i in range(10) if i == 6]
    print(a)
    pass


def main():
    __test_list()
    pass


if __name__ == '__main__':
    main()
