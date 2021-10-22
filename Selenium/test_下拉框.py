from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
driver.get("https://www.baidu.com")
#点击设置
driver.find_element(By.ID,"s-usersetting-top").click()
#点击高级搜索
driver.find_element(By.LINK_TEXT,"高级搜索").click()

#选择
#按照书上不行了，自己换了一个方法就是直接定位了用text()
sel = driver.find_element(By.XPATH,"//div[@class='c-select adv-ft-select']/div[@class='c-select-selection']")
sel.click()
driver.find_element(By.XPATH,"//p[text()='所有格式']").click()

driver.find_element(By.XPATH,"//li[text()='搜索设置']").click()

#保存设置
driver.find_element(By.LINK_TEXT,"保存设置").click()

#获取警告框
alert = driver.switch_to.alert

#获取警告框信息
alert_text = alert.text
print(alert_text)

#接取警告框
alert.accept()




