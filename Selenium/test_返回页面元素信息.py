from selenium import webdriver
driver = webdriver.Edge()
driver.get('https://www.baidu.com')

#获取输入框的尺寸
size = driver.find_element_by_id("kw").size
print(size)

#返回页面底部备案信息(失败)
text = driver.find_element_by_xpath("//a[text()='帮助中心']")
print(text.text,text.get_attribute('href'))

#返回元素的属性值，可以使id、name、type或其他属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

#返回元素的结果是否可见，返回结果为True或False
result = driver.find_element_by_id("kw").is_displayed()
print(result)
driver.quit