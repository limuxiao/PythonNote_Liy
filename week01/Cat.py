# -*- coding:utf-8 -*-

class Cat:

<<<<<<< HEAD

=======
    def __init__(self, name='Haha', age=12):
        self.name = name
        self.age = age
        # print('Cat starting....')
        pass
>>>>>>> f1fbd30ec43428464f9aa0c188185343f876cf14

    def test(self):
        print('test...')

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

    def printName(self):
        print(self.name)

def main():
    pass


if __name__ == '__main__':
    main()