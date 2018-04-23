# -*- coding:utf-8 -*-
from urllib import request
from urllib import parse
import time
import math


class Param:
    """
        参数整合类
    """

    def __init__(self, keyword, cenX, cenY, batch=1, number=10, range=1500):
        """
        :param keyword:
        :param cenX:
        :param cenY:
        :param batch:
        :param number:
        :param range:
        """
        self.__params = {}
        self.__params['keyword'] = str(keyword)
        self.__params['batch'] = str(batch)
        self.__params['number'] = str(number)
        self.__params['sid'] = '1002'
        self.__params['mobile'] = '1'
        self.__params['map_cbc'] = 'on'
        self.__params['scheme'] = 'https'
        self.__params['cenX'] = str(cenX)
        self.__params['cenY'] = str(cenY)
        self.__params['range'] = str(range)
        self.__params['_'] = str(math.floor(time.time()))
        pass

    def __str__(self) -> str:
        return str(self.__params)

    def joinUrl(self, url) -> str:
        url_new = ''

        i = url.find('?')
        if i < 0:
            url_new = url + '?'
        else:
            url_new = url + '&'

        url_new += parse.urlencode(self.__params)
        return url_new



def f1():
    p = Param('便利店', '121.56483459', '31.24673653')
    s = p.joinUrl("https://restapi.map.so.com/newapi")
    print(s)

    # url = "https://restapi.map.so.com/newapi?keyword=%E4%BE%BF%E5%88%A9%E5%BA%97&batch=1&number=10&sid=1002&mobile=1&map_cbc=on&scheme=https&cenX=121.56483459&cenY=31.24673653&range=1500&_=1520390405025"
    # re = request.Request(url)
    # client = request.urlopen(re)
    # content = client.read()
    # print(content)
    pass


def f2():
    # help(request)
    params = {}
    params['keyword'] = '哈哈'
    print(params)
    s = parse.urlencode(params)
    print(s)
    pass


def testTime():
    print(math.floor(time.time()))


def main():
    f1()
    # f2()
    pass


if __name__ == '__main__':
    main()
