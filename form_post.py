#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
from requests import Session, exceptions

from requests.auth import HTTPBasicAuth

from utils import connection_util


def post_login():
    params = {'username': 'admin', 'passwd': '123alsdfiow####***'}

    r = requests.post("http://www.test.com/admin/index.php?c=session&a=login", data=params)
    print(r.text)


def upload_image():
    files = {'uploadFile': open('files/2fe7243c7c113fad443b375a021801eb6277169d.png', 'rb')}
    r = requests.post("http://pythonscraping.com/pages/processing2.php", files=files)
    print(r.text)


def http_auth():
    auth = HTTPBasicAuth('user', '123##@de09pp')
    r = requests.post(url="http://www.test.com:1111/", auth=auth)
    print(r.text)


class GetCookie(object):
    def __init__(self):
        self._session = Session()
        self._init_connection = connection_util.ProcessConnection()

    def get_cookie_by_login(self):
        get_token = self.get_request_verification_token()
        # 另外一个 session 中
        # get_token=self.request_verification_token()
        if get_token:
            params = {'__RequestVerificationToken': get_token, 'Email': '123@gmail.com',
                      'Password': '123@pd-09',
                      'RememberMe': True}
            r = self._session.post('https://pdf-lib.org/account/admin', params)
            # 如果使用 request_verification_token 此处会出现 500 错误
            if r.status_code == 500:
                print(r.content.decode('utf-8'))
            print('Cookie is set  to:')
            print(r.cookies.get_dict())
            print('--------------------------------')
            print('Going to post article page..')
            # 此处如果是使用 requests.get 并不会获取后台文章内容，由于并不是在同一个会话对象当中
            # r = requests.get('https://pdf-lib.org/account/users')
            r = self._session.get('https://pdf-lib.org/account/users')
            print(r.text)

    def get_request_verification_token(self):
        # 连接网站
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
            html = self._session.get("https://pdf-lib.org/account/admin", headers=headers)
        except (exceptions.ConnectionError, exceptions.HTTPError, exceptions.Timeout) as e:
            return False
        try:
            bsObj = BeautifulSoup(html.text, features='html.parser')
        except AttributeError as e:
            return False
        if bsObj:
            try:
                get_token = bsObj.find("input", {"name": "__RequestVerificationToken"}).get("value")
            except Exception as e:
                print(f"ot unhandled exception {e}")
                return False
            return get_token

    def request_verification_token(self):
        # 此处仍然会获取所需要的内容
        get_content = self._init_connection.init_connection('https://pdf-lib.org/account/admin')
        if get_content:
            try:
                get_token = get_content.find("input", {"name": "__RequestVerificationToken"}).get("value")
            except Exception as e:
                print(f"ot unhandled exception {e}")
                return False
            return get_token


if __name__ == '__main__':
    http_auth()
