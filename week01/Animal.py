# -*- coding:utf-8 -*-

class Animal:
    def __init__(self):
        pass

    def eat(self):
        print('.....eating.....')


class C(Animal):

    def __init__(self, name='Haha', age=15):
        # Animal.__init__(self)
        super().__init__()
        pass

    def eat(self):
        print('=====eating=====')
        # Animal.eat(self)
        super().eat()

    def drake(self):
        print('.....drake.....')


def main():
    c = C()
    c.eat()
    c.drake()
    pass


if __name__ == '__main__':
    main()
