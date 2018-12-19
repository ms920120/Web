import pytest
import logging
import time
from common import log
from pageobjects.main_page import MainPage
from pageobjects.searchschool_page import SearchSchoolPage
from testdatas import searchschoolroll_data as SD
class TestSearchSchoolRoll:
    #次查询测试用例需要考虑分页的情况
    #@pytest.mark.smoke
    #查询条件参数化
    @pytest.mark.parametrize("search_data", SD.search_data)
    #断言数据
    @pytest.mark.parametrize("querysearchschoolroll",SD.searchschoolroll_data)
    @pytest.mark.usefixtures("login_driver")
    def test_schoolroll(self,login_driver,search_data,querysearchschoolroll):
        MainPage(login_driver).click_left(search_data["left"])
        MainPage(login_driver).click_firstmenu(search_data["firstmenu"])
        MainPage(login_driver).click_lastmenu(search_data["lastmenu"])
        MainPage(login_driver).iframe_into()
        time.sleep(3)
        #下拉框选择院系
        SearchSchoolPage(login_driver).select_organization(search_data["orgval"])
        #下拉框选择年级
        SearchSchoolPage(login_driver).select_grade(search_data["gradeval"])
        #下拉框选择专业
        SearchSchoolPage(login_driver).select_major(search_data["majorval"])
        #文本框输入学号
        SearchSchoolPage(login_driver).inputsnum(search_data["stunum"])
        #文本框输入姓名
        SearchSchoolPage(login_driver).inputsname(search_data["stuname"])
        SearchSchoolPage(login_driver).click_btn()
        time.sleep(3)
        tdata=SearchSchoolPage(login_driver).get_tabledata()
        print("aaaaaaaaaaaaaaaa")
        print(tdata)
        assert tdata==querysearchschoolroll
        print(111111111111111)

