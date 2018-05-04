# -*- coding:utf-8 -*-
import json
import os
import requests
from threading import Thread
from flask import Flask, request, render_template, url_for, send_file, send_from_directory, Response
from webService.src.db.dbhelper import GoodItem
from webService.src.db.dbhelper import DBHelper
from webService.src.tools import Log
from webService.src.threadmanager import ThreadManager

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
    Log.info('*' * 25 + '接到请求' + '*' * 25)
    try:
        params = request.form.to_dict()
        Log.info('upload_img:%s' % str(params))
        item = GoodItem(params)
    except:
        return response_headers(json.dumps({'returnCode': '9999', 'returnMessage': '参数异常'}))

    # 开启线程下载图片
    # ThreadManager.execute(target=downImgs, args=(item,))
    t = Thread(target=downImgs, args=(item,))
    t.start()
    Log.info('*' * 25 + '结束请求' + '*' * 25)
    Log.info('\n')
    return response_headers(json.dumps({'returnCode': '0000', 'returnMessage': '操作成功'}))


# 下载图片
def downImgs(item):

    img_front_status, img_side_status, img_obverse_status = '0', '0', '0'

    # 正面
    if item.img_front:
        Log.info('开始下载图片：upc:%s, 图片类型：正面， 链接：%s' % (item.good_upc, item.img_front))
        rs = downloadImg(item.img_front, '%s_100' % item.good_upc)
        if rs:
            item.img_front_local = rs
            img_front_status = '1'
            Log.info('图片下载成功：upc:%s, 图片类型：正面， 链接：%s' % (item.good_upc, item.img_front))
        else:
            Log.info('图片下载失败：upc:%s, 图片类型：正面， 链接：%s' % (item.good_upc, item.img_front))

    # 侧面
    if item.img_side:
        Log.info('开始下载图片：upc:%s, 图片类型：侧面， 链接：%s' % (item.good_upc, item.img_side))
        rs = downloadImg(item.img_side, '%s_010' % item.good_upc)
        if rs:
            item.img_side_local = rs
            img_side_status = '1'
            Log.info('图片下载成功：upc:%s, 图片类型：侧面， 链接：%s' % (item.good_upc, item.img_side))
        else:
            Log.info('图片下载失败：upc:%s, 图片类型：侧面， 链接：%s' % (item.good_upc, item.img_side))

    # 反面
    if item.img_obverse:
        Log.info('开始下载图片：upc:%s, 图片类型：反面， 链接：%s' % (item.good_upc, item.img_obverse))
        rs = downloadImg(item.img_obverse, '%s_001' % item.good_upc)
        if rs:
            item.img_obverse_local = rs
            img_obverse_status = '1'
            Log.info('图片下载成功：upc:%s, 图片类型：反面， 链接：%s' % (item.good_upc, item.img_obverse))
        else:
            Log.info('图片下载失败：upc:%s, 图片类型：反面， 链接：%s' % (item.good_upc, item.img_obverse))

    item.status = img_front_status + img_side_status + img_obverse_status
    Log.info('待保存的商品信息：%s' % item)
    # 保存到数据库里
    DBHelper.insert_item(item)


def downloadImg(img_url, img_name) -> str:
    filename = os.path.join(DIR_PATH, img_name)
    try:
        res = requests.get(img_url, timeout=15)
        if str(res.status_code)[0] == '4':
            return None
    except:
        return None

    f = open(filename + '.jpg', 'wb')
    f.write(res.content)
    f.close()
    return img_name


def main():
    app.run(host='0.0.0.0', port='9090')
    pass


if __name__ == '__main__':
    main()
