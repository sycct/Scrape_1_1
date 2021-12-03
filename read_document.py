#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from requests import Session


class ReadDocument(object):
    def __init__(self):
        self._text_url = 'https://image.pdflibr.com/crawler/blog/tencent_cloud_ip_range.txt'

    def read_text_document(self):
        init_session = Session()
        response = init_session.get(url=self._text_url)
        # 显示原来文本的编码方式
        print(response.encoding)
        # 将文本设置成 utf-8 的编码方式
        response.encoding = 'utf-8'
        print(response.text)
        # 显示改变编码后的编码方式
        print(response.encoding)


if __name__ == '__main__':
    ReadDocument().read_text_document()
