from data_manage.base_manage import BaseManage
from util.write_util import write_county


class CountyManage(BaseManage):
    def get_county_data(self):
        p_soup = self.get_index_soup()
        province_trs = p_soup.select('.provincetr')
        county_data_list = []
        for province_tr in province_trs:
            for province_td in province_tr:
                if province_td.a is not None:
                    city_url_path = province_td.a['href']
                    city_url = self.base_url + city_url_path
                    city_soup = self.get_base_soup(city_url)
                    city_trs = city_soup.select('.citytr')
                    for city_tr in city_trs:
                        city_td = city_tr.find_all('td')
                        county_url_path = city_td[0].a['href']
                        county_url = self.base_url + county_url_path
                        county_soup = self.get_base_soup(county_url)
                        county_trs = county_soup.select('.countytr')
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

    def save_county_data(self, county_list):
        write_county(county_list)

    # 获取区数据
    def get_county_by_url(self, county_url):
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

