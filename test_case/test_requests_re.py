import re

import requests


class TestRequestsRe:
    def test_re(self):
        base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/'
        r = requests.get(base_url + "index.html")
        r.encoding = 'gbk'
        home_page = r.text
        print(home_page)
        province_name_list = re.findall("html'>(.*?)<br/></a>", home_page, re.S)
        city_url_list = re.findall("<td><a href='(.*?)'>", home_page, re.S)
        print(province_name_list)
        print(city_url_list)
        for city_url in city_url_list:
            cr = requests.get(base_url + city_url)
            cr.encoding = 'gbk'
            city_page = cr.text
            city_name_list = re.findall("html'>(.*?)</a>", city_page, re.S)[1]
            region_url_list = re.findall("<td><a href='(.*?)'", city_page, re.S)[1]
            print(city_name_list)
            print(region_url_list)