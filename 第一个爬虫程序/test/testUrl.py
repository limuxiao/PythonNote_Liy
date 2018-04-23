# -*- coding:utf-8 -*-
from urllib.request import urlopen
import http.client


def f1():
    my_url = "https://vps.beta.ule.com/vpsUzsMobile/yzs/user/testInfo.do"
    client = urlopen(my_url)
    content = client.read()
    print(content)
    client.close()
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
