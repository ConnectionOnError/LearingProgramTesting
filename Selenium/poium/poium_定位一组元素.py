from poium import Page, Element

class ResultPage(Page):

    #定位一组元素
    search_result = Element(xpath = "//div/h3/a")