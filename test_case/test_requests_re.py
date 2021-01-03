import re

import requests


class TestRequestsRe:
    def test_get_province(self):
        base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/'
        r = requests.get(base_url + "index.html")
        r.encoding = 'gbk'
        tr_list = re.findall("<tr class='provincetr'>(.*?)</tr>", r.text)
        province_list = []
        for tr in tr_list:
            td_list = re.findall('<td>(.*?)</td>', tr)
            for td in td_list:
                if "a" in td:
                    print(td)
                    name = re.match("\[u4e00-\u9fa5]", td)
                    print(name)
        #             name = re.findall("'>(.*?)<br/>", td)
        #             url = re.findall("'(.*?)'", td)
        #             province = {"name": name, "url": url}
        #             province_list.append(province)
        # print(province_list)

    def test_re(self):
        base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/'
        r = requests.get(base_url + "index.html")
        r.encoding = 'gbk'
        # print(home_page)
        province_name_list = re.findall("html'>(.*?)<br/></a>", r.text)
        city_url_list = re.findall("<td><a href='(.*?)'>", r.text)

        for city_url in city_url_list:
            cr = requests.get(base_url + city_url)
            cr.encoding = 'gbk'
            city_name_list_parent = re.findall("html'>(.*?)</a>", cr.text)
            region_url_list_parent = re.findall("<td><a href='(.*?)'", cr.text)
            for city_name_list in city_name_list_parent:
                if '0' not in city_name_list:
                    print(city_name_list)
            region_url_list_temp = []
            for region_url_list in region_url_list_parent:
                if region_url_list not in region_url_list_temp:
                    # print(region_url_list)
                    region_url_list_temp.append(region_url_list)
                    rr = requests.get(base_url + region_url_list)
                    rr.encoding = 'gbk'
                    town_name_list_parent = re.findall("html'>(.*?)</a>", rr.text)
                    town_url_list_parent = re.findall("<td><a href='(.*?)'", rr.text)
                    for town_name_list in town_name_list_parent:
                        if '0' not in town_name_list:
                            print(town_name_list)
