from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#换了一个测试网站
driver = webdriver.Edge()
driver.get("http://www.jq22.com/yanshi4976")
#页面超时3s
driver.set_page_load_timeout(3)
#script超时4s
driver.set_script_timeout(4)
sleep(2)
#仔细观察定位元素是否被嵌套进iframe！！！！
# 定位要滑动的年、月、日
driver.switch_to.frame("iframe")
driver.find_element_by_id("appDate").click()

#在定位一组元素的时候确定是不是find_elements
dwwos = driver.find_elements(By.CLASS_NAME,"dwwo")
year = dwwos[0]
month = dwwos[1]
day = dwwos[2]

#拨动年
action = webdriver.ActionChains(driver)
action.click_and_hold(year).move_by_offset(0,20).perform()
action.reset_actions()

# 拨动月
action2 = webdriver.ActionChains(driver)
action2.click_and_hold(month).move_by_offset(0, 150).perform()
action2.reset_actions()

#拨动天
action3 = webdriver.ActionChains(driver)
action3.click_and_hold(day).move_by_offset(0, 150).perform()
action3.reset_actions()