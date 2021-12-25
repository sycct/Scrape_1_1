#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re
import string
from collections import OrderedDict

from utils import connection_util


class DataCleaning(object):
    def __init__(self):
        self._target_url = 'https://en.wikipedia.org/wiki/python_(programming_language)'
        self._init_connection = connection_util.ProcessConnection()

    def ngrams(self, input, n):
        input = self.clean_input(input)
        output = []
        for i in range(len(input) - n + 1):
            output.append(input[i:i + n])
        return output

    def getNgrams(self, input, n):
        input = self.clean_input(input)
        output = dict()
        for i in range(len(input) - n + 1):
            newNGram = " ".join(input[i:i + n])
            if newNGram in output:
                output[newNGram] += 1
            else:
                output[newNGram] = 1
        return output

    @staticmethod
    def clean_input(input):
        input = input.upper()
        input = re.sub('\n+', " ", input)
        input = re.sub('\[[0-9]*\]', "", input)
        input = re.sub(' +', " ", input)
        input = bytes(input, "UTF-8")
        input = input.decode("ascii", "ignore")
        input = input.split(' ')
        clean_input = []
        for item in input:
            # string.punctuation 获取所有的标点符号
            item = item.strip(string.punctuation)
            if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
                clean_input.append(item)
        return clean_input

    def get_result(self):
        # 连接目标网站，获取内容
        get_content = self._init_connection.init_connection(self._target_url)
        if get_content:
            content = get_content.find("div", {"id": "mw-content-text"}).get_text()
            ngrams = self.getNgrams(content, 2)
            ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
            print(ngrams)
            print("2-grams count is: " + str(len(ngrams)))


if __name__ == '__main__':
    DataCleaning().get_result()
