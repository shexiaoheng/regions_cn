import json

from data_manage.data_manage import DataManage


class TestManage:
    def setup(self):
        self.manage = DataManage()

    def teardown(self):
        pass

    def test_province(self):
        province_list = self.manage.get_province_data()
        data = json.dumps(province_list, ensure_ascii=False, indent=4)
        print(data)

    def test_get_all_city(self):
        all_city_data = self.manage.get_all_city_data()
        data = json.dumps(all_city_data, ensure_ascii=False, indent=4)
        print(data)

    def test_county(self):
        all_county_data = self.manage.get_all_county_data()
        data = json.dumps(all_county_data, ensure_ascii=False, indent=4)
        print(data)
