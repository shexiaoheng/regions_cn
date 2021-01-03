from data_manage.province_manage import ProvinceManage


class TestProvince:
    def setup(self):
        self.manage = ProvinceManage()

    def test_province(self):
        province_list = self.manage.get_province_data()
        self.manage.save_province_data(province_list)