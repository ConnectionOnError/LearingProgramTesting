from time import ctime, sleep

from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.baidu.com")
print(ctime())

for i in range(10):
    try:
        el = driver.find_element_by_id("kw")
        if el.is_displayed():
            print("找到元素kw")
            break
    except:
        pass
    sleep(1)
else:
    print("time out")
print(ctime())
driver.quit()
