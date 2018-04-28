# -*- coding:utf-8 -*-
import sqlite3
import pymysql



def f1():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE yzg_goods (id int, data char(50))
    ''')
    c.execute('''
        INSERT INTO yzg_goods values(1, 'haha')
    ''')

    c.execute('''
            INSERT INTO yzg_goods values(1, 'haha')
    ''')

    conn.commit()
    conn.close()
    pass


def f2():
    help(sqlite3)
    pass


def f3():
    # help(pymysql)
    connection = pymysql.connect(host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 password='123456',
                                 db='lmx',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)


def main():
    # f1()
    # f2()
    f3()
    pass


if __name__ == '__main__':
    main()
