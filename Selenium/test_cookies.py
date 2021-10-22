from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

#获取所有cookies信息并打印
cookies = driver.get_cookies()
print(cookies)

#添加Cookies信息
driver.add_cookie({'name':'key-aaaaaaaaaaaaa','value':'key-bbbbbbbbbbbbbbb'})

#遍历出想要的cookie
for cookie in driver.get_cookies():
    print ("%s -> %s" % (cookie['name'],cookie['value']))  
#删除名字为domain的cookie
driver.delete_cookie('key-aaaaaaaaaaaaa')

#自己添加的cookie删除成功了，但是网站自带的就没成功，不懂为什么
# driver.delete_cookie('.baidu.com')
# driver.delete_cookie('www.baidu.com')
cookies = driver.get_cookies()
print(cookies)
