from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Edge()
driver.get("https://www.baidu.com")
#点击设置
driver.find_element(By.ID,"s-usersetting-top").click()
#点击搜索设置
driver.find_element(By.LINK_TEXT,"搜索设置").click()

#保存设置
driver.find_element(By.LINK_TEXT,"保存设置").click()

#获取警告框
alert = driver.switch_to.alert

#获取警告框信息
alert_text = alert.text
print(alert_text)

#接取警告框
alert.accept()

driver.quit()