import json

import requests
from bs4 import BeautifulSoup


# 实验类，有 bug，仅留作纪念
class TestBs4:

    def test_bs4(self):
        base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/'
        data = []
        r = requests.get(base_url + "index.html")
        p_soup = BeautifulSoup(r.content, 'html.parser')
        province_trs = p_soup.select('.provincetr')
        for province_tr in province_trs:
            for province_t in province_tr:
                if province_t.a is not None:
                    city_url = base_url + province_t.a['href']

                    cr = requests.get(city_url)
                    c_soup = BeautifulSoup(cr.content, 'html.parser')
                    citys = []
                    city_trs = c_soup.select('.citytr')
                    for city_tr in city_trs:
                        city_a = city_tr.find_all('a')[1]
                        region_url = base_url + city_a['href']

                        rr = requests.get(region_url)
                        r_soup = BeautifulSoup(rr.content, 'html.parser')
                        regions = []
                        region_trs = r_soup.select('.countytr')
                        for region_tr in region_trs:
                            region_td = region_tr.find_all('td')[1]
                            # region = {"region_name": region_td.text}
                            regions.append(region_td.text)
                        city = {"city_name": city_a.text, "region_list": regions}
                        citys.append(city)
                    provinces = {"province_name": province_t.text, "city_list": citys}
                    data.append(provinces)
        result = json.dumps(data, ensure_ascii=False, indent=4)
        file = open('json_data.json', 'w', encoding='utf-8')
        file.write(result)
        file.close()

    def test_write(self):
        test_str = [{"name": "佘小恒", "sex": "男"}, {"name": "shexiaoheng", "sex": "man"}]
        data = json.dumps(test_str, ensure_ascii=False)
        file = open('demo.json', 'w', encoding='utf-8')
        file.write(data)
        file.close()
