# -*- coding:utf-8 -*-
from multiprocessing import Pool
import webService.src.flask_main as fm
import webService.src.simpleserver as ss
from webService.src.db.dbhelper import DBHelper


def main():

    DBHelper.init()

    pool = Pool(2)
    pool.apply_async(fm.main)
    pool.apply_async(ss.main)

    pool.close()
    pool.join()
    pass


if __name__ == '__main__':
    main()
