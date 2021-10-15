#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from utils import connection_util


class DataCollection(object):
    def __init__(self):
        self._target_url = 'https://www.scrapingbee.com/blog/'
        self._init_connection = connection_util.ProcessConnection()

    def main(self):
        # 连接目标网站，获取内容
        get_content = self._init_connection.init_connection(self._target_url)
        if get_content:
            parent = get_content.findAll("section", {"class": "section-sm"})[0]
            get_row = parent.findAll("div", {"class": "col-lg-12 mb-5 mb-lg-0"})[0]
            get_child_item = get_row.findAll("div", {"class": "col-md-4 mb-4"})
            for item in get_child_item:
                # 获取标题文字
                get_title = item.find("a", {"class": "h5 d-block mb-3 post-title"}).get_text()
                # 获取发布时间
                get_release_date = item.find("div", {"class": "mb-3 mt-2"}).findAll("span")[1].get_text()
                # 获取文章描述
                get_description = item.find("p", {"class": "card-text post-description"}).get_text()
                print(get_title)
                print(get_release_date)
                print(get_description)


if __name__ == '__main__':
    DataCollection().main()
