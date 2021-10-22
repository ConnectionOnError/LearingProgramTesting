from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
text = "宇宙凛为什么是神？"
driver.get("http://127.0.0.1:5500/textrear.html")
js = "document.getElementById('id').value='"+ text +"';"
driver.execute_script(js)