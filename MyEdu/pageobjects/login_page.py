from common.basepage import BasePage
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):
    # 元素定位
    # 用户名输入框
    user_input = "txtUserName"
    # 密码输入框
    passwd_input ="txtPassword"
    # 登陆按钮
    button = 'mlbActive'
    # 输入错误用户名或者密码的出错信息提示通过xpath方式定位
    error_Msg = "#dialog-message-Alert>div"

    # 登陆功能
    def login_page(self, user, password):
        name = "登录页面--登录功能"
        self.wait_elementvisibility(self.user_input, by=By.ID, model=name)
        self.send_keys_element(self.user_input, user, by=By.ID, model=name)
        self.send_keys_element(self.passwd_input, password, by=By.ID, model=name)
        self.click_element(self.button, by=By.ID, model=name)
        time.sleep(1)
    #获取输入错误登录框的错误信息
    def get_errorMsg_from_loginArea(self):
        name = "登陆页面_获取登陆框错误信息"
        self.wait_elementvisibility(self.error_Msg, by=By.XPATH, model=name)
        return self.get_text(self.error_Msg, by=By.XPATH, model=name)
    def click_errbtn(self):
        name = "登陆页面_点击弹出框的确定按钮"
