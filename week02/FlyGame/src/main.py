# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time
import random


class Config(object):
    """
        游戏资源的配置类
    """
    __images_dict = {}

    @classmethod
    def load_resources(cls):
        Config.__images_dict['window_width'] = 595
        Config.__images_dict['window_height'] = 800
        Config.__images_dict['plane_hero'] = '../resource/image/plane.png'
        Config.__images_dict['plane_enemy'] = '../resource/image/small.png'
        Config.__images_dict['bullet_hero'] = '../resource/image/yellow_bullet.png'
        Config.__images_dict['bullet_enemy'] = '../resource/image/yellow_bullet.png'
        Config.__images_dict['bg'] = '../resource/image/img_bg03.png'

    @classmethod
    def get_resource(cls, key):
        return cls.__images_dict.get(key)


class GameObject(object):
    """
        所有游戏物体的基类
    """

    def __init__(self, screen_item, x, y, image_item):
        self.screen = screen_item
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_item)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


class BasePlane(GameObject):
    """
        所有飞机的基类
    """

    def __init__(self, screen_item, x, y, image_item):
        super().__init__(screen_item, x, y, image_item)
        self.bullets = []

    def display(self):
        super().display()
        for bullet in self.bullets:
            bullet.display()
            bullet.move()
            if bullet.isJudge():
                self.bullets.remove(bullet)


class BaseBullet(GameObject):
    """
        所有子弹的基类
    """

    def __init__(self, screen_item, x, y, image_item):
        super().__init__(screen_item, x, y, image_item)

    def move(self):
        pass

    def isJudge(self):
        pass


class HeroBullet(BaseBullet):
    def __init__(self, screen_item, x, y):
        super().__init__(screen_item, x, y, Config.get_resource('bullet_hero'))

    def move(self):
        self.y -= 5

    def isJudge(self):
        """是否越界"""
        return self.y < 0


class EnemyBullet(BaseBullet):
    def __init__(self, screen_item, x, y):
        super().__init__(screen_item, x, y, Config.get_resource('bullet_hero'))

    def move(self):
        self.y += 5

    def isJudge(self):
        return self.y >= 800


class HeroPlane(BasePlane):
    """
        玩家主角飞机
    """

    def __init__(self, screen_item):
        super().__init__(screen_item, 270, 700, Config.get_resource('plane_hero'))

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullets.append(HeroBullet(self.screen, self.x, self.y))
        print(len(self.bullets))


class EnemyPlane(BasePlane):
    """敌机"""

    def __init__(self, screen_item):
        super().__init__(screen_item, 0, 0, Config.get_resource('plane_enemy'))
        self.direction = 'right'

    def display(self):
        super().display()
        self.move()
        i = random.randint(0, 100)
        if i == 36 or i == 50:
            self.fire()

    def move(self):
        if self.x <= 0:
            self.direction = 'right'
        elif self.x >= 595:
            self.direction = 'left'

        if self.direction == 'right':
            self.x += 3
        elif self.direction == 'left':
            self.x -= 3

    def fire(self):
        self.bullets.append(EnemyBullet(self.screen, self.x, self.y))


def keyboard_listener(hero):
    for event in pygame.event.get():
        if event.type == QUIT:
            print('exit')
            exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                hero.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                hero.move_right()
            elif event.key == K_SPACE:
                hero.fire()


def main():
    # 加载资源
    Config.load_resources()
    # 1.创建窗口
    screen = pygame.display.set_mode((Config.get_resource('window_width'), Config.get_resource('window_height')), 0, 0)
    # 2.创建背景对象
    bg = GameObject(screen, 0, 0, Config.get_resource('bg'))
    # 3.创建主角
    hero = HeroPlane(screen)
    # 4.创建敌机
    enemy = EnemyPlane(screen)
    while True:
        bg.display()
        hero.display()
        enemy.display()
        # 添加键盘监听器
        keyboard_listener(hero)
        # 更新画面
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
