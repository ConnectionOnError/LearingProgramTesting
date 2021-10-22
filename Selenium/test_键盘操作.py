from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Edge()
driver.get("https://www.baidu.com")

#在输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")

#删除一个多余的m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

#添加一个空格和教程字段
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")

#输入组合键ctrl+a、ctrl+x、ctrl+v
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')

#输出回车代替点击搜索按钮操作
driver.find_element_by_id("kw").send_keys(Keys.ENTER)