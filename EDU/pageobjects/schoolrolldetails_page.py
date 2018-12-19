import time
from selenium.webdriver.common.by import By
from common.basepage import BasePage
class SchoolRollDetails(BasePage):
    table="//table[@class='TableCss']"
    def querytable(self):
        name="查询待提交表格数据"
        print(0000000000)
        time.sleep(10)
        self.wait_elementvisibility(self.table,by=By.XPATH,model=name)
        print(99999999999)
        print(self.get_table(self.table,"tr","td",0,12,by=By.XPATH,model=name))
        return self.get_table(self.table,"tr","td",0,12,by=By.XPATH,model=name)
