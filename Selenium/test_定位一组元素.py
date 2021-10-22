from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.baidu.com")

driver.find_element(By.ID,"kw").send_keys('宇宙凛')
driver.find_element(By.ID,"su").click()
sleep(2)

#定位一组元素
texts = driver.find_elements(By.XPATH,"//div[@tpl='se_com_default']/h3/a")
print(len(texts))

#循环遍历出每一条搜索结果的标题
for t in texts:
    print(t.text)

driver.quit()