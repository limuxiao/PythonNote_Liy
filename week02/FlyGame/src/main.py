# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time

def main():
    # help(pygame)
    # 1.创建窗口
    screen = pygame.display.set_mode((595, 800), 0, 32)
    # 2.创建一个背景图片
    bg = pygame.image.load('../resource/image/img_bg03.png')
    pygame.event.get()
    while True:
        # 3.将背景图设置到屏幕中去
        screen.blit(bg, (0, 0))
        # 更新画面
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                print('exit')
                exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    print('按了A键盘')


        time.sleep(0.01)
        pass


if __name__ == '__main__':
    main()
