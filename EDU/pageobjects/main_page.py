from common.basepage import BasePage
from selenium.webdriver.common.by import By
class MainPage(BasePage):
    #img_right=".logo-mini>img"
    #css方式定位
    #first_menu="#vuewrap>aside>div>section>ul>li:nth-child(1)>a"
    #查询学籍
    #last_menu="div.listwrap>div:nth-child(1)>ul>li:nth-child(2)>a"
    #添加学籍
    #last_menu="div.listwrap>div:nth-child(1)>ul>li:nth-child(1)"
    #xpath定位
    #first_menu="//span[text()='学籍管理']"
    #last_menu="//p[text()='查询学籍信息']"
    iframename="iframeundefined"
    def click_left(self,img_right):
        name="主页面-点击校徽展示图标"
        self.wait_elementvisibility(img_right,by=By.CSS_SELECTOR,model=name)
        self.click_element(img_right,by=By.CSS_SELECTOR,model=name)
    '''
    #没有参数化
    def click_firstmenu(self):
        name = "主页面-点击一级菜单"
        self.wait_elementvisibility(self.first_menu,by=By.CSS_SELECTOR,model=name)
        self.click_element(self.first_menu, by=By.CSS_SELECTOR, model=name)

    def click_lastmenu(self):
        name = "主页面-点击菜单进入页面"
        self.wait_elementvisibility(self.last_menu, by=By.CSS_SELECTOR, model=name)
        self.click_element(self.last_menu, by=By.CSS_SELECTOR, model=name)
    '''
    #将下拉框参数化
    def click_firstmenu(self,first_menu):
        name="主页面-点击一级菜单"
        self.wait_elementvisibility(first_menu, by=By.CSS_SELECTOR, model=name)
        self.click_element(first_menu,by=By.CSS_SELECTOR,model=name)
    def click_lastmenu(self,last_menu):
        name="主页面-点击菜单进入页面"
        self.wait_elementvisibility(last_menu, by=By.CSS_SELECTOR, model=name)
        self.click_element(last_menu, by=By.CSS_SELECTOR, model=name)

    def iframe_into(self):
        name = "切入iframe"
        self.switch_iframe_byname(self.iframename,model=name)
        #self.switch_iframe_byindex(0,model=name)
    def iframe_out(self):
        model="切出iframe"
        self.out_iframe()

    