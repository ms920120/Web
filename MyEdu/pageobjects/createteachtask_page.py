from selenium.webdriver.common.by import By
from common.basepage import BasePage
class CreateTeachTask(BasePage):
    semester="dlstSemester"
    learningspace="dllLearningSpace"
    checkbox="//input[@type='checkbox']"
    #本科
    #blevel="ckblstTrainLevel1"
    #专科
    #zlevel="ckblstTrainLevel6"
    #辅修双学位
    #flevel="ckblstTrainLevel7"
    save="btnNext"
    confirm="//span[text()='确定']"
    confirm_text="//div[contains(text(),'创建成功')]"
    def select_semester(self,sval):
        name="教学任务_下拉选择学期"
        self.wait_elementvisibility(self.semester,by=By.ID,model=name)
        self.select_element(self.semester,sval,by=By.ID,model=name)
    def select_learningspace(self,lval):
        name="教学任务_下拉框选择校区"
        self.wait_elementvisibility(self.learningspace,by=By.ID,model=name)
        self.select_element(self.learningspace,lval,by=By.ID,model=name)
    def chekcbox_elements(self):
        name="教学任务_下拉框的处理"
        self.wait_elementvisibility(self.checkbox,model=name)
        self.decide_element(self.checkbox,model=name)
    def click_btn(self):
        name="教学任务_点击保存按钮"
        self.wait_elementvisibility(self.save,by=By.ID,model=name)
        self.click_element(self.save,by=By.ID,model=name)
    def getalter_text(self):
        name="教学任务_获取创建成功后的弹窗内的文本框的提示信息"
        self.wait_elementvisibility(self.confirm_text,model=name)
        return  self.get_text(self.confirm_text,model=name)
    def click_confirm(self):
        name="教学任务_点击创建教学任务成功后的弹窗按钮"
        self.wait_elementvisibility(self.confirm,model=name)
        self.click_element(self.confirm,model=name)


