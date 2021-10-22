from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Edge()
driver.get("https://www.bilibili.com")
sleep(2)
#获取哔哩哔哩首页窗口句柄
main_windows = driver.current_window_handle

#不知道为什么哔哩哔哩会打开两个不同的页面，页面的代码是有区别的，所以只能多次进去蒙
#点击登录按钮
driver.find_element(By.CLASS_NAME,"unlogin-avatar").click()
# driver.find_element(By.CLASS_NAME,"header-login-entry").click()

#获取所有的窗口句柄
all_handles = driver.window_handles

for handle in all_handles:
    if handle != main_windows:
        driver.switch_to.window(handle)
        print(driver.title)
        #获取登陆账户框
        driver.find_element(By.ID,"login-username").send_keys('15578883772')
        #获取登陆密码框
        driver.find_element(By.ID,"login-passwd").send_keys('hentai666')
        sleep(2)
        #点击登录按钮
        driver.find_element(By.XPATH,"//div[@class='btn-box']/a[@class='btn btn-login']").click()
        sleep(5)
        driver.close()

driver.switch_to.window(main_windows)
print(driver.title)
