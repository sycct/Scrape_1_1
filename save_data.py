#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests

from utils import connection_util


class SaveData(object):
    def __init__(self):
        self._target_url = 'https://www.pdflibr.com'
        self._init_connection = connection_util.ProcessConnection()

    def save_image(self):
        # 连接目标网站，获取内容
        get_content = self._init_connection.init_connection(self._target_url)
        if get_content:
            imageLocation = get_content.find("img", {"alt": "IP to Location"})["data-src"]
            real_path = self._target_url + imageLocation
            r = requests.get(real_path)
            with open("ip_location.png", 'wb') as f:
                f.write(r.content)


if __name__ == "__main__":
    SaveData().save_image()
