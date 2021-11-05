from poium import Page,Element

class SomePage(Page):
    #8种定位方法
    elem_id = Element(id_ = "id")
    elem_name = Element(name = 'name')
    elem_class = Element(class_name = 'class')
    elem_tag = Element(tag = 'input')
    elem_link_text = Element(link_text = 'this_is_link')
    elem_partial_link_text = Element(partical_link_text = 'is_link')
    elem_xpath = Element(xpath='//*[@id="kk"]')
    elem_css = Element(css = '#id')

    #
