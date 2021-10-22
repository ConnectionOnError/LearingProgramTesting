from selenium import webdriver
driver = webdriver.Edge()
driver.get('https://www.baidu.com')

driver.find_element_by_id("kw").send_keys("土方岁三")
driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("宇宙凛")
# driver.find_element_by_id("su").click()
#使用submit提交
search_text = driver.find_element_by_id('kw')
search_text.send_keys('宇宙凛')
search_text.submit()
driver.quit