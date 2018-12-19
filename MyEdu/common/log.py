import time
import logging
from logging.handlers import RotatingFileHandler
from common import dir_config

# 定义日志输出的格式
format = ("%(asctime)s-%(levelname)s-%(filename)s-%(funcName)s-[ line:%(lineno)d-%(message)s")
# 定义日志输出的时间格式
datefmt = ("%a, %d %b %Y %H:%M:%S")
# 日志输出到屏幕
handle = logging.StreamHandler()
# 时间
curTime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
# 类似于filehandle可以管理文件的格式如果达到backupCount的个数会将当前日志文件自动改名，在创建一个新的同名文件自动输出
handle1 = RotatingFileHandler(dir_config.logs_dir + "/web-AutoLog{0}.log".format(curTime), backupCount=30,
                              encoding="utf-8")
# 日志的基本配置信息
logging.basicConfig(format=format, datefmt=datefmt, level=logging.INFO, handlers=[handle, handle1])