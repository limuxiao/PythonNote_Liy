# -*- coding:utf-8 -*-
import sqlite3


def f1():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
