# -*- coding:utf-8 -*-
import cv2


class ShowTool(object):

    @classmethod
    def show_by_cv2(cls, img_name, img_bgr):
        cv2.imshow(img_name, img_bgr)
        cv2.waitKey(0)


def main():
    pass


if __name__ == '__main__':
    main()
