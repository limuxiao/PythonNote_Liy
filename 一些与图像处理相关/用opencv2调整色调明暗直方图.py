# -*- coding:utf-8 -*-
"""

    除了区域，图像本身的属性操作也非常多，比如可以通过HSV空间对色调和明暗进行调节。
    HSV空间是由美国的图形学专家A. R. Smith提出的一种颜色空间，HSV分别是色调（Hue），饱和度（Saturation）和明度（Value）。
    在HSV空间中进行调节就避免了直接在RGB空间中调节是还需要考虑三个通道的相关性。
    OpenCV中H的取值是[0, 180)，其他两个通道的取值都是[0, 256)，下面例子接着上面例子代码，通过HSV空间对图像进行调整


    # 通过cv2.cvtColor把图像从BGR转换到HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # H空间中，绿色比黄色的值高一点，所以给每个像素+15，黄色的树叶就会变绿
    turn_green_hsv = img_hsv.copy()
    turn_green_hsv[:, :, 0] = (turn_green_hsv[:, :, 0]+15) % 180
    turn_green_img = cv2.cvtColor(turn_green_hsv, cv2.COLOR_HSV2BGR)
    cv2.imwrite('turn_green.jpg', turn_green_img)

    # 减小饱和度会让图像损失鲜艳，变得更灰
    colorless_hsv = img_hsv.copy()
    colorless_hsv[:, :, 1] = 0.5 * colorless_hsv[:, :, 1]
    colorless_img = cv2.cvtColor(colorless_hsv, cv2.COLOR_HSV2BGR)
    cv2.imwrite('colorless.jpg', colorless_img)

    # 减小明度为原来一半
    darker_hsv = img_hsv.copy()
    darker_hsv[:, :, 2] = 0.5 * darker_hsv[:, :, 2]
    darker_img = cv2.cvtColor(darker_hsv, cv2.COLOR_HSV2BGR)
    cv2.imwrite('darker.jpg', darker_img)

"""

import cv2
import math

from 一些与图像处理相关.ShowTool import ShowTool


def test_rgb2hsv():

    # help(cv2.cvtColor)

    img_arr = cv2.imread('djssg.jpg')
    img_hsv = cv2.cvtColor(img_arr, code=cv2.COLOR_RGB2HSV)

    # 调整色调
    img_hsv[:, :, 0] = (img_hsv[:, :, 0] - 180) % 180

    # 调整饱和度
    img_hsv[:, :, 1] = (1.5 * img_hsv[:, :, 1]) % 256

    # 调整明暗
    img_hsv[:, :, 2] = (1 * img_hsv[:, :, 2]) % 256

    img_arr_new = cv2.cvtColor(img_hsv, code=cv2.COLOR_HSV2RGB)
    img_arr_new = cv2.resize(img_arr_new, dsize=(0, 0), fx=0.3, fy=0.3)
    ShowTool.show_by_cv2('img_arr', img_arr_new)

    pass


def main():
    test_rgb2hsv()
    pass


if __name__ == '__main__':
    main()
