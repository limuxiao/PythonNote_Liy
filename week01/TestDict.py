# -*- coding:utf-8 -*-


def testDict01():
    infos = {'name': 'laowang', 'age': 18}
    for key in infos.keys():
        print(key)

    for value in infos.values():
        print(value)

    infos.setdefault('gender', '1')
    gender = infos.get('gender')
    print(gender)
    print(infos)
    if 'name' in infos:
        print('name 在 infos里面 name:%s'%infos['name'])
    print(infos)
    pass


def main():
    testDict01()
    pass


if __name__ == '__main__':
    main()
