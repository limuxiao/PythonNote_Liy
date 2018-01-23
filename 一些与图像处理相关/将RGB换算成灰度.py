# -*- coding:utf-8 -*-


def gary_float(r, g, b):
    """
        通过浮点型算法计算灰度
    :param r:  红色色值
    :param g:  绿色色值
    :param b:  蓝色色值
    :return:   灰度值
    """
    return int(r * 0.30 + g * 0.59 + b * 0.11)


def gary_int(r, g, b):
    """
        通过整数算法计算灰度
    :param r: 红色色值
    :param g: 绿色色值
    :param b: 蓝色色值
    :return:  灰度值
    """
    return int((r * 30 + g * 59 + b * 11) / 100)


def gary_move(r, g, b):
    """
        通过移位算法计算灰度
    :param r: 红色色值
    :param g: 绿色色值
    :param b: 蓝色色值
    :return:  灰度值
    """
    return int((r * 76 + g * 151 + b * 28) >> 8)


def gary_average(r, g, b):
    """
        通过平均值算法计算灰度
    :param r:  红色色值
    :param g:  绿色色值
    :param b:  蓝色色值
    :return:   灰度值
    """
    return int((r + g + b) / 3)


def gary_green(r, g, b):
    """
        通过仅取绿色法计算灰度
    :param r: 红色色值
    :param g: 绿色色值
    :param b: 蓝色色值
    :return:  灰度值
    """
    return g


def f1():
    r = 200
    g = 88
    b = 120
    print('浮点算法结果：%d' % gary_float(r, g, b))
    print('整数算法结果：%d' % gary_int(r, g, b))
    print('位移算法结果：%d' % gary_move(r, g, b))
    print('均值算法结果：%d' % gary_average(r, g, b))
    print('取绿算法结果：%d' % gary_green(r, g, b))
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
