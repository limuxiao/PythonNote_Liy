# -*- coding:utf-8 -*-
import matplotlib.pyplot as mplt
import matplotlib.image as mimg


def f1():
    lena = mimg.imread('test2.png')
    # print(lena)
    # help(lena)
    print(len(lena))
    print(len(lena[0]))
    print(len(lena[0][0]))
    print(lena.shape)
    mplt.imshow(lena)

    # mplt.axis('off')
    # mplt.show()


def f2():
    lena = mimg.imread('test2.png')
    lena_1 = lena[:, :, 0]
    print(lena[0][0])
    print(len(lena_1[0]))
    mplt.imshow(lena_1, cmap='Greys_r')
    mplt.show()
    pass


def f3():
    lena = mimg.imread('test2.png')
    lena_0 = lena[:, :, 0]
    print(lena_0)
    pass


def main():
    # f1()
    # f2()
    f3()
    pass


if __name__ == '__main__':
    main()
