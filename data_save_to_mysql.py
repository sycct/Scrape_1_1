# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
import os
from dotenv import load_dotenv

from config import logger_config
from utils import connection_util


class DataSaveToMySQL(object):
    def __init__(self):
        # loading env config file
        dotenv_path = os.path.join(os.getcwd(), '.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        # MySQL config
        self._host = os.environ.get('MYSQL_HOST')
        self._port = int(os.environ.get('MYSQL_PORT'))
        self._user = os.environ.get('MYSQL_USER')
        self._password = os.environ.get('MYSQL_PASSWORD')
        self._db = os.environ.get('MYSQL_DATABASES')

        self._target_url = 'https://www.scrapingbee.com/blog/'
        self._baseUrl = 'https://www.scrapingbee.com'
        self._init_connection = connection_util.ProcessConnection()
        logging_name = 'store_mysql'
        init_logging = logger_config.LoggingConfig()
        self._logging = init_logging.init_logging(logging_name)

    def scrape_data(self):
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
                self.article_save_mysql(title=get_title, description=get_description)
        else:
            self._logging.warning('为获取到文章任何内容，请检查！')

    def mysql_query_demo(self):
        conn = pymysql.connect(host=self._host, port=self._port, user=self._user, password=self._password, db=self._db)
        cur = conn.cursor()
        cur.execute("SELECT * FROM articles WHERE id=4;")
        print(cur.fetchone())
        cur.close()
        conn.close()

    def article_save_mysql(self, title, description):
        connection = pymysql.connect(host=self._host, port=self._port, user=self._user, password=self._password,
                                     db=self._db)
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO articles (title,summary) VALUES (%s,%s);"
            cursor.execute(sql, (title, description))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()


if __name__ == '__main__':
    DataSaveToMySQL().scrape_data()
