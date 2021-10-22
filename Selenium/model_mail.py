class Mail:
    def __init__(self,driver):
        self.driver = driver
    
    def login(self,username,password):
        """登录"""
        driver.switch_to_frame('x-URS-iframe')
        driver.find_element(By.NAME,"email").clear()
        driver.find_element(By.NAME,"email").send_keys(username)
        driver.find_element(By.NAME,"password").clear()
        driver.find_element(By.NAME,"password").send_keys(password)
        driver.find_element(By.ID,"dologin").click()

    def logout(self):
        """退出"""
        driver.find_element(By.LINK_TEXT,"退出").click()