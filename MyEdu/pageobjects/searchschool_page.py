from selenium.webdriver.common.by import By
from common.basepage import BasePage
class SearchSchoolPage(BasePage):
    #院系
    organization="ddlOrganization"
    #年级
    grade="ddlGrade"
    #专业
    major="ddlMajor"
    #学号
    snum="SchoolRollNumber"
    #姓名
    sname="txtName"
    #查询按钮
    btn="//input[@value='查询']"
    #根据学号验证查询结果
    tdata="tableLst"

    def select_organization(self,orgval):
        name="查询学籍信息--选择院系"
        self.wait_elementvisibility(self.organization,by=By.ID,model=name)
        self.select_element(self.organization,orgval, by=By.ID, model=name)
        #self.select_element(self.organization,"18",by=By.ID,model=name)
    def select_grade(self,gradeval):
        name="查询学籍信息--选择年级"
        self.wait_elementvisibility(self.grade,by=By.ID,model=name)
        self.select_element(self.grade, gradeval, by=By.ID, model=name)
        #self.select_element(self.grade,"14",by=By.ID,model=name)
    def select_major(self,majorval):
        name="查询学籍信息--选择专业"
        self.wait_elementvisibility(self.major,by=By.ID,model=name)
        #self.select_element(self.major,"3",by=By.ID,model=name)
        self.select_element(self.major,majorval, by=By.ID, model=name)
    def inputsnum(self,stunum):
        name = "查询学籍信息--输入学号"
        self.wait_elementvisibility(self.snum,by=By.ID,model=name)
        #self.send_keys_element(self.snum,"1222170101",by=By.ID,model=name)
        self.send_keys_element(self.snum, stunum, by=By.ID, model=name)
    def inputsname(self,stuname):
        name = "查询学籍信息--输入姓名"
        self.wait_elementvisibility(self.sname,by=By.ID,model=name)
        #self.send_keys_element(self.sname,"郭子琳",by=By.ID,model=name)
        self.send_keys_element(self.sname, stuname, by=By.ID, model=name)
    def click_btn(self):
        name="查询学籍信息--点击查询按钮"
        self.wait_elementvisibility(self.btn,model=name)
        self.click_element(self.btn,model=name)
    def get_tabledata(self):
        name="查询学籍信息--获取表格数据"
        #1表示获取那列的数据
        return self.get_table(self.tdata,"tr","td",1,14,by=By.ID,model=name)
