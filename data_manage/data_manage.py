import requests
from bs4 import BeautifulSoup


class DataManage:
    base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/'

    def get_home_soup(self):
        return self.get_base_soup(self.base_url + "index.html")

    def get_base_soup(self, url):
        r = requests.get(url)
        r.encoding = 'gbk'
        p_soup = BeautifulSoup(r.text, 'html.parser')
        return p_soup

    # 获取省市区联动数据
    def get_linked_data(self):
        p_soup = self.get_home_soup()
        province_trs = p_soup.select('.provincetr')
        province_list = []
        for province_tr in province_trs:
            for province_td in province_tr:
                if province_td.a is not None:
                    url_path = province_td.a['href']
                    name = province_td.text
                    c_url = self.base_url + url_path
                    city_list = self.get_city_data(city_url=c_url)
                    province = {"name": name, "city_url": c_url, "city_list": city_list}
                    province_list.append(province)
        return province_list

    # 获取所有省级数据
    def get_province_data(self):
        p_soup = self.get_home_soup()
        province_trs = p_soup.select('.provincetr')
        province_list = []
        for province_tr in province_trs:
            for province_td in province_tr:
                if province_td.a is not None:
                    url_path = province_td.a['href']
                    name = province_td.text
                    c_url = self.base_url + url_path
                    province = {"name": name, "city_url": c_url}
                    province_list.append(province)
        return province_list

    def get_all_city_data(self):
        p_soup = self.get_home_soup()
        province_trs = p_soup.select('.provincetr')
        city_data_list = []
        for province_tr in province_trs:
            for province_td in province_tr:
                if province_td.a is not None:
                    url_path = province_td.a['href']
                    c_url = self.base_url + url_path
                    city_data = self.get_city_data(c_url)
                    city_data_list.append(city_data)
        return city_data_list

    # 获取市数据
    def get_city_data(self, city_url):
        p_soup = self.get_base_soup(city_url)
        city_trs = p_soup.select('.citytr')
        city_list = []
        for city_tr in city_trs:
            city_td = city_tr.find_all('td')
            c_id = city_td[0].text
            url = city_td[0].a['href']
            name = city_td[1].text
            city = {"id": c_id, "name": name, "url": self.base_url + url}
            city_list.append(city)
        return city_list

    def get_all_county_data(self):
        p_soup = self.get_home_soup()
        province_trs = p_soup.select('.provincetr')
        county_data_list = []
        for province_tr in province_trs:
            for province_td in province_tr:
                if province_td.a is not None:
                    url_path = province_td.a['href']
                    c_url = self.base_url + url_path
                    city_data = self.get_city_data(c_url)
                    for city in city_data:
                        p_soup = self.get_base_soup(city['url'])
                        county_trs = p_soup.select('.countytr')
                        for county_tr in county_trs:
                            county_td = county_tr.find_all('td')
                            c_id = county_td[0].text
                            name = county_td[1].text
                            if county_td[0].a is not None:
                                url = self.base_url + county_td[0].a['href']
                            else:
                                url = ""
                            county = {"id": c_id, "name": name, "url": url}
                            county_data_list.append(county)
        return county_data_list

    # 获取区数据
    def get_county_data(self, county_url):
        p_soup = self.get_base_soup(county_url)
        county_trs = p_soup.select('.countytr')
        county_list = []
        for county_tr in county_trs:
            county_td = county_tr.find_all('td')
            c_id = county_td[0].text
            name = county_td[1].text
            if county_td[0].a is not None:
                url = self.base_url + county_td[0].a['href']
            else:
                url = ""
            county = {"id": c_id, "name": name, "url": url}
            county_list.append(county)
        return county_list
