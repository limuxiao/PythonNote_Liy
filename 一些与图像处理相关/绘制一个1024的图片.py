# -*- coding:utf-8 -*-
import cv2
import numpy
import matplotlib.pyplot as plt
import math


def get_r(i, j):
    return math.fabs(math.sin(i * j))


def get_g(i, j):
    return ((i **2 + j ** 2) % 255) / 255


def get_b(i, j):
    return math.fabs(math.cos(i * j))


def get_image():
    img_arr = [[[get_r(j, i), get_g(j, i), get_b(j, i)] for j in range(1024)] for i in range(1024)]
    # cv2.imwrite('1024.jpg', numpy.array(img_arr))
    # cv2.imshow('image', numpy.array(img_arr))
    plt.imshow(numpy.array(img_arr), interpolation='bicubic')
    plt.show()
    pass


def main():
    get_image()
    pass


if __name__ == '__main__':
    main()
