from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.baidu.com")

driver.save_screenshot("./files/baidu_img.png")