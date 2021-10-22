from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Edge()
driver.get("https://www.bilibili.com")
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME,"nav-search-input").send_keys("宇宙凛为什么是神")
driver.find_element(By.CLASS_NAME,"nav-search-btn").click()
sleep(2)

#获取视频标题(失败)
# texts = driver.find_elements(By.XPATH,"//ul[@class='video-list clearfix']/li[@class='video-item matrix']")
# print(len(texts))
driver.quit()