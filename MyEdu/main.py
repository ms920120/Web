import pytest
pytest.main(["-m","smoke",
             #用例失败执行次数
            # "--reruns","2",
             #次数之间的延时设置，单位是秒
            # "--reruns-delay","5"
             "--html=report\\pytest_result.html",
             "--alluredir=report\\allurereport"])