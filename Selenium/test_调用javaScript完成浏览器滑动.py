import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.baidu.com")
#设置浏览器宽高
driver.set_window_size(800,600)
driver.find_element(By.ID,"kw").send_keys("selenium")
driver.find_element(By.ID,"su").click()
time.sleep(3)
#通过JavaScript设置浏览器窗口的滑动条位置
js = 'window.scrollTo(100,450);'
driver.execute_script(js)
