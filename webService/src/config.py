# -*- coding:utf-8 -*-
import logging
import time

config = {

    'page_size': 20,

}


class Log(object):
    file_name = './log/myapp_%s.log' % time.strftime('%Y-%m-%d', time.localtime(time.time()))

    handler = logging.FileHandler(filename=file_name, encoding='UTF-8')

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S ',
                        handlers=(handler,))

    @classmethod
    def info(cls, msg):
        logging.info(msg)
