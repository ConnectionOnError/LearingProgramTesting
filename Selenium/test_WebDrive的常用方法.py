from selenium import webdriver
driver = webdriver.Edge()
#转到百度页面
driver.get("https://www.baidu.com")

#清空输入框的文本clear()
driver.find_element_by_id("kw").clear()
#输入selenium
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
driver.implicitly_wait(10)
# driver.quit()