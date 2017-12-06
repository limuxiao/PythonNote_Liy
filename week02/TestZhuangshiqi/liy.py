# -*- coding:utf-8 -*-
class ZSQ(object):
    def __init__(self):
        print('----ZSQ __init__ ----')

    @staticmethod
    def check_entry(func):
        def inner():
            print('----ZSQ check_entry----')
            func()
            pass

        return inner

    @staticmethod
    def check(has_arg=False):
        def inner(func):
            if has_arg:
                def arg_has(*args, **kwargs):
                    print('----has args----')
                    func(*args, **kwargs)
                    pass

                return arg_has
            else:
                def arg_no():
                    print('----no args----')
                    func()

                return arg_no

        return inner


@ZSQ.check_entry
def test01():
    print('----test01----')


@ZSQ.check(has_arg=False)
def test02():
    print('----test02----')


@ZSQ.check(has_arg=True)
def test03(*args, **kwargs):
    print('----test03----')
    print('args: %s ' % str(args))
    print('kwargs: %s' % str(kwargs))


def test04(*args, **kwargs):
    print('----test04----')
    print('args: %s ' % str(args))
    print('kwargs: %s' % str(kwargs))


@ZSQ.check(has_arg=True)
def test05(num):
    print('----test05: num: %s----' % str(num))


@ZSQ.check_entry
@ZSQ.check()
def test06():
    print('----test06----')


def main():
    # test01()
    # test02()
    # a = [11, 22, 33, 44]
    # b = {'name': 'laowang', 'age': 18}
    # test03(*a, **b)
    # test04(a, b)
    # test04(*a, **b)
    # test05(50)
    test06()
    pass


if __name__ == '__main__':
    main()
