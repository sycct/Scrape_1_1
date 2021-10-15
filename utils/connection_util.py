# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import exceptions
import requests
from bs4 import BeautifulSoup

from config import logger_config


class ProcessConnection:
    def __init__(self):
        logger_name = 'crawler'
        self._logger_write_file = logger_config.LoggingConfig().init_logging(logger_name)

    def init_connection(self, uri):
        # 连接网站
        try:
            session = requests.session()
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
            html = session.get(uri, headers=headers)
        except (exceptions.ConnectionError, exceptions.HTTPError, exceptions.Timeout) as e:
            self._logger_write_file.error(f'执行 init_connection 函数出错，具体错误内容：{e}')
            return False
        try:
            bsObj = BeautifulSoup(html.text, features='html.parser')
            return bsObj
        except AttributeError as e:
            self._logger_write_file.error(f'执行 init_connection 函数出错，具体错误内容：{e}')
            return False
