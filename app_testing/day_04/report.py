from app_testing.Tools.HTMLTestReportCN_New import HTMLTestRunner
import unittest
import time

# 生成测试套件
suite = unittest.defaultTestLoader.discover("./", "homework_*.py")

# 报告存放的路径
report_dir = "../Reports/"

now_time = time.strftime("%Y%m%d_%H%M%S")

# HTML报告的名字
report_name = report_dir + "考研帮app项目自动化测试报告_" + now_time + "_Report.html"

# 执行测试套件，生成测试报告
with open(report_name, 'wb') as file:
    # 实例化HTMLTestRunner
    runner = HTMLTestRunner(stream=file,
                            title="考研帮app自动化测试报告",
                            description="项目版本：2.3.4 "
                                        "appium: 3.141.0    "
                                        "操作系统:win7  "
                                        "python: 35.0+  "
                                        "pycharm:社区版    "
                                        "模拟器：夜神",
                            tester="lilgaage"
                            )
    # 执行测试套件
    runner.run(suite)
