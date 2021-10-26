import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Edge()
        cls.base_url = "https://www.baidu.com"

    # def setUp(self) -> None:
    #     self.driver = webdriver.Edge()
    #     self.base_url = "https://www.baidu.com"

    #传入搜索框输入文字，完成搜索操作
    def baidu_search(self,search_key):
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID,"kw").send_keys(search_key)
        sleep(3)
        self.driver.find_element(By.ID,"su").click()
        sleep(2)

    def test_search_key_selenium(self):
        search_key = "selenium"
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
        sleep(3)

    def test_search_key_FGO(self):
        search_key = "宇宙凛"
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
        sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
