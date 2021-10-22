from selenium import webdriver
#引入actionchain类
from selenium.webdriver import ActionChains
import time
driver = webdriver.Edge()
driver.get("https://www.baidu.com")
driver.maximize_window()
#定位要要悬停的位置
adbove = driver.find_element_by_id("s-usersetting-top")
#对定位到的元素进行悬停操作
ActionChains(driver).move_to_element(adbove).perform()
# ActionChains(driver).click(adbove).perform()