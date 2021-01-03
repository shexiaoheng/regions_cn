from data_manage.county_manage import CountyManage


class TestCounty:
    def setup(self):
        self.manage = CountyManage()

    def test_county(self):
        county_list = self.manage.get_county_data()
        self.manage.save_county_data(county_list)