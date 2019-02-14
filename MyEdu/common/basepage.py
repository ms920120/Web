import logging
import datetime
import time
import random
from common import log
from common import dir_config
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
class BasePage:
    def __init__(self,driver):
        self.driver=driver
        #self.driver=webdriver.Chrome()
    #等待元素可见
    def wait_elementvisibility(self,locator,by=By.XPATH,model="model",wait=20,requence=0.5):
        """
        :param locator:
        :param by:
        :param model:
        :param wait:
        :param requence:
        :return:
        """
        try:
            starttime=datetime.datetime.now()
            WebDriverWait(self.driver,wait,requence).until(EC.visibility_of_element_located((by,locator)))
            endtime=datetime.datetime.now()
            waittime=(starttime-endtime).seconds
            logging.info("等待元素可见：{0}，开始等待时间：{1}，等待结束时间{2}，等待时间间隔：{3}".format(locator, starttime, endtime, waittime))
        except:
            logging.exception("等待元素可见异常。")
            self._screenshort(model)
            raise
    #等待元素加载到dome树
    def wait_elementpresence(self,locator,by=By.XPATH,model="model",wait=20,requence=0.5):
        """
        :param locator:
        :param by:
        :param model:
        :param wait:
        :param requence:
        :return:
        """
        try:
            starttime = datetime.datetime.now()
            WebDriverWait(self.driver,wait,requence).until(EC.presence_of_element_located((by,locator)))
            endtime = datetime.datetime.now()
            waittime = (starttime - endtime).seconds
            logging.info("等待元素可见：{0}，开始等待时间：{1}，等待结束时间{2}，等待时间间隔：{3}".format(locator, starttime, endtime, waittime))
        except:
            logging.info("等待元素加载到dom树出现异常。")
            self._screenshot(model)
            raise
    #通过智能等待的方式切入iframe
    def frame_to_be_available(self,locator,by=By.XPATH,model="model",wait=20,requence=0.5):
        """
        :param locator:
        :param by:
        :param model:
        :param wait:
        :param requence:
        :return:
        """
        try:
            logging.info("通过{0}方式切入{1}。".format(by, locator))
            starttime = datetime.datetime.now()
            WebDriverWait(self.driver,wait,requence).until(EC.frame_to_be_available_and_switch_to_it((by,locator)))
            endtime = datetime.datetime.now()
            waittime = (starttime - endtime).seconds
            logging.info("等iframe框架加载出来并切入框架：{0}，开始等待时间：{1}，等待结束时间{2}，等待时间间隔：{3}".format(locator, starttime, endtime, waittime))
        except:
            logging.info("等iframe框架加载出来并切入框架出现异常。")
            self._screenshort(model)
            raise
    #切入iframe通过名字
    def switch_iframe_byname(self,name,model="model"):
        try:
            logging.info("通过iframe的名字{0}查找iframe")
            self.driver.switch_to.frame(name)
        except:
            logging.info("通过iframe的name属性查找iframe出现异常。")
            self._screenshort(model)
            raise
    #切入iframe通过iframe的索引，索引下标从0开始
    def switch_iframe_byindex(self,frame_index,model="model"):
        try:
            self.driver.switch_to.frame(frame_index)
        except:
            logging.exception("通过索引的方式查找元素出现异常。")
            self._screenshort(model)
            raise
    #切出iframe
    def out_iframe(self,model="model"):
        self.driver.switch_to.default_content()
    #查找一个元素
    def find_element(self,locator,by=By.XPATH,model="model"):
        """
        :param locator:
        :param by:
        :param model:
        :return:
        """
        logging.info("通过{0}方式，查找元素{1}。")
        try:
            return self.driver.find_element(by,locator)
        except:
            logging.exception("查找元素出现异常。")
            self._screenshort(model)
            raise
    #查找多个元素
    def find_elements(self,locator,by=By.XPATH,model="model"):
        """
        :param locator:
        :param by:
        :param model:
        :return:
        """
        logging.info("通过{0}方式查找符合的多个元素{1}".format(by, locator))
        try:
            return self.driver.find_elements(by,locator)
        except:
            logging.exception("查找多个元素出现异常。")
            self._screenshort(model)
            raise
    #元素点击操作
    def click_element(self,locator,by=By.XPATH,model="model",index=None):
        """
        :param locator:
        :param by:
        :param model:
        :param index:
        :return:
        """
        logging.info("执行元素点击操作。")
        try:
            self._get_element(locator,by,model,index).click()
        except:
            logging.info("执行元素点击事件出现异常。")
            self._screenshort(model)
            raise
    #复选框处理
    def decide_element(self,locator,by=By.XPATH,model="model"):
        """

        :param locator: 定位表达式
        :param by: 定位的方式
        :param model: 模块
        :return:
        """
        logging.info("判断复选框是否选中操作")
        try:
            decide=self.find_elements(locator,by,model)
            for i in decide:
                i_select=i.is_selected()
                print(i_select)
                print("aaaaaaaa")
                if i_select==False:
                    print("bbbbbbbb")
                    self.i.click()
                    print("cccccccc")
        except:
            logging.info("执行复选框勾选元素出现异常。")
            self._screenshort(model)
            raise

    #获取元素属性
    def get_attribute(self,locator,attr_name,by=By.XPATH,model="model",index=None):
        logging.info("获取元素属性操作。")
        try:
            self._get_element(locator,by,model,index).get_attribute(attr_name)
        except:
            logging.exception("获取元素属性出现异常。")
            self._screenshort(model)
            raise
    #通过写js语句或者jq方式移除属性
    def remove_attribute(self,locator,attrname,by=By.ID,model="model"):
        logging.info("移除元素属性操作")
        try:
            self.driver.execute_script("document.getElementById('{0}').removeAttribute('{1}')".format(locator,attrname))

        except:
            logging.exception("移除元素属性出现异常。")
            self._screenshort(model)
            raise
        pass
    #获得元素文本
    def get_text(self,locator,by=By.XPATH,model="model",index=None):
        logging.info("测试{0}，通过{1}元素定位方式，定位{2}元素".format(model, by, locator))
        try:
            return self._get_element(locator,by,model,index).text
        except:
            logging.exception("获取元素文本出现异常。")
            self._screenshort(model)
            raise
    #清除文本框内的文本信息
    def clear_input(self,locator,by=By.XPATH,model="model"):
        logging.info("清除文本框内容操作。")
        try:
            self._get_element(locator,by,model).clear()
        except:
            logging.info("清除文本框内容操作出现异常。")
            self._screenshort(model)
            raise
    #获取表格中表头单元格数据
    def get_thead(self,locator,tr_tag,td_tag,by=By.XPATH,model="model"):
        pass
    #获取表格中表格主体单元格数据
    #是否可以考虑大佬说的pandas模块爬取数据放到excel里面在去取出来在对比？？？？？？记得尝试啊！！！！！
    #获取除了表格第一行，和第一列以外的数据
    def get_table(self,locator,tr_tag,td_tag,td_start,td_end,by=By.XPATH,model="model"):
        """
        :param locator:表格元素定位
        :param tr_tag:表格行标签tr或者th标签
        :param td_tag:表格列标签td
        :param td_start: 获取数据开始列
        :param td_end: 获取数据结束列（注意此处遍历的是列表的数据，通过索引下标取值注意取左不取右）
        :param by:表格定位方式
        :param model:测试模块名称
        :return:
        """
        logging.info("获取表格数据操作。")
        try:
            self.wait_elementvisibility(locator,by,model)
            table_tr=self.driver.find_element(by,locator).find_elements(By.TAG_NAME,tr_tag)
            table_list=[]
            #遍历除表头外的行
            for tr in table_tr[1:]:
                table_td=tr.find_elements(By.TAG_NAME,td_tag)
                td_list=[]
                #由于项目单元格的复选框没有意义所以取数据的时候考虑不取第一列数据
                for td in table_td[td_start:td_end]:
                    td_list.append(td.text)
                table_list.append(td_list)
            return table_list
        except:
            logging.exception("获取页面表格数据出现异常。")
            raise
    #通过滚动条将元素滚动到可见区域
    def scrollintoview(self,locator,by=By.XPATH,model="model",index=None):
        logging.info("通过操作滚动条将元素展示在可见区域，在{0}，通过{1}定位方式，将{1}元素滚动到可见区域操作。".format(model, by, locator))
        try:
            self.driver.execute_script("Arguments[0].scrollIntoView",self._get_element(locator,by,model,index))
        except:
            logging.exception("将元素滚动到可见区域出现异常。")
            self._screenshort(model)
            raise
    #通过获取元素焦点将元素展示到可见区域
    def focus_element(self,locator,by=By.XPATH,model="model",index=None):
        logging.info("通过获取焦点将元素展示在可见区域，在{0}，通过{1}定位方式，将{1}元素滚动到可见区域操作。".format(model, by, locator))
        try:
            self.driver.execute_script("Arguments[0].focus",self._get_element(locator,by,model,index))
        except:
            logging.exception("通过获取焦点方式将元素展示到可见区域出现异常。")
            self._screenshort(model)
            raise
    #元素输入操作
    def send_keys_element(self,locator,value,by=By.XPATH,model="model",index=None):
        logging.info("执行元素输入操作。")
        try:
            self._get_element(locator,by,model,index).send_keys(value)
        except:
            logging.exception("执行元素输入操作出现异常。")
            self._screenshort(model)
            raise
    #下拉框选择元素操作
    def select_element(self,locator,num_value,mark="value",by=By.XPATH,model="model",index=None):
        """
        :param locator:元素定位
        :param num_value: 下拉框通过索引选择则填写数字，若通过value只选择则填写相关的value字符串
        :param mark: 下拉框选择元素的方式通过索引选择或者通过value值选择，根据mark参数传的值选择具体下拉框选择值的操作方式
        :param by:元素定位方式
        :param model:测试模块名称
        :param index:index:index=None则选择一个元素，index!=None则选择多个元素
        :return:
        """
        logging.info("下拉选择元素操作。")
        try:
            if mark.lower()=="value":
                Select(self._get_element(locator, by, model, index)).select_by_value(num_value)
            elif mark.lower()=="num":
                Select(self._get_element(locator, by, model, index)).select_by_index(num_value)
            else:
                logging.exception("下拉框元素选择方式出错。")
        except:
            logging.exception("执行下拉框选择元素出现异常")
            self._screenshort(model)
            raise

    #截图操作并且保存在相关目录下
    def _screenshort(self,model="model"):
        """
        :param model:
        :return:
        """
        filepath=dir_config.screenshot_dir+"\{0}-{1}.png".format(model,time.strftime("%Y-%m-%d %H-%M-%S",time.localtime()))
        self.driver.save_screenshot(filepath)
        logging.info("截图成功保存路径为{0}".format(filepath))

    # 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
    def _get_element(self,locator,by=By.XPATH,model="model",index=None):
        """
        :param locator:元素定位表达式
        :param by:元素定位的方式
        :param model:模块名
        :param index:index=None则选择一个元素，index!=None则选择多个元素若index=-1或index<0则随机选择多个元素
        :return:
        """
        if index is not None:
            return self._select_ele_from_elements(locator,by,index)
        else:
            return self.find_element(locator,by,model)
    #在查找的元素中随机选择元素还是按照多个元素的下标查找
    def _select_ele_from_elements(self,locator,by=By.XPATH,model="model",index=-1):
        """
        :param locator:元素定位表达式
        :param by:元素定位的方式
        :param model:模块名
        :param index:index=-1或者index<0则随机选择一个，index>0则按照下标选择元素
        :return:
        """
        eles = self.find_elements(by, locator)
        if index==-1 or index<0:
            pos=random.randint(0,len(eles)-1)
            return eles[pos]
        else:
            return eles[index]


