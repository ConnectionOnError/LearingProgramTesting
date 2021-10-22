from time import sleep
from selenium import webdriver
from time import sleep
driver = webdriver.Edge()
driver.get("https://www.baidu.com")

#打印当前页面title
title = driver.title
print("当前页面title:"+title)

#打印当前页面url
url = driver.current_url
print("当前页面url:"+url)

driver.find_element_by_id("kw").send_keys("宇宙凛")
driver.find_element_by_id("su").click()
print("搜索宇宙凛之后的信息")
sleep(2)

#打印当前页面title
new_title = driver.title
print("搜索页面title:"+new_title)

#打印当前页面url
new_url = driver.current_url
print("搜索页面url:"+new_url)

#获取搜索结果数目
nums = driver.find_element_by_class_name("nums_text").text
print(nums)