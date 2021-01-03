import json

import requests
from bs4 import BeautifulSoup


class BaseManage:
    base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/'

    def __init__(self):
        pass

    def get_index_soup(self):
        return self.get_base_soup(self.base_url + "index.html")

    def get_base_soup(self, url):
        r = requests.get(url)
        r.encoding = 'gbk'
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    def parser_to_json(self, content):
        return json.dumps(content, ensure_ascii=False, indent=4)