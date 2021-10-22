from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://www.baidu.com")

element = WebDriverWait(driver,5,0.5).until(
    EC.visibility_of_element_located((By.ID,"kw"))
)

element.send_keys("宇宙凛")