import unittest
from time import sleep
from selenium import webdriver
from baidu_page import BaiduPage

class TestBaidu(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Edge()

    def test_baidu_search_case1(self):
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "selenium"
        page.search_button.click()
        sleep(2)
        self.assertEqual(page.get_title(),"selenium_百度搜索")

    def test_baidu_search_case2(self):
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "unittest"
        page.search_button.click()
        sleep(2)
        self.assertEqual(page.get_title(),"unittest_百度搜索")

    def test_baidu_search_case3(self):
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "Page Object"
        page.search_button.click()
        sleep(2)
        self.assertEqual(page.get_title(),"Page Object_百度搜索")

    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
    