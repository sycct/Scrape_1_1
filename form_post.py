#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests

params = {'username': 'admin', 'passwd': '123alsdfiow####***'}

r = requests.post("http://www.test.com/admin/index.php?c=session&a=login", data=params)
print(r.text)
