# -*- coding:utf-8 -*-
import os
import random


def testFile01():
    file = open('TestNi.py', 'rb')
    print(file.readline())
    file.seek(0)
    print(file.readline())
    file.close()
    pass


def testFile02():
    f = open('test.txt', 'w+')
    f.write('i test')
    f.write('\nhaha')
    f.flush()
    f.close()
    pass


def testFile03():
    f = open('test.txt', 'r')
    print(f.read())
    f.close()


def testFile04():
    f = open('test.txt')
    pos = f.name.rfind('.')
    name_new = f.name[:pos] + '[附件]' + f.name[pos:]
    print(f.encoding)
    help(f)
    f1 = open(name_new, 'w')
    f1.write(f.read())
    f.close()
    f1.close()


def testFile05():
    f = open('test.txt', 'w', encoding='gbk')
    f.write('i test')
    f.close()
    f1 = open('test.txt')
    print(f1.read(), 'r', encoding='gbk')
    f1.close()


def testFile06():
    f = open('test.txt')
    print(f.read(4))
    print(f.tell())
    f.seek(0, 0)
    print(f.tell())
    f.close()
    pass


def testFile07():
    print(os.path.abspath('.'))
    # os.remove('test.txt')
    # os.remove('text.txt')
    print(os.listdir('.'))
    pass


def testFile08():
    print(os.name)
    print(os.curdir)
    print(os.listdir())
    if not os.path.exists('test'):
        os.mkdir('test')
    os.chdir('test')
    print(os.curdir)
    print(os.listdir())
    pass


def testFile09():
    # print(os.ctermid)
    # for n in os.environ.items():
    #     print(n)
    # print(os.getcwd())
    # os.chdir('test')
    # print(os.getcwd())
    # print(os.environ['JAVA_HOME'])
    # os.environ['JAVA_HOME'] = 'D:\jdk'
    # print(os.environ['JAVA_HOME'])
    # help(os.fsencode)
    # print(os.fspath(os.getcwd()))
    # print(os.getenv('JAVA_HOME', 'D:\\test'))
    print(os.getpid())
    print(os.getppid())
    print(os.get_terminal_size)


def main():
    # testFile01()
    # testFile02()
    # testFile03()
    # testFile04()
    # testFile05()
    # testFile06()
    # testFile07()
    # testFile08()
    testFile09()
    pass


if __name__ == '__main__':
    main()
