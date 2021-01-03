from data_manage.base_manage import BaseManage
from util.write_util import write_city


class CityManage(BaseManage):

    def get_city_data(self):
        p_soup = self.get_index_soup()
        province_trs = p_soup.select('.provincetr')
        city_data_list = []
        for province_tr in province_trs:
            for province_td in province_tr:
                if province_td.a is not None:
                    url_path = province_td.a['href']
                    c_url = self.base_url + url_path
                    p_soup = self.get_base_soup(c_url)
                    city_trs = p_soup.select('.citytr')
                    for city_tr in city_trs:
                        city_td = city_tr.find_all('td')
                        c_id = city_td[0].text
                        url = city_td[0].a['href']
                        name = city_td[1].text
                        city = {"id": c_id, "name": name, "url": self.base_url + url}
                        city_data_list.append(city)
        return city_data_list

    def save_city_data(self, city_list):
        write_city(city_list)

    # 获取市数据
    def get_city_by_url(self, city_url):
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
