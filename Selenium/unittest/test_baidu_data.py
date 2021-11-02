import csv
import codecs
import unittest
import os
from time import sleep
from itertools import islice
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.base_url = "https://www.baidu.com"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def baidu_search(self,search_key):
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID,"kw").send_keys(search_key)
        self.driver.find_element(By.ID,"su").click()
        sleep(3)

    def test_search(self):
        with codecs.open('./unittest/csv_data/baidu_data.csv','r','utf_8_sig') as f:
            data = csv.reader(f)
            for line in islice(data, 1, None):
                search_key = line[1]
                # print(search_key)
                self.baidu_search(search_key)

if __name__ =='__main__':
    # cwd = os.getcwd()
    # print("当前目录："+cwd)
    unittest.main(verbosity=2)
