# -*- coding:utf-8 -*-
import matplotlib.pyplot as m_plot
import matplotlib.image as m_img
import numpy
import cv2


def img_reversal(img_old_path, img_new_path, format='jpg'):
    """
        完成图像的翻转
    :param format:
    :param img_old_path: 原图像路径
    :param img_new_path: 新翻转的图像路径
    :return:
    """
    m_plot.imsave(img_new_path, numpy.array([i[::-1] for i in m_img.imread(img_old_path)]), format=format)


def img_reversal_cv2(img_old_path, img_new_path):
    cv2.imwrite(img_new_path, numpy.array([i[::-1] for i in m_img.imread(img_old_path)]))
    pass


def color_reversal(img_old_path):
    img_arr = m_img.imread(img_old_path)
    img_w, img_h, img_d = img_arr.shape
    img_arr_new = []
    for i in img_arr:
        img_row = []

    pass


def test_list():
    arr = [11, 22, 33, 44, 55, 66]
    arr_new = [(i, j) for i, j in enumerate(arr)]
    print(arr_new)
    pass


def test_plot(img_path):
    img_arr = m_img.imread(img_path)
    print(img_arr.shape)


def main():
    img_reversal('djssg.jpg', 'djssg_revl_plot.jpg') 
    # img_reversal_cv2('djssg.jpg', 'djssg_revl_cv2.jpg')
    # color_reversal('djssg.jpg')
    # test_list()
    # test_plot('djssg_revl_plot.jpg')
    pass


if __name__ == '__main__':
    main()
