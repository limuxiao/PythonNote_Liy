# -*- coding:utf-8 -*-
class Cat:

    def __init__(self, name='Haha', age=12):
        self.name = name
        self.age = age
        # print('Cat starting....')
        pass

    def test(self):
        print('test...')

    def eat(self):
        print('eatint.....')

    def sleep(self):
        print('sleep.....')

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def compare(self, cat):
        if self.age >= cat.age:
            return True
        else:
            return False

    def __str__(self):
        return 'Name:%s,Age:%s'% (self.name, self.age)

def main():
    pass


if __name__ == '__main__':
    main()