# -*- coding:utf-8 -*-
import matplotlib.pyplot as mplot
import matplotlib.image as mimg
import cv2

import img_recognize as ir


def f1():
    help(mplot.plot)


def f2():
    help(cv2.calcHist)


def f3():
    """
        绘制一张图的灰度直方图
    :return:
    """
    # 1.读取一张图片,获取纵横深
    img_arr = mimg.imread('test3.jpg')
    img_width, img_height, img_deep = img_arr.shape
    # print('img_width = %d; img_height = %d; img_deep = %d' % (img_width, img_height, img_deep))

    # 2.获取灰度图
    img_grey = ir.get_grey(img_arr)
    # print(len(img_grey))
    # print(len(img_grey[0]))

    # 3.计算直方图
    x = range(img_width)
    y = [256 - max([img_grey[i][j] * 256 for j in range(img_height)]) for i in range(img_width)]
    mplot.plot(x, y, 'g')
    mplot.show()
    pass


def Hist(image):
    a = [0] * 256
    w = image.width
    h = image.height
    iHist = cv2.CreateImage((256, 256), 8, 3)
    for i in range(h):
        for j in range(w):
            iGray = int(image[i, j])
            a[iGray] = a[iGray] + 1

    S = max(a)
    c = cv2.RGB(200, 150, 255)

    for k in range(256):
        a[k] = a[k] * 200 / S
        x = (k, 255)
        y = (k, 255 - a[k])
        cv2.Line(iHist, x, y, c)

    return iHist


def f4():
    img_arr = mimg.imread('test3.jpg')
    # print(img_arr.shape)
    img_width, img_height, img_deep = img_arr.shape
    img_arr_r = img_arr[:, :, 0]
    img_arr_g = img_arr[:, :, 1]
    img_arr_b = img_arr[:, :, 2]
    x = range(img_width)
    yr = [max([j for j in i]) for i in img_arr_r]
    yg = [[min([j for j in i]), max([j for j in i])] for i in img_arr_g]
    yb = [256 - max([j for j in i]) for i in img_arr_b]
    mplot.plot(x, yg, 'g')
    mplot.show()
    11001100


def main():
    # f1()
    # f2()
    # f3()
    f4()
    pass


if __name__ == '__main__':
    main()
