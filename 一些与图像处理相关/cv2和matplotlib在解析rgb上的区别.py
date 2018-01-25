# -*- coding:utf-8 -*-

"""
    在颜色的表示中，其实就一个矩阵，矩阵里的每个元素是一个由三个数组成的数组，
    也可以说矩阵的每个元素是一个三个维度的数组，其中，第一个维度为高度，第二个维度为高度，第三个维度为通道。
    而在颜色表示中，最常见的RGB表示法就是通过这种三维度方式来表示的，第一个维度是R，第二个维度是G，第三个维度是B，
    但是在早期的相机中采用的是BGR表示法，第一个维度是B，第二个维度是G，第三个维度是R。
    在windows操作系统中bmp格式的图片在存储时就是采用的BGR方式。

    通过验证发现（通过观察以两种不同的方式保存的图片img_cv2.jpg和img_plot.jpg）：
    OpenCV在表示的时候，采用的是BGR表示法
    matplotlib在表示的时候，采用的是RGB表示法

"""

import matplotlib.pyplot as mplot
import matplotlib.image as mimg
import cv2
import numpy


def test_save():
    a = [
        [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
        [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
        [[255, 255, 255], [128, 128, 128], [0, 0, 0]]
    ]

    b = [
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        [[1, 1, 0], [1, 0, 1], [0, 1, 1]],
        [[1, 1, 1], [0.5, 0.5, 0.5], [0, 0, 0]]
    ]

    img_arr_cv2 = numpy.array(2)
    img_arr_plot = numpy.array(b)
    cv2.imwrite('img_cv2.jpg', img_arr_cv2)
    mplot.imsave('img_plot.jpg', img_arr_plot)


def test_read():
    img_arr_cv2 = cv2.imread('img_plot.jpg')
    img_arr_plot = mimg.imread('img_plot.jpg')
    print(img_arr_cv2)
    print(img_arr_plot)


def test_read_png():
    pass


def main():
    # test_save()
    test_read()
    pass


if __name__ == '__main__':
    main()
