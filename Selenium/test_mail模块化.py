from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from model_mail import Mail

driver = webdriver.Edge()
driver.get("https://www.126.com")

#调用Mail类并接受driver驱动
mail = Mail(driver)

#登录账号密码为空
mail.login("","")

#登录账号为空
mail.login("","password")

#登录密码为空
mail.login("username","")

#管理员登录
mail.login("admin","admin123")

#登录之后的动作
sleep(5)

#退出
mail.logout()

driver.quit()