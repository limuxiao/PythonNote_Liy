# -*- coding:utf-8 -*-
class Gun:
    """
        枪类
    """
    def __init__(self, name):
        self.__name = name
        self.__clip = None

    def shoot(self, enemy):
        if self.__clip:
            bullet = self.__clip.get_bullets().pop()
            if bullet:
                bullet.hurt_enemy(enemy)

    def get_name(self):
        return self.__name

    def get_clip(self):
        return self.__clip

    def set_clip(self, clip):
        self.__clip = clip

    def __str__(self):
        msg = '%s' % self.__name
        if self.__clip:
            msg += ' %s' % self.__clip
        return msg


def main():
    pass


if __name__ == '__main__':
    main()
