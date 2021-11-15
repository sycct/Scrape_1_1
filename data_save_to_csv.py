# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os
from os import path

from utils import connection_util
from config import logger_config


class DataSaveToCSV(object):
    def __init__(self):
        self._init_download_dir = 'downloaded'
        self._target_url = 'https://www.scrapingbee.com/blog/'
        self._baseUrl = 'https://www.scrapingbee.com'
        self._init_connection = connection_util.ProcessConnection()
        logging_name = 'write_csv'
        init_logging = logger_config.LoggingConfig()
        self._logging = init_logging.init_logging(logging_name)

    @staticmethod
    def save_data():
        get_path = path.join(os.getcwd(), 'files')
        if not path.exists(get_path):
            os.makedirs(get_path)
        csv_file = open(get_path + '\\test.csv', 'w+', newline='')
        try:
            writer = csv.writer(csv_file)
            writer.writerow(('number', 'number plus 2', 'number times 2'))
            for i in range(10):
                writer.writerow((i, i + 2, i * 2))
        finally:
            csv_file.close()

    def scrape_data_to_csv(self):
        get_path = path.join(os.getcwd(), 'files')
        if not path.exists(get_path):
            os.makedirs(get_path)
        with open(get_path + '\\article.csv', 'w+', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(('标题', '发布时间', '内容概要'))
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
                    writer.writerow((get_title, get_release_date, get_description))
            else:
                self._logging.warning('为获取到文章任何内容，请检查！')


if __name__ == '__main__':
    DataSaveToCSV().save_data()
