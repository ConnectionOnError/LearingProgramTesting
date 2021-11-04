import time

class BasePage:
    """
    基础page层，封装一些常用方法
    """

    def __init__(self,driver) -> None:
        self.driver =  driver
    
    #打开页面
    def open(self,url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    #id定位
    def by_id(self,id_):
        return self.driver.find_element_by_id(id_)

    #class定位
    def by_class(self,class_name):
        return self.driver.find_element_by_class(class_name)

    #name定位
    def by_name(self,name):
        return self.driver.find_element_by_name(name)
    
    #XPath定位
    def by_xpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)

    #CSS定位
    def by_css(self,css):
        return self.driver.find_element_by_css(css)
    
    #获取title
    def get_title(self):
        return self.driver.title

    #获取页面text,仅使用XPth定位
    def get_text(self,xpath):
        return self.by_xpath(xpath).text

    #执行JavaScript脚本
    def js(self,script):
        self.driver.execute_script(script)