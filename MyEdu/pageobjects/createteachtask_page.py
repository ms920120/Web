from selenium.webdriver.common.by import By
from common.basepage import BasePage
class CreateTeachTask(BasePage):
    semester="dlstSemester"
    learningspace="dllLearningSpace"
    #本科
    #blevel="ckblstTrainLevel1"
    #专科
    #zlevel="ckblstTrainLevel6"
    #辅修双学位
    #flevel="ckblstTrainLevel7"
    save="btnNext"
    def select_semester(self,sval):
        name="教学任务_下拉选择学期"
        self.wait_elementvisibility(self.semester,by=By.ID,model=name)
        self.select_element(self.semester,21,by=By.ID,model=name)
    def select_learningspace(self,lval):
        name="教学任务_下拉框选择校区"
        self.wait_elementvisibility(self.learningspace,by=By.ID,model=name)
        self.select_element(self.learningspace,lval,by=By.ID,model=name)
    def click_btn(self):
        name="教学任务_点击保存按钮"
        self.wait_elementvisibility(self.save,by=By.ID,model=name)
        self.click_element(self.save,by=By.ID,model=name)


