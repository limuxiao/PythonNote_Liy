# -*- coding:utf-8 -*-
import json
import os
import math
from threading import Thread
from flask import Flask, request, render_template, url_for, send_file, send_from_directory, Response
from webService.src.db.dbhelper import GoodItem
from webService.src.db.dbhelper import DBHelper

from webService.src.tools import Download
from webService.src.threadmanager import ThreadManager
from webService.src.config import config
from webService.src.config import Log

app = Flask(__name__)
DIR_PATH = os.path.join(os.getcwd(), 'imgs')


def response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/uploadImg', methods=['POST'])
def upload_img():
    """
        上传图片
    :return:
    """
    Log.info('*' * 25 + '接到请求: /uploadImg' + '*' * 25)
    try:
        params = request.form.to_dict()
        Log.info('upload_img:%s' % str(params))
        item = GoodItem(params)
    except:
        return response_headers(json.dumps({'returnCode': '9999', 'returnMessage': '参数异常'}))

    # 开启线程下载图片
    # ThreadManager.execute(target=downImgs, args=(item,))
    t = Thread(target=Download.downImgs, args=(item,))
    t.start()
    Log.info('*' * 25 + '结束请求' + '*' * 25)
    Log.info('\n')
    return response_headers(json.dumps({'returnCode': '0000', 'returnMessage': '操作成功'}))


@app.route('/', methods=['GET'])
def index():
    Log.info('*' * 25 + '收到访问请求: /' + '*' * 25)
    count = DBHelper.select_count()
    Log.info('数据总量：%d' % count)
    data = [i + 1 for i in range(math.ceil(count / config['page_size']))]
    Log.info('*' * 25 + '请求处理完毕' + '*' * 25)
    return render_template('index.html', data=data)


@app.route('/items/<page>', methods=['GET'])
def items(page=None):
    """
        分页查询
    :param page:
    :return:
    """
    Log.info('*' * 25 + '收到访问请求: /items/%s' % str(page) + '*' * 25)
    if page is None:
        return 'page is None'
    else:
        data = DBHelper.select_items(page=int(page), page_size=config['page_size'])
        return render_template('items.html', data=data)


@app.route('/htmls/common.css', methods=['GET'])
def get_common_css():
    return send_from_directory('htmls', 'common.css')


@app.route('/htmls/common.js', methods=['GET'])
def get_common_js():
    return send_from_directory('htmls', 'common.js')


@app.route('/htmls/jquery-3.3.1.js', methods=['GET'])
def get_jquery():
    return send_from_directory('htmls', 'jquery-3.3.1.js')


def main():
    DBHelper.init()
    app.run(host='0.0.0.0', port='9090')
    # l = DBHelper.select_items()
    # print(l[0])
    pass


if __name__ == '__main__':
    main()
