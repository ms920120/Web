
import os

# 框架项目顶层目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

testdatas_dir = os.path.join(BASE_DIR, "testdatas")

testcases_dir = os.path.join(BASE_DIR, "testcases")

htmlreport_dir = os.path.join(BASE_DIR, "report")

logs_dir = os.path.join(BASE_DIR, "logs")

screenshot_dir = os.path.join(BASE_DIR, "screenshot")
