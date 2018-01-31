# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import cv2
from mpl_toolkits.mplot3d import Axes3D


def f1():
    fig = plt.figure()

    arr = [
        [[1], [2], [3]],
        [[4], [5], [6]],
        [[7], [8], [9]]
    ]

    img_arr = np.array(arr)

    ax = fig.add_subplot(111, projection='rectilinear')

    ax.set_xlabel('X Values')
    ax.set_xlim([0, 9])
    ax.set_ylim([0, 9])
    # ax.set_zlim([0, 9])
    ax.set_ylabel('Y Values')
    # ax.set_zlabel('Z Values')

    plt.show()
    pass


def f2():
    arr = [
        [[178, 166, 184], [153, 139, 157]],
        [[166, 154, 172], [154, 140, 158]],
        [[166, 155, 171], [163, 150, 166]],
    ]

    img_arr = np.array(arr)

    plt.plot(img_arr)
    plt.show()
    pass


def f3():
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel('X value')
    ax.set_ylabel('Y value')
    ax.set_zlabel('Z value')
    ax.set_xlim([0, 9])
    ax.set_ylim([0, 9])
    ax.set_zlim([0, 9])
    plt.show()
    pass


def test_hist():
    arr = [
        [[178, 166, 184], [153, 139, 157]],
        [[166, 154, 172], [154, 140, 158]],
        [[166, 155, 171], [163, 150, 166]],
    ]

    img = np.array(arr)

    img_jpg = cv2.imread('djssg.jpg')

    print(img.shape)

    # plt.imshow(img)
    # plt.show()
    # cv2.imshow('test', img)
    # cv2.waitKey(0)

    # 分通道计算每个通道的直方图
    hist_b = cv2.calcHist([img], [0], None, [256], [0, 256])
    # hist_g = cv2.calcHist([img], [1], None, [256], [0, 256])
    # hist_r = cv2.calcHist([img], [2], None, [256], [0, 256])
    #
    print(hist_b)
    # print('-' * 50)
    # print(hist_g)
    # print('-' * 50)
    # print(hist_r)

    pass


def test_zip():
    a = [1, 2]
    b = [3, 4, 5]
    for c, d in zip(a, b):
        print(c)
        print(d)
    pass


def test_plot():
    # help(plt.plot)
    plt.plot([1, 4, 3], [1, 2, 3], [1, 2, 3],  'go-', label='line 1', linewidth=1)
    plt.axis([0, 9, 0, 9])
    plt.show()
    pass


def main():
    # f1()
    # f2()
    f3()
    # test_zip()
    # test_hist()
    # test_plot()
    pass


if __name__ == '__main__':
    main()
