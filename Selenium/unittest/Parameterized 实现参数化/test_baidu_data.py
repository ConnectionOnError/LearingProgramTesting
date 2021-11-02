import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from parameterized import parameterized

class TestBaidu(unittest.TestCase):  
       
    #类最先执行
    @classmethod
    def setUpClass(cls) -> None:  
        #设置百度搜搜地址和浏览器类型
        cls.base_url = "https://www.baidu.com"
        cls.driver = webdriver.Edge()

    #搜索方法，只需要修改search_key完成不同的搜索
    def baidu_search(self,search_key):
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID,"kw").send_keys(search_key)
        self.driver.find_element(By.ID,"su").click()
        sleep(3)

    #通过使用Parameterized实现参数化
    @parameterized.expand([
        ("case1","selenium"),
        ("case2","宇宙凛"),
        ("case3","贝尔塞蒂亚"),
    ])

    #name是用来接受casex的，在函数中并没有使用到，所以是灰色，但是书上是这样写的
    #可以做修改去掉上面的case1那一列只传入search_key也可以
    def test_search(self,search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)