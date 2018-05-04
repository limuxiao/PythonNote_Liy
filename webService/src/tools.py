# -*- coding:utf-8 -*-

import logging


class Log(object):
    handler = logging.FileHandler(filename='myapp.log', encoding='UTF-8')

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S ',
                        handlers=(handler,))

    @classmethod
    def info(cls, msg):
        logging.info(msg)


def main():
    pass


if __name__ == '__main__':
    main()
