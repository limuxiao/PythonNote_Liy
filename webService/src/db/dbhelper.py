# -*- coding:utf-8 -*-
import sqlite3
from webService.src.tools import Log
import threading
import time

TABLE_NAME = 'items'

CREATE_SQL = '''
            CREATE TABLE IF NOT EXISTS %s(
                good_id VARCHAR(20) PRIMARY KEY NOT NULL, 
                good_name VARCHAR(50),
                good_upc VARCHAR(20) NOT NULL,
                good_first VARCHAR(20),
                good_second VARCHAR(20),
                good_third VARCHAR(20),
                good_desc VARCHAR(50),
                good_price VARCHAR(20),
                good_p VARCHAR(20),
                good_c VARCHAR(20),
                good_x VARCHAR(20),
                img_front VARCHAR(200),
                img_side VARCHAR(200),
                img_obverse VARCHAR(200),
                create_time VARCHAR(20),
                status VARCHAR(3),
                img_front_local VARCHAR(100),
                img_side_local VARCHAR(100),
                img_obverse_local VARCHAR(100)
            )
''' % TABLE_NAME


class GoodItem(object):
    """
        商品类
    """

    def __init__(self, info={}):
        self.good_name = info.get('good_name')
        self.good_upc = info.get('good_upc')
        self.good_first = info.get('good_first')
        self.good_second = info.get('good_second')
        self.good_third = info.get('good_third')
        self.good_desc = info.get('good_desc')
        self.good_price = info.get('good_price')
        self.good_id = info.get('good_id')
        self.good_p = info.get('good_p')
        self.good_c = info.get('good_c')
        self.good_x = info.get('good_x')
        self.img_front = info.get('img_front')
        self.img_side = info.get('img_side')
        self.img_obverse = info.get('img_obverse')
        self.status = '000'
        self.img_front_local = ''
        self.img_side_local = ''
        self.img_obverse_local = ''


class DBHelper(object):
    """
        数据库连接工具
    """
    conn = sqlite3.connect('data.db', check_same_thread=False)
    cursor = conn.cursor()
    lock = threading.Lock()

    @classmethod
    def init(cls):
        cls.create_table()

        pass

    @classmethod
    def create_table(cls):
        cls.cursor.execute(CREATE_SQL)
        Log.info('数据库初始化完成')

    @classmethod
    def insert_or_update(cls, item):
        items = cls.select_item('good_upc', item.good_upc)
        if items:
            cls.update_item(item)
        else:
            cls.insert_item(item)

    @classmethod
    def select_item(cls, key='', value=''):
        """
            根据某一列查询商品
        :param key:
        :param value:
        :return:
        """

        select_sql = '''
            SELECT * FROM %s where %s = %s
        ''' % (TABLE_NAME, key, value)
        return cls.cursor.execute(select_sql)

    @classmethod
    def insert_item(cls, item):
        """
            插入一条商品信息
        :param item:
        :return:
        """
        cls.lock.acquire()      # 加线程锁
        cls.conn.execute("BEGIN TRANSACTION")       # 开启事务
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        insert_sql = '''
            INSERT INTO %s (good_id, good_name, good_upc, good_first, good_second
            , good_third, good_desc, good_price, good_p, good_c, good_x, img_front
            , img_side, img_obverse, img_front_local, img_side_local, img_obverse_local,create_time, status)
             VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'
             , '%s', '%s', '%s', '%s', '%s', '%s')
        ''' % (TABLE_NAME,  item.good_id, item.good_name, item.good_upc, item.good_first, item.good_second
               , item.good_third, item.good_desc, item.good_price, item.good_p, item.good_c, item.good_x, item.img_front
               , item.img_side, item.img_obverse, item.img_front_local, item.img_side_local, item.img_obverse_local
               , time_str, item.status)
        cls.cursor.execute(insert_sql)
        cls.conn.execute("COMMIT")                  # 结束事务
        Log.info('数据库保存商品成功：商品名：%s, upc: %s, 状态：%s' % (item.good_name, item.good_upc, item.status))
        cls.lock.release()  # 释放锁

    @classmethod
    def update_item(cls, item):
        """
            更新一条商品信息
        :param item:
        :return:
        """
        cls.lock.acquire()  # 加线程锁
        cls.conn.execute("BEGIN TRANSACTION")  # 开启事务
        update_sql = '''
            UPDATE items SET
        '''
        cls.cursor.execute(update_sql)
        cls.conn.execute("COMMIT")  # 结束事务
        cls.lock.release()      # 释放锁


def main():
    DBHelper.init()
    item = GoodItem({'good_id': '01', 'good_name': '商品名称', 'good_upc': '123456789'})
    DBHelper.insert_item(item)
    pass


if __name__ == '__main__':
    main()
