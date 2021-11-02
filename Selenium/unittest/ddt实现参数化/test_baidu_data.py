import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt, data, file_data, unpack

@ddt
class TestBaidu(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.base_url = "https://www.baidu.com"

    def baidu_search(self,search_key):
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID,"kw").send_keys(search_key)
        self.driver.find_element(By.ID,"su").click()
        sleep(3)
    
    #记得改变test_search的名字，1,2,3执行三个不同的参数化方法用例

    #参数化使用方法1
    @data(["case1","selenium"],["case2","宇宙凛"],["case3","贝尔塞蒂亚"])
    @unpack
    def test_search1(self,case,search_key):
        print("第一组测试用例：",case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
    
    #参数化使用方法2
    @data(("case1","selenium"),("case2","宇宙凛"),("case3","贝尔塞蒂亚"))
    @unpack
    def test_search2(self,case,search_key):
        print("第二组测试用例：",case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")

    #参数化使用方法3
    @data({"search_key":"selenium"},{"search_key": "ddt"},{"search_key": "python"})
    @unpack
    def test_search3(self,search_key):
        print("第三组测试用例：",search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
    