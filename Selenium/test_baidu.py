from selenium import webdriver
import time
driver = webdriver.Edge()
driver.get("https://www.baidu.com")

# driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("伊什塔尔")
driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("伊什塔尔")
driver.find_element_by_id("su").click()
print("设置浏览器宽480、高800显示")
driver.set_window_size(480,800)
time.sleep(2)
#使用a标签上一个h3来定位到伊什塔尔百度百科
# driver.find_element_by_xpath("//h3[@class='t c-gap-bottom-small']/a").click()
#使用a标签上的title属性来定位
# driver.find_element_by_xpath("//a[@title='角色背景']").click()
# driver.find_element_by_css_selector(".s_ipt").send_keys("仇凛")
# driver.find_element_by_xpath("//input[@id='su']").click()
driver.quit 