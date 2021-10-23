#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests


class ScrapeAPI(object):
    def __init__(self):
        self._api_url = 'https://api.bigdatacloud.net/data/ip-geolocation-full?ip=27.30.84.181&localityLanguage=zh&key=bee73355d8821a1c19393c545e7f0'

    def get_geolocation(self):
        init_session = requests.Session()
        response = init_session.get(self._api_url)
        json_result = response.json()
        get_country = json_result['country']['name']
        get_location = json_result['location']
        get_region = get_location['isoPrincipalSubdivision']
        get_city = get_location['city']
        get_locality_name = get_location['localityName']
        area = f'当前 IP 国家：{get_country}，地区：{get_region}，城市：{get_city},区划：{get_locality_name}'
        print(area)


if __name__ == '__main__':
    ScrapeAPI().get_geolocation()
