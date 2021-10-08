#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from utils import connection_util


class Scraping(object):

    def __init__(self):
        self._init_url = 'https://www.pdflibr.com'

    def get_my_ip(self):
        connection = connection_util.ProcessConnection()
        get_content = connection.init_connection(self._init_url)
        get_ip_wrap = get_content.findAll("a", {"class": "ip-info-content-container"})
        for item in get_ip_wrap:
            result = item.findAll("div", {"class": "right-result"})
            for child in result:
                get_ip = child.get_text()
                print(get_ip)


if __name__ == '__main__':
    Scraping().get_my_ip()
