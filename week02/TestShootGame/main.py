# -*- coding:utf-8 -*-
from week02.TestShootGame.Bullet import Bullet
from week02.TestShootGame.Clip import Clip
from week02.TestShootGame.Gun import Gun
from week02.TestShootGame.Person import Person


def game_start():
    # 1.create player
    player = Person('射手')
    # 2.set gun to player
    player.set_gun(Gun('AK47'))
    # 3.put bullets to clip
    clip = Clip(30)
    for i in range(clip.get__max()):
        bullet = Bullet(10)
        player.bullet_2_clip(clip, bullet)
    # 4.put clip to gun
    player.clip_2_gun(player.get_gun(), clip)
    # 5.create a enemy
    enemy = Person('敌人')
    # 6. shoot enemy
    player.shoot(enemy)
    player.shoot(enemy)
    player.shoot(enemy)
    player.shoot(enemy)
    print(player)
    print(enemy)
    pass


def main():
    game_start()
    pass


if __name__ == '__main__':
    main()
