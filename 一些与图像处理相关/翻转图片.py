# -*- coding:utf-8 -*-
import matplotlib.pyplot as m_plot
import matplotlib.image as m_img
import numpy


def img_reversal(img_old_path, img_new_path):
    """
        完成图像的翻转
    :param img_old_path: 原图像路径
    :param img_new_path: 新翻转的图像路径
    :return:
    """
    m_plot.imsave(img_new_path, numpy.array([i[::-1] for i in m_img.imread(img_old_path)]))


def main():
    img_reversal('djssg.jpg', 'djssg_revl.jpg')
    pass


if __name__ == '__main__':
    main()
