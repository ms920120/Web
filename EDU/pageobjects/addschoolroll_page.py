from selenium.webdriver.common.by import By
from common.basepage import BasePage
class AddSchoolRoll(BasePage):
    #姓（文本框）
    firstname="FirstName"
    #名（文本框）
    lastname="LastName"
    #曾用名（文本框）
    formername="FormerName"
    #性别（下）
    ddlgender="ddlGender"
    #英文姓（文本）
    engfamilyname="EngFamilyName"
    #英文名（文本）
    engfirstname="EngFirstName"
    # 出生日期（日期时间）
    birth = "Birth"
    #国籍（下）
    ddlcountrycode="ddlCountryCode"
    #民族（下）
    ddlnationality="ddlNationality"
    #政治面貌(下)
    ddlpoliticalStatus="ddlPoliticalStatus"
    #籍贯（文本框）
    nativeplace="NativePlace"
    #证件类型
    ddlardtype="ddlCardType"
    #证件号
    cardno="CardNo"
    #有效期
    visaeffectivedate="VisaEffectiveDate"
    #婚姻状况
    ddlmarriage="ddlMarriage"
    #母语
    ddlativelanguage="ddlNativeLanguage"
    #语言能力
    ddlmaindarin="ddlMainDarin"
    #学号
    schoolrollnumber="SchoolRollNumber"
    #组织机构
    ddldepartment="ddlDepartment"
    #年级
    ddlgrade="ddlGrade"
    #培养层次
    ddltrainlevel="ddlTrainLevel"
    #学制
    schoolsystem="SchoolSystem"
    #培养方案
    ddlprogram="ddlProgram"
    #学生类别
    ddlstudenttype="ddlStudentType"
    #学习形式
    ddlstudytype="ddlStudyType"
    #分流方向
    ddldistributary="ddlDistributary"
    #入学年级
    ddlentergrade="ddlEnterGrade"
    #入学日期
    enterdate="EnterDate"
    #毕业日期
    enddate="EndDate"
    #考生号
    txtstudentexamcode="txtStudentExamCode"
    #招生类别
    ddlstudentsoursetype="ddlStudentSourseType"
    #生源地
    ddlsourcerea="ddlSourceArea"
    #暂存按钮
    savebtn="//input[@value='暂存']"
    #提交按钮
    submit="//input[@value='提交']"
    #弹窗内的确认按钮
    confirm="//span[text()='确定']"
    #保存后表格数据
    table = "//table[@class='TableCss']"
    def firstname_input(self,firstname):
        name="姓名--输入姓"
        self.wait_elementvisibility(self.firstname,by=By.ID,model=name)
        self.send_keys_element(self.firstname,firstname,by=By.ID,model=name)

    def lastname_input(self,lastname):
        name="姓名--输入名"
        self.wait_elementvisibility(self.lastname,by=By.ID,model=name)
        self.send_keys_element(self.lastname,lastname,by=By.ID,model=name)

    #formername为曾用名处文本框填写的值，此处参数化了
    def formername_input(self,formername):
        name="输入曾用名"
        self.wait_elementvisibility(self.formername,by=By.ID,model=name)
        self.send_keys_element(self.formername,formername,by=By.ID,model=name)

    #value是下拉框中value属性的值
    def select_sex(self,sexval):
        name="下拉框选择性别"
        self.wait_elementvisibility(self.ddlgender,by=By.ID,model=name)
        self.select_element(self.ddlgender,sexval,by=By.ID,model=name)

    def engfamilyname_input(self,engfamilyname):
        name="英文名输入姓"
        self.wait_elementvisibility(self.engfamilyname,by=By.ID,model=name)
        self.send_keys_element(self.engfamilyname,engfamilyname,by=By.ID,model=name)

    def engfirstname_input(self,engfirstname):
        name="英文名输入名"
        self.wait_elementvisibility(self.engfirstname, by=By.ID, model=name)
        self.send_keys_element(self.engfirstname,engfirstname,by=By.ID, model=name)

    #日期控件的选择
    def birth_input(self,attrname,time):
        name="移除日期的属性，并设置出生日期的属性"
        self.wait_elementvisibility(self.birth,by=By.ID,model=name)
        self.remove_attribute(self.birth,attrname)
        self.send_keys_element(self.birth,time,by=By.ID,model=name)

    def ddlcountrycode_select(self,countrycodeval):
        name="下拉框选择国籍"
        self.wait_elementvisibility(self.ddlcountrycode,by=By.ID,model=name)
        self.select_element(self.ddlcountrycode,countrycodeval,by=By.ID,model=name)

    def ddlnationality_select(self,nationval):
        name="下拉框选择民族"
        self.wait_elementvisibility(self.ddlnationality, by=By.ID, model=name)
        self.select_element(self.ddlnationality,nationval, by=By.ID, model=name)

    def ddlpoliticalStatus_select(self,politicalval):
        name="下拉框选择政治面貌"
        self.wait_elementvisibility(self.ddlpoliticalStatus,by=By.ID,model=name)
        self.select_element(self.ddlpoliticalStatus,politicalval, by=By.ID, model=name)

    def nativeplace_input(self,place):
        name="输入籍贯"
        self.wait_elementvisibility(self.nativeplace, by=By.ID, model=name)
        self.send_keys_element(self.nativeplace,place,by=By.ID,model=name)

    def ddlcardtype_select(self,cardtypeval):
        name="下拉框选择证件类型"
        self.wait_elementvisibility(self.ddlardtype, by=By.ID, model=name)
        self.send_keys_element(self.ddlardtype,cardtypeval, by=By.ID, model=name)

    def cardno_input(self,cardno):
        name="输入证件号"
        self.wait_elementvisibility(self.cardno, by=By.ID, model=name)
        self.send_keys_element(self.cardno, cardno, by=By.ID, model=name)

    def visaeffectivedate_input(self,attrname,time):
        name="移除日期的属性，并设置有效期的属性"
        self.wait_elementvisibility(self.visaeffectivedate, by=By.ID, model=name)
        self.remove_attribute(self.visaeffectivedate,attrname,model=name)
        self.send_keys_element(self.visaeffectivedate,time, by=By.ID, model=name)

    def ddlmarriage_select(self,marriage):
        name="下拉框选择婚姻状况"
        self.wait_elementvisibility(self.ddlmarriage,by=By.ID,model=name)
        self.select_element(self.ddlmarriage,marriage,by=By.ID,model=name)

    def ddlativelanguage_select(self,language):
        name="下拉框选择母语"
        self.wait_elementvisibility(self.ddlativelanguage,by=By.ID,model=name)
        self.select_element(self.ddlativelanguage,language,by=By.ID,model=name)

    def ddlmaindarin_select(self,value):
        name="下拉框选择语言能力"
        self.wait_elementvisibility(self.ddlmaindarin, by=By.ID, model=name)
        self.select_element(self.ddlmaindarin,value, by=By.ID, model=name)

    def schoolrollnumber_input(self,snum):
        name="输入学号"
        self.wait_elementvisibility(self.schoolrollnumber,by=By.ID,model=name)
        self.send_keys_element(self.schoolrollnumber,snum,by=By.ID,model=name)

    def ddldepartment_select(self,department):
        name="下拉框选择组织机构"
        self.wait_elementvisibility(self.ddldepartment, by=By.ID, model=name)
        self.select_element(self.ddldepartment,department, by=By.ID, model=name)

    def ddlgrade_select(self,grade):
        name="下拉框选择年级"
        self.wait_elementvisibility(self.ddlgrade, by=By.ID, model=name)
        self.select_element(self.ddlgrade, grade, by=By.ID, model=name)

    def ddltrainlevel_select(self,trainlevel):
        name="下拉框选择培养层次"
        self.wait_elementvisibility(self.ddltrainlevel,by=By.ID,model=name)
        self.select_element(self.ddltrainlevel,trainlevel,by=By.ID,model=name)

    def schoolsystem_input(self,attrname,year):
        name="输入学制"
        self.wait_elementvisibility(self.schoolsystem,by=By.ID,model=name)
        self.remove_attribute(self.schoolsystem,attrname,by=By.ID,model=name)
        self.send_keys_element(self.schoolsystem,year,by=By.ID,model=name)

    def ddlprogram_select(self,program):
        name="下拉框选择培养方案"
        self.wait_elementvisibility(self.ddlprogram,by=By.ID,model=name)
        self.select_element(self.ddlprogram,program,by=By.ID,model=name)

    def ddlstudenttype_select(self,stutype):
        name="下拉框选择学生类别"
        self.wait_elementvisibility(self.ddlstudenttype,by=By.ID,model=name)
        self.select_element(self.ddlstudenttype,stutype,by=By.ID,model=name)

    def ddlstudytype_select(self,studytype):
        name = "下拉框选择学习形式"
        self.wait_elementvisibility(self.ddlstudenttype, by=By.ID, model=name)
        self.select_element(self.ddlstudenttype, studytype, by=By.ID, model=name)

    def ddldistributary_select(self,butary):
        name="下拉框选择分流方向"
        self.wait_elementvisibility(self.ddldistributary,by=By.ID,model=name)
        self.select_element(self.ddldistributary,butary,by=By.ID,model=name)

    def ddlentergrade_select(self,ingrade):
        name="下拉框选择入学年级"
        self.wait_elementvisibility(self.ddlentergrade, by=By.ID, model=name)
        self.select_element(self.ddlentergrade,ingrade, by=By.ID, model=name)

    def enterdate_input(self,attrname,time):
        name="日期时间控件输入入学日期"
        self.wait_elementvisibility(self.enterdate,by=By.ID,model=name)
        self.remove_attribute(self.enterdate,attrname,model=name)
        self.clear_input(self.enterdate, by=By.ID, model=name)
        self.send_keys_element(self.enterdate,time,by=By.ID,model=name)

    def enddate_input(self,attrname,time):
        name="日期时间时间控件输入毕业日期"
        self.wait_elementvisibility(self.enddate, by=By.ID, model=name)
        self.remove_attribute(self.enddate, attrname, model=name)
        self.clear_input(self.enddate, by=By.ID, model=name)
        self.send_keys_element(self.enddate, time, by=By.ID, model=name)

    def txtstudentexamcode_input(self,stucode):
        name="输入考生号"
        self.wait_elementvisibility(self.txtstudentexamcode,by=By.ID,model=name)
        self.send_keys_element(self.txtstudentexamcode,stucode,by=By.ID,model=name)

    def ddlstudentsoursetype_select(self,stusoursettype):
        name="下拉框选择招生类别"
        self.wait_elementvisibility(self.ddlstudentsoursetype,by=By.ID,model=name)
        self.select_element(self.ddlstudentsoursetype,stusoursettype,by=By.ID,model=name)

    def ddlsourcerea_select(self,area):
        name="下拉框选择生源地"
        self.wait_elementvisibility(self.ddlsourcerea, by=By.ID, model=name)
        self.select_element(self.ddlsourcerea,area, by=By.ID, model=name)
    def savebtn_click(self):
        name="点击暂存按钮"
        self.wait_elementvisibility(self.savebtn,by=By.XPATH,model=name)
        self.click_element(self.savebtn,by=By.XPATH,model=name)

    def submit_click(self):
        name="点击提交按钮"
        self.wait_elementvisibility(self.submit,by=By.XPATH,model=name)
        self.click_element(self.submit,by=By.XPATH,model=name)

    def confirm_click(self):
        name="点击弹出框的确认按钮"
        self.wait_elementvisibility(self.confirm,by=By.XPATH,model=name)
        self.click_element(self.confirm,by=By.XPATH,model=name)
    def querytable(self):
        name="查询待提交表格数据"
        print("aaaaaa")
        #time.sleep(10)
        self.wait_elementvisibility(self.table,by=By.XPATH,model=name)
        print("bbbbbbbb")
        print(self.get_table(self.table,"tr","td",0,1,by=By.XPATH,model=name))
        return self.get_table(self.table,"tr","td",0,1,by=By.XPATH,model=name)








