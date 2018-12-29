import pytest
import logging
from common import log
from pageobjects.createteachtask_page import CreateTeachTask
from pageobjects.main_page import MainPage
from testdatas import createteachtask_data as TD
class TestCreateTeachTask:
    @pytest.mark.smoke
    #使用夹具进行用例的准备和清理工作
    @pytest.mark.usefixtures("login_driver")
    #参数化测试用例的数据
    @pytest.mark.parametrize("taskdata",TD.teachtask)
    def test_createteachtask(self,login_driver,taskdata):
        MainPage(login_driver).click_left(taskdata["left"])
        MainPage(login_driver).click_firstmenu(taskdata["firstmenu"])
        MainPage(login_driver).click_lastmenu(taskdata["lastmenu"])
        MainPage(login_driver).iframe_into()
        print(111111111)
        CreateTeachTask(login_driver).select_semester(taskdata["semester"])
        print(222222222)
        CreateTeachTask(login_driver).select_learningspace(taskdata["learningspace"])
        CreateTeachTask(login_driver).chekcbox_elements()
        CreateTeachTask(login_driver).click_btn()
        assert CreateTeachTask(login_driver).confirm_text==taskdata["confirmtext"]

