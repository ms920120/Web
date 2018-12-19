import logging
import pytest
import time
from pageobjects.login_page import LoginPage
from testdatas import common_data as CD
from testdatas import login_data as LD
from common import log
class TestLogin:
    #@pytest.mark.smoke
    @pytest.mark.usefixtures("nologin_driver")
    @pytest.mark.parametrize("login_data",LD.login_data)
    def test_login_success(self, nologin_driver,login_data):
        logging.info("*********登陆用例：正常场景：使用正确的用户名和密码登陆*********")
        LoginPage(nologin_driver).login_page(login_data["user"], login_data["passwd"])
        #LoginPage(nologin_driver).login_page(LD.success_data[0]["user"],LD.success_data[0]["passwd"])
        assert nologin_driver.current_url == login_data["check_url"]
        #assert nologin_driver.current_url == LD.success_data[0]["check_url"]
    """
    @pytest.mark.smoke
    @pytest.mark.usefixtures("nologin_driver")
    @pytest.mark.parametrize("noLogindata", LD.err_data)  # 多参数演示 示例
    def test_login_noLoginInfo(self, login_web, noLogindata):
        logging.info("*********登陆用例：异常场景：没有用户名/没有密码/用户名格式不正确*********")
        LoginPage(login_web).login_page(noLogindata["user"], noLogindata["passwd"])
        # 验证-检查点
        assert LoginPage(login_web).get_errorMsg_from_loginArea() == noLogindata["check"]
    """
