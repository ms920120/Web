# 定义pytest的fixture
import pytest
import logging
import allure
from selenium import webdriver
from testdatas import common_data as CD
from pageobjects.login_page import LoginPage



# 定义一个函数，并在这个函数当中，实现用例的准备工作和清理工作。
# 在函数的前面加上 @pytest.fixture
# fixture可以设置作用域范围
@pytest.fixture  # 执行级别 控制是否重新传入新的 driver 对象
def login_driver():
    # 初始化浏览器会话（登录）
    logging.info("=====用例前置：初始化浏览器会话，登陆教务管理系统=======")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.login_url)
    LoginPage(driver).login_page(CD.user, CD.passwd)
    # yield 准备工作和清理工作的分限线。上面是准备工作。下面的是清理工作
    # 有返回值的情况下，返回值写在yield后面。
    #driver.status = True

    yield driver
    logging.info("=====用例后置：关闭浏览器会话,清理环境=======")
    driver.quit()


#
@pytest.fixture  # 执行级别 控制是否重新传入新的 driver 对象
def nologin_driver():
    # 初始化浏览器会话(未登录)
    logging.info("=====用例前置：初始化浏览器会话，登陆教务管理系统=======")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.login_url)
    yield driver
    logging.info("=====用例后置：关闭浏览器会话,清理环境=======")
    driver.quit()


# 图片禁止加载的功能

'''
1、定义fixture == conftest.py放测试用例要用到的初始化工作和清理 工作。
如果不同的功能有相同的准备和清理 工作，我们就可以直接共用 就好了

@pytest.fixture  == 默认是用例级
def XXX():
    XXXXXXXXXXX准备工作XXXXX
    yield  [返回值]
    XXXXX收尾工作XXXXXXXX


2、在测试用例或者测试类当中来使用fixture
@pytest.mark.usefixtures("fixture对应的函数名称")
有返回值的话，那每一个测试用例需要接收一个参数(fixture函数名称) = 返回值
然后在测试用例当中通过函数名称 来使用 返回值。

3、assert断言
'''
