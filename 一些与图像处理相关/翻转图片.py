# -*- coding:utf-8 -*-
import matplotlib.pyplot as m_plot
import matplotlib.image as m_img
import numpy
import cv2
import math


def img_reversal(img_old_path, img_new_path, img_format='jpg'):
    """
        完成图像的翻转
    :param img_format:
    :param img_old_path: 原图像路径
    :param img_new_path: 新翻转的图像路径
    :return:
    """
    m_plot.imsave(img_new_path, numpy.array([i[::-1] for i in m_img.imread(img_old_path)]), format=img_format)


def img_reversal_cv2(img_old_path, img_new_path):
    cv2.imwrite(img_new_path, numpy.array([i[::-1] for i in cv2.imread(img_old_path)]))
    pass


def color_reversal(img_old_path, img_new_path):
    img_arr = [[[255 - k for k in j] for j in i] for i in cv2.imread(img_old_path)]
    img_arr_new = numpy.array(img_arr, dtype=numpy.uint8)
    m_plot.imsave(img_new_path, img_arr_new, format='jpg')
    pass


def color_reversal_cv2(img_old_path, img_new_path):
    """
        颜色翻转
    :param img_old_path:
    :param img_new_path:
    :return:
    """
    img_arr_new = [[[255-k for k in j] for j in i] for i in cv2.imread(img_old_path)]
    cv2.imwrite(img_new_path, numpy.array(img_arr_new))
    pass


def test_list():
    arr = [11, 22, 33, 44, 55, 66]
    arr_new = [(i, j) for i, j in enumerate(arr)]
    print(arr_new)
    pass


def test_plot(img_path):
    img_arr = m_img.imread(img_path)
    print(img_arr.shape)


def test_cv_write():
    help(cv2.imwrite)


def test_rgb():
    img_arr = numpy.array([[[0, 0.5, 0.25]]])
    m_plot.imshow(img_arr)
    m_plot.show()
    pass

def test_math():
    help(math)


def main():
    # img_reversal('djssg.jpg', 'djssg_revl_plot.jpg')
    # img_reversal_cv2('djssg.jpg', 'djssg_revl_cv2.jpg')
    color_reversal('djssg.jpg', 'djssg_crevl_cv2.jpg')
    # color_reversal('djssg_crevl_cv2.jpg', 'djssg_crevl_cv2_new.jpg')
    # test_list()
    # test_plot('djssg_revl_plot.jpg')
    # test_cv_write()
    # test_rgb()
    # test_math()
    pass


if __name__ == '__main__':
    main()
