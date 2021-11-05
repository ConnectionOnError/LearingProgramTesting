from poium import Page,Element

class LoginPage(Page):
    """
    登录Page类
    """

    username = Element(css = '#loginAccount',describe = "用户名")
    password = Element(css = '#loginPwd', describe = "密码")
    login_button = Element(css = '#login_btn', describe = "登录按钮")
    user_info = Element(css = "a.nav_user_name > span", describe = "用户信息")