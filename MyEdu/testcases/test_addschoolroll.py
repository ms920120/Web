import pytest
import time
import logging
from common import log
from pageobjects.addschoolroll_page import AddSchoolRoll
from pageobjects.main_page import MainPage
from testdatas import addschoolroll_data as AD
class TestAddSchoolRoll:
    #@pytest.mark.smoke
    @pytest.mark.usefixtures("login_driver")
    #创建学籍参数化需要添加的数据,菜单数据，断言数据
    @pytest.mark.parametrize("inputschoolroll",AD.input_addschoolrolldata)
    #login_driver夹具中返回的参数
    #添加学籍点击暂存按钮
    def test_saveaddstudent(self,login_driver,inputschoolroll):
        MainPage(login_driver).click_left(inputschoolroll["left"])
        MainPage(login_driver).click_firstmenu(inputschoolroll["firstmenu"])
        MainPage(login_driver).click_lastmenu(inputschoolroll["lastmenu"])
        MainPage(login_driver).iframe_into()
        time.sleep(3)
        #输入姓
        AddSchoolRoll(login_driver).firstname_input(inputschoolroll["firstname"])
        #输入名
        AddSchoolRoll(login_driver).lastname_input(inputschoolroll["lastname"])
        #输入曾用名
        AddSchoolRoll(login_driver).formername_input(inputschoolroll["formername"])
        #输入性别
        AddSchoolRoll(login_driver).select_sex(inputschoolroll["sexval"])
        #输入英文姓
        AddSchoolRoll(login_driver).engfamilyname_input(inputschoolroll["engfamilyname"])
        #输入英文名
        AddSchoolRoll(login_driver).engfirstname_input(inputschoolroll["engfirstname"])
        #出生日期
        AddSchoolRoll(login_driver).birth_input(inputschoolroll["datatime"],inputschoolroll["birth"])
        #国籍
        AddSchoolRoll(login_driver).ddlcountrycode_select(inputschoolroll["countrycodeval"])
        #民族
        AddSchoolRoll(login_driver).ddlnationality_select(inputschoolroll["nationval"])
        #政治面貌
        AddSchoolRoll(login_driver).ddlpoliticalStatus_select(inputschoolroll["politicalval"])
        #籍贯
        AddSchoolRoll(login_driver).nativeplace_input(inputschoolroll["place"])
        #证件类型
        AddSchoolRoll(login_driver).ddlcardtype_select(inputschoolroll["cardtypeval"])
        #证件号
        AddSchoolRoll(login_driver).cardno_input(inputschoolroll["cardno"])
        #有效期
        AddSchoolRoll(login_driver).visaeffectivedate_input(inputschoolroll["datatime"],inputschoolroll["visaeffectivedate"])
        #婚姻状况
        AddSchoolRoll(login_driver).ddlmarriage_select(inputschoolroll["marriage"])
        #母语
        AddSchoolRoll(login_driver).ddlativelanguage_select(inputschoolroll["language"])
        #语言能力
        AddSchoolRoll(login_driver).ddlmaindarin_select(inputschoolroll["maindarin"])
        #输入学号
        AddSchoolRoll(login_driver).schoolrollnumber_input(inputschoolroll["snum"])
        #选择组织机构
        AddSchoolRoll(login_driver).ddldepartment_select(inputschoolroll["department"])
        #年级
        AddSchoolRoll(login_driver).ddlgrade_select(inputschoolroll["grade"])
        #培养层次
        AddSchoolRoll(login_driver).ddltrainlevel_select(inputschoolroll["trainlevel"])
        #学制
        AddSchoolRoll(login_driver).schoolsystem_input(inputschoolroll["yearattr"],inputschoolroll["year"])
        #培养方案
        AddSchoolRoll(login_driver).ddlprogram_select(inputschoolroll["program"])
        #学生类别
        AddSchoolRoll(login_driver).ddlstudytype_select(inputschoolroll["stutype"])
        #学习形式
        AddSchoolRoll(login_driver).ddlstudytype_select(inputschoolroll["studytype"])
        #分流方向
        AddSchoolRoll(login_driver).ddldistributary_select(inputschoolroll["butary"])
        #入学年级
        AddSchoolRoll(login_driver).ddlentergrade_select(inputschoolroll["ingrade"])
        #入学日期
        AddSchoolRoll(login_driver).enterdate_input(inputschoolroll["datatime"],inputschoolroll["enterdate"])
        #毕业日期
        AddSchoolRoll(login_driver).enddate_input(inputschoolroll["datatime"],inputschoolroll["enddate"])
        #考生号
        AddSchoolRoll(login_driver).txtstudentexamcode_input(inputschoolroll["stucode"])
        #招生类别
        AddSchoolRoll(login_driver).ddlstudentsoursetype_select(inputschoolroll["stusoursettype"])
        #生源地
        AddSchoolRoll(login_driver).ddlsourcerea_select(inputschoolroll["area"])
        #暂存按钮
        AddSchoolRoll(login_driver).savebtn_click()
        AddSchoolRoll(login_driver).confirm_click()
        time.sleep(3)
        querydata=AddSchoolRoll(login_driver).querytable()
        print(querydata)
        assert  inputschoolroll["num"] in querydata
    #添加学籍点击提交按钮
    def test_submitaddstudent(self,login_driver,addschoolrollmenu,inputschoolroll):
        MainPage(login_driver).click_left()
        MainPage(login_driver).click_firstmenu(addschoolrollmenu["firstmenu"])
        MainPage(login_driver).click_lastmenu(addschoolrollmenu["lastmenu"])
        #输入姓
        AddSchoolRoll(login_driver).firstname_input(inputschoolroll["firstname"])
        #输入名
        AddSchoolRoll(login_driver).lastname_input(inputschoolroll["lastname"])
        #输入曾用名
        AddSchoolRoll(login_driver).formername_input(inputschoolroll["formername"])
        #输入性别
        AddSchoolRoll(login_driver).select_sex(inputschoolroll["sexval"])
        #输入英文姓
        AddSchoolRoll(login_driver).engfamilyname_input(inputschoolroll["engfamilyname"])
        #输入英文名
        AddSchoolRoll(login_driver).engfirstname_input(inputschoolroll["engfirstname"])
        #出生日期
        AddSchoolRoll(login_driver).birth_input(inputschoolroll["datatime"],inputschoolroll["birth"])
        #国籍
        AddSchoolRoll(login_driver).ddlcountrycode_select(inputschoolroll["countrycodeval"])
        #民族
        AddSchoolRoll(login_driver).ddlnationality_select(inputschoolroll["nationval"])
        #政治面貌
        AddSchoolRoll(login_driver).ddlpoliticalStatus_select(inputschoolroll["politicalval"])
        #籍贯
        AddSchoolRoll(login_driver).nativeplace(inputschoolroll["nplaceval"])
        #证件类型
        AddSchoolRoll(login_driver).ddlcardtype_select(inputschoolroll["cardtypeval"])
        #证件号
        AddSchoolRoll(login_driver).cardno_input(inputschoolroll["cardno"])
        #有效期
        AddSchoolRoll(login_driver).visaeffectivedate(inputschoolroll["visaeffectivedate"])
        #婚姻状况
        AddSchoolRoll(login_driver).ddlmarriage_select(inputschoolroll["marriage"])
        #母语
        AddSchoolRoll(login_driver).ddlativelanguage(inputschoolroll["language"])
        #语言能力
        AddSchoolRoll(login_driver).ddlmaindarin_select(inputschoolroll["maindarin"])
        #输入学号
        AddSchoolRoll(login_driver).schoolrollnumber_input(inputschoolroll["snum"])
        #选择组织机构
        AddSchoolRoll(login_driver).ddldepartment_select(inputschoolroll["department"])
        #年级
        AddSchoolRoll(login_driver).ddlgrade_select(inputschoolroll["grade"])
        #培养层次
        AddSchoolRoll(login_driver).ddltrainlevel_select(inputschoolroll["trainlevel"])
        #学制
        AddSchoolRoll(login_driver).schoolsystem_input(inputschoolroll["year"])
        #培养方案
        AddSchoolRoll(login_driver).ddlprogram_select(inputschoolroll["program"])
        #学生类别
        AddSchoolRoll(login_driver).ddlstudentsoursetype_select(inputschoolroll["stutype"])
        #学习形式
        AddSchoolRoll(login_driver).ddlstudytype_select(inputschoolroll["studytype"])
        #分流方向
        AddSchoolRoll(login_driver).ddldistributary_select(inputschoolroll["butary"])
        #入学年级
        AddSchoolRoll(login_driver).ddlentergrade_select(inputschoolroll["ingrade"])
        #入学日期
        AddSchoolRoll(login_driver).enterdate_input(inputschoolroll["datetime"],inputschoolroll["enterdate"])
        #毕业日期
        AddSchoolRoll(login_driver).enddate_input(inputschoolroll["datetime"],inputschoolroll["enddate"])
        #考生号
        AddSchoolRoll(login_driver).txtstudentexamcode_input(inputschoolroll["stucode"])
        #招生类别
        AddSchoolRoll(login_driver).ddlstudentsoursetype_select(inputschoolroll["stusoursettype"])
        #生源地
        AddSchoolRoll(login_driver).ddlsourcerea_select(inputschoolroll["area"])
        #暂存按钮
        AddSchoolRoll(login_driver).savebtn_click()