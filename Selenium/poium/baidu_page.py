from poium import Page,Element

class BaiduPage(Page):
    """百度Page层，百度页面封装操作到的元素"""
    #通过timeout可以设置元素超时时间
    
    search_input = Element(id_="kw", timeout = 5)
    search_button = Element(id_ = "su", timeout = 30)
    
    #获取title
    def get_title(self):
        return self.driver.title
    