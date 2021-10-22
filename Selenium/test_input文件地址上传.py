from selenium import webdriver
from selenium.webdriver.common.by import By
import os
#获取当前文件的路径
file_path = os.path.abspath('')
driver = webdriver.Edge()
upload_page = 'file:///' + file_path + '/upfile.html'
driver.get(upload_page)

#定位上传按钮，添加本地文件
driver.find_element_by_id("name").send_keys(file_path + '\\test.txt')