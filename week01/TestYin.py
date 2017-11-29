# -*- coding:utf-8 -*-


def testYin01():
    a = 100
    b = a
    print(id(a))
    print(id(b))

    A = [11,22,33]
    B = A
    B.append(44)
    print(A)
    print(B)
    print(id(A))
    print(id(B))

    b = 200
    print(a)
    print(b)
    print(id(a))
    print(id(b))

    pass


def main():
    testYin01()
    pass


if __name__ == '__main__':
    main()