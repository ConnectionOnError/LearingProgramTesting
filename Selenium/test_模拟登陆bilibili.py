from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Edge()
driver.get("https://passport.bilibili.com/login?from_spm_id=333.851.top_bar.login")

#获取登陆账户框
driver.find_element(By.ID,"login-username").send_keys('15578883772')
#获取登陆密码框
driver.find_element(By.ID,"login-passwd").send_keys('hentai666')
sleep(2)
#点击登录按钮
driver.find_element(By.XPATH,"//div[@class='btn-box']/a[@class='btn btn-login']").click()