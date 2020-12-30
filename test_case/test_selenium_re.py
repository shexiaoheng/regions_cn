import re
from selenium import webdriver


class TestRe:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/'

    def teardown(self):
        self.driver.quit()

    def test_re(self):
        self.driver.get(self.base_url + 'index.html')
        home_page = self.driver.page_source
        print(home_page)
        province_name_list = re.findall('html">(.*?)<br></a>', home_page, re.S)
        city_url_list = re.findall('<td><a href="(.*?)"', home_page, re.S)
        print(province_name_list)
        print(city_url_list)
        for city_url in city_url_list:
            self.driver.get(self.base_url + city_url)
            city_page = self.driver.page_source
            city_name_list = re.findall('html">(.*?)</a>', city_page, re.S)[1]
            region_url_list = re.findall('<td><a href="(.*?)"', city_page, re.S)[1]
            print(city_name_list)
            print(region_url_list)

            # for region_url in region_url_list:
            #     print(region_url)
                # self.driver.get(self.base_url + region_url)
                # region_page = self.driver.page_source
                # region_name_list = re.findall('html">(.*?)</a>', region_page, re.S)[1]
                # town_url_list = re.findall('<td><a href="(.*?)"', region_page, re.S)[1]
                # print(region_name_list)
                # print(town_url_list)
