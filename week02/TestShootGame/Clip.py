# -*- coding:utf-8 -*-
class Clip:
    """
        弹夹类
    """
    def __init__(self, max_num):
        self.__max = max_num
        self.__bullets = []

    def add_bullet(self, bullets):
        """
            将子弹添加到弹夹中
        :param bullets:
        :return:
        """
        if len(self.__bullets) < self.__max:
            self.__bullets.append(bullets)

    def get__max(self):
        return self.__max

    def get_bullets(self):
        return self.__bullets

    def __str__(self):
        return '%d/%d' % (len(self.__bullets), self.__max)


def main():
    clip = Clip(30)
    print(clip)
    pass


if __name__ == '__main__':
    main()
