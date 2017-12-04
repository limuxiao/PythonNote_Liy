# -*- coding:utf-8 -*-
class Bullet:
    """子弹类"""
    def __init__(self, hurt):
        self.__hurt = hurt

    def hurt_enemy(self, enemy):
        """
            命中敌人，给敌人造成伤害
        :param enemy:
        :return:
        """
        enemy.set_hp(enemy.get_hp() - self.get_hurt())

    def get_hurt(self):
        return self.__hurt


def main():
    pass


if __name__ == '__main__':
    main()
