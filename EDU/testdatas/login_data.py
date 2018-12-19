# 正常用例-登陆成功的数据
login_data =[{"user": "admin","passwd": "zbyw@zbyw","check_url": "http://211.103.188.27:8077/Navigation/main.aspx"},{"user": "admin","passwd": "zbyw@zbyw","check_url": "http://211.103.188.27:8077/Navigation/main.aspx"}]

success_data=[{"user": "admin","passwd": "zbyw@zbyw","check_url": "http://211.103.188.27:8077/Navigation/main.aspx",},
    {"user": "1704040101","passwd": "1704040101","check_url": "http://211.103.188.27:8077/Navigation/main.aspx",}]
# 用户名、密码为空
err_data=[{"user": "", "passwd": "admin", "check": "请输入用户名。"},
              {"user": "admin", "passwd": "", "check": "请输入密码。"}]
no_data = [
    {"user": "", "passwd": "123456", "check": "用户名不能为空"},
    {"user": "18733661948", "passwd": "", "check": "密码不能为空"},
    {"user": "1873366", "passwd": "123456", "check": "非法的手机号"}
]
# 错误的密码、尚未注册的用户
wrong_data = [
    {"user": "18733661948", "passwd": "123456789", "check": "账号信息错误"},
    {"user": "18600001100", "passwd": "python", "check": "账号信息错误"}
]
