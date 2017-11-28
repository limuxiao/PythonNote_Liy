# -*- coding:utf-8 -*-

# 定义名片列表
names = []


def print_title():
    """
        打印Title
    :return:
    """
    print('=' * 50)
    print('===', end='')
    print('名片管理系统'.center(38, ' '), end='')
    print('===')
    print('=' * 50)


def print_func(func):
    """
        打印一个功能
    :return:
    """
    print('* ', end='')
    print(func)
    pass


def print_menu():
    """
        打印名片管理系统的清单
    :return:
    """
    print_title()
    print_func('1.新增一个名片')
    print_func('2.修改一个名片')
    print_func('3.删除一个名片')
    print_func('4.查询一个名片')
    print_func('5.查询全部名片')
    print_func('6.退出系统')
    print('=' * 50)
    pass


def name_add():
    """
        新增一个名片
    :return:
    """
    name = input('清输入姓名：')
    age = input('请输入年龄：')
    gender = input('请输入性别：')
    names.append({'name': name, 'age': age, 'gender': gender})
    name_query_all()
    pass


def name_modify():
    """
        修改一个名片
    :return:
    """
    pass


def name_delete():
    """
        删除一个名片
    :return:
    """
    name = input('请输入要删除的名片的名字：')
    name_dels = []
    for n in names:
        if n['name'] == name:
            name_dels .append(n)

    if len(name_dels) <= 0:
        print('未找到您要删除的名片')
        return
    for n in name_dels:
        names.remove(n)
    name_query_all()


def name_query():
    """
        查询一个名片
    :return:
    """
    n = input('请输入你要查找的名片的名字：')
    has_name = False
    for name in names:
        if name['name'] != n:
            continue
        print('%s' % name['name'], end='\t')
        print('%s' % name['age'], end='\t')
        print('%s' % name['gender'])
        has_name = True

    if not has_name:
        print('未找到您要查询的名片')


def name_query_all():
    """
        查询名片列表
    :return:
    """
    print('姓名\t年龄\t性别')
    for name in names:
        print('%s'%name['name'], end='\t')
        print('%s' % name['age'], end='\t')
        print('%s' % name['gender'])
        pass


def has_name(name):
    for n in names:
        if n['name'] == name:
            return True
    else:
        return False


def main():
    """

    :return:
    """
    print_menu()
    while True:
        num = input('请输入功能序号：')
        if num == '1':
            name_add()
        elif num == '2':
            name_modify()
        elif num == '3':
            name_delete()
        elif num == '4':
            name_query()
        elif num == '5':
            name_query_all()
        elif num == '6':
            print('程序即将退出....')
            return
        else:
            print('您输入的功能序号有误，请重新输入')


if __name__ == '__main__':
    main()
