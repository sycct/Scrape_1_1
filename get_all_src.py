#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os.path
import requests

from utils import connection_util


class GetAllSrc(object):
    def __init__(self):
        self._init_download_dir = 'downloaded'
        self.__targetUrl = 'https://www.scrapingbee.com/blog/'
        self._baseUrl = 'https://www.scrapingbee.com'
        self._init_connection = connection_util.ProcessConnection()

    @staticmethod
    def get_absolute_url(baseUrl, source):
        if source.startswith("https://www."):
            url = "https://www.scrapingbee.com" + source[27:]
        elif source.startswith("https://"):
            url = source
        elif source.startswith("www."):
            url = "https://" + source[4:]
        else:
            url = baseUrl + '/' + source
        if baseUrl not in source[0:27]:
            return None
        return url

    @staticmethod
    def get_download_path(baseUrl, absoluteUrl, download_dir):
        path = absoluteUrl.replace(baseUrl, "")
        path = download_dir + path
        directory = os.path.dirname(path)

        if not os.path.exists(directory):
            os.makedirs(directory)

        return path

    def download_main(self):
        get_content = self._init_connection.init_connection(self.__targetUrl)
        if get_content:
            download_list = get_content.findAll(src=True)
            for download in download_list:
                file_url = self.get_absolute_url(self._baseUrl, download["src"])
                if file_url is not None:
                    print(file_url)
                    r = requests.get(file_url)
                    with open(self.get_download_path(self._baseUrl, file_url, self._init_download_dir), 'wb') as f:
                        f.write(r.content)


if __name__ == '__main__':
    GetAllSrc().download_main()
