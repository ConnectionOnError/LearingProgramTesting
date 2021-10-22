from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.126.com")

#登录
sleep(2)
driver.switch_to_frame('x-URS-iframe')
driver.find_element(By.NAME,"email").clear()
driver.find_element(By.NAME,"email").send_keys("username")
driver.find_element(By.NAME,"password").clear()
driver.find_element(By.NAME,"password").send_keys("password")
driver.find_element(By.ID,"dologin").click()

#登陆之后的动作
sleep(5)

#退出
driver.find_element(By.LINK_TEXT,"退出").click()

driver.quit()
