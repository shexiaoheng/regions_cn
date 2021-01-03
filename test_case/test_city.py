from data_manage.city_manage import CityManage


class TestCity:
    def setup(self):
        self.manage = CityManage()

    def test_city(self):
        city_list = self.manage.get_city_data()
        self.manage.save_city_data(city_list)