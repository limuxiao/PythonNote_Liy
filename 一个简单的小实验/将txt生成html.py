# -*- coding:utf-8 -*-
import os


def f1():
    f_txt = open('sss.txt', 'r', encoding='utf-8')
    s = f_txt.read()
    print(f_txt.name)
    new_name = 'sss.html'

    f_html = open(new_name, 'w', encoding='utf-8')
    f_html.write('''
<!doctype html>
    <html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
    ''')

    f_html.write('''
<h1>模块版本</h1>
    ''')

    modules = s.split('\n')
    for m in modules:
        f_html.write('''
        <span>%s</span><br>
        ''' % m)
        pass

    # f_html.write(s)

    f_html.write('''
</body>
</html>
    ''')

    f_txt.close()
    f_html.close()
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
