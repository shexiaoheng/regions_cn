from data_manage.base_manage import BaseManage
from util.write_util import write_province


class ProvinceManage(BaseManage):
    # 获取省级数据
    def get_province_data(self):
        p_soup = self.get_index_soup()
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

    def save_province_data(self, province_list):
        write_province(province_list)