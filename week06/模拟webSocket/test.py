# -*- coding:utf-8 -*-
import zipfile


def f1():
    pass
    # h1 = 0x85
    # h2 = 0x7f
    # print(type(h1 & h2))
    # print(hex(h1 & h2))
    # print(133 & h2)
    # print(hex(ord(chr(h1))))
    # print(''.join(chr(h1)))
    # print(0xc3)
    # a = [230, 136, 145, 229, 176, 177, 232, 175, 149, 232, 175, 149, 231, 156, 139]
    # b = bytes(a)
    # print(b)
    # s = b.decode('utf-8')
    # print(s)
    print(0x82 & 0x7f)


def f2():
    recv_b = bytes('1234', encoding='utf-8')
    print(recv_b)
    print(len(recv_b))
    print(hex(len(recv_b)))
    recv_l = [0x81, 0x4]
    for r in recv_b:
        recv_l.append(r)
    print(recv_l)
    print(type(recv_b))
    recv_l = bytes(recv_l)
    print(type(recv_l))
    print(recv_l)
    pass


def f3():
    help(zipfile)
    pass


def f4():
    a = [4, 5, 6, 4, 6, 5, 1, 8, 6, 4, 6, 1]
    print(a)
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if a[i] > a[j]:
                t = a[i]
                a[i] = a[j]
                a[j] = t
    print(a)


def f5():
    recv_list = [0x88]
    print(bytes(recv_list))
    pass


def main():
    # f1()
    # f2()
    # f3()
    # f4()
    f5()
    pass


if __name__ == '__main__':
    main()
