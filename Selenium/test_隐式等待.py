from selenium import webdriver
from time import ctime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Edge()

#设置隐式等待10s
driver.implicitly_wait(10)
driver.get("Https://www.baidu.com")

try:
    print(ctime())
    driver.find_element(By.ID,"kw2").send_keys('宇宙凛')
except NoSuchElementException as e:
    print("错误信息:")
    print(e)
finally:
    print(ctime())
    driver.quit()