from selenium import webdriver
import time
driver = webdriver.Edge()
driver.get("https://www.baidu.com")

#访问百度首页
first_url = 'https://www.baidu.com'
driver.get(first_url)
time.sleep(1)

#访问新闻页面
second_url = 'http://news.baidu.com/'
driver.get(second_url)
time.sleep(1)

#back()返回上一页
driver.back()
time.sleep(1)

#forward()前进到之前的页面
driver.forward()
time.sleep(1)

#模拟浏览器刷新
driver.refresh()
driver.close()