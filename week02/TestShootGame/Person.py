# -*- coding:utf-8 -*-
class Person(object):
    """
        人类
    """
    def __init__(self, name):
        self.__name = name      # 名称
        self.__gun = None       # 枪
        self.__hp = 100         # 血量
        pass

    def clip_2_gun(self, gun, clip):
        """
            将弹夹安装到枪支里
        :param gun: 枪
        :param clip: 弹夹
        :return:
        """
        gun.set_clip(clip)
        pass

    def bullet_2_clip(self, clip, bullet):
        """
            将子弹安装到弹夹里
        :param clip:    弹夹
        :param bullet:  子弹
        :return:
        """
        clip.add_bullet(bullet)
        pass

    def shoot(self, enemy):
        """
            射击敌人
        :param enemy:
        :return:
        """
        if self.__gun:
            self.__gun.shoot(enemy)

    def get_name(self):
        return self.__name

    def get_gun(self):
        return self.__gun

    def get_hp(self):
        return self.__hp

    def set_gun(self, gun):
        self.__gun = gun

    def set_hp(self, hp):
        self.__hp = hp

    def __str__(self):
        msg = '名称：%s\n血量：%s\n' % (self.__name, self.__hp)
        if self.__gun:
            msg += '携带：%s' % self.__gun
        return msg


def main():
    pass


if __name__ == '__main__':
    main()
