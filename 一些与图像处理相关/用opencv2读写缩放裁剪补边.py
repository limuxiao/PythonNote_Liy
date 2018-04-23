# -*- coding:utf-8 -*-

"""
    读图像用cv2.imread()，
        可以按照不同模式读取，一般最常用到的是读取单通道灰度图，或者直接默认读取多通道。
    存图像用cv2.imwrite()，
        注意存的时候是没有单通道这一说的，根据保存文件名的后缀和当前的array维度，
        OpenCV自动判断存的通道，另外压缩格式还可以指定存储质量


        # 读取一张400x600分辨率的图像
        color_img = cv2.imread('test_400x600.jpg')
        print(color_img.shape)

        # 直接读取单通道
        gray_img = cv2.imread('test_400x600.jpg', cv2.IMREAD_GRAYSCALE)
        print(gray_img.shape)

        # 把单通道图片保存后，再读取，仍然是3通道，相当于把单通道值复制到3个通道保存
        cv2.imwrite('test_grayscale.jpg', gray_img)
        reload_grayscale = cv2.imread('test_grayscale.jpg')
        print(reload_grayscale.shape)

        # cv2.IMWRITE_JPEG_QUALITY指定jpg质量，范围0到100，默认95，越高画质越好，文件越大
        cv2.imwrite('test_imwrite.jpg', color_img, (cv2.IMWRITE_JPEG_QUALITY, 80))

        # cv2.IMWRITE_PNG_COMPRESSION指定png质量，范围0到9，默认3，越高文件越小，画质越差
        cv2.imwrite('test_imwrite.png', color_img, (cv2.IMWRITE_PNG_COMPRESSION, 5))


        --------------------------------------------------------------------------

        # 读取一张四川大录古藏寨的照片
        img = cv2.imread('tiger_tibet_village.jpg')

        # 缩放成200x200的方形图像
        img_200x200 = cv2.resize(img, (200, 200))

        # 不直接指定缩放后大小，通过fx和fy指定缩放比例，0.5则长宽都为原来一半
        # 等效于img_200x300 = cv2.resize(img, (300, 200))，注意指定大小的格式是(宽度,高度)
        # 插值方法默认是cv2.INTER_LINEAR，这里指定为最近邻插值
        img_200x300 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5,
                                      interpolation=cv2.INTER_NEAREST)

        # 在上张图片的基础上，上下各贴50像素的黑边，生成300x300的图像
        img_300x300 = cv2.copyMakeBorder(img, 50, 50, 0, 0,
                                               cv2.BORDER_CONSTANT,
                                               value=(0, 0, 0))

        # 对照片中树的部分进行剪裁
        patch_tree = img[20:150, -180:-50]

        cv2.imwrite('cropped_tree.jpg', patch_tree)
        cv2.imwrite('resized_200x200.jpg', img_200x200)
        cv2.imwrite('resized_200x300.jpg', img_200x300)
        cv2.imwrite('bordered_300x300.jpg', img_300x300)

        --------------------------------------------------------------------------
"""

import cv2
import matplotlib.pyplot as plt
import numpy


class ShowTool(object):
    pass

    @classmethod
    def show_by_plt(cls, img_arr):
        plt.imshow(img_arr)
        plt.show()
        pass

    @classmethod
    def show_by_cv2(cls, img_name, img_arr):
        cv2.imshow(img_name, img_arr)
        cv2.waitKey(0)
        pass


def test_read_all():
    """

    :return:
    """
    img_arr = cv2.imread('djssg.jpg')
    print(img_arr.shape)
    img_arr = cv2.imread('djssg.jpg', flags=cv2.IMREAD_GRAYSCALE)
    print(img_arr.shape)
    cv2.imshow('image', img_arr)
    pass


def test_resize():
    """
        测试缩放
    :return:
    """
    img_arr = cv2.imread('logo.png')
    print(img_arr.shape)
    # dsize 为一个两个元素tuple 既（width, height）, fx、fy表示在宽高上的缩放比例,当指定fx、fy时,dsiz应设为（0，0）才有效
    img_arr_new = cv2.resize(img_arr, dsize=(144, 144))
    print(img_arr_new.shape)
    print(img_arr_new[100][100])
    # plt.imshow(img_arr_new)
    # plt.show()
    # plt.imsave(img_arr_new, "icon_new.png")
    cv2.imwrite("logo_new.png", img_arr_new)
    pass


def test_cut():
    """
        测试裁剪
    :return:
    """
    img_arr = cv2.imread('djssg.jpg')
    img_arr_new = img_arr[0:500, 0:700]
    cv2.imshow('test', img_arr_new)
    cv2.waitKey(0)
    pass


def test_add():
    """
        测试补边
    :return:
    """
    img_arr = cv2.imread('djssg.jpg')
    img_arr_resize = cv2.resize(img_arr, dsize=(0, 0), fx=0.3, fy=0.3)
    img_arr_add = cv2.copyMakeBorder(img_arr_resize, 50, 20, 30, 70,
                                     borderType=cv2.BORDER_CONSTANT, value=(255, 127, 63))
    ShowTool.show_by_cv2('add', img_arr_add)
    pass


def main():
    # test_read_all()
    test_resize()
    # test_cut()
    # test_add()
    pass


if __name__ == '__main__':
    main()
