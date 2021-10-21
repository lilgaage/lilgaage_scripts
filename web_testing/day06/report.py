from Tools.HTMLTestReportCN_New import HTMLTestRunner
import unittest
import time

# 生成测试套件
suite = unittest.defaultTestLoader.discover("cases/", "ca*.py")

# 报告存放的路径
report_dir = "reports/"

now_time = time.strftime("%Y%m%d_%H%M%S")

# HTML报告的名字
report_name = report_dir + "XXX项目自动化测试报告_" + now_time + "_Report.html"

# 执行测试套件，生成测试报告
with open(report_name, 'wb') as file:
    # 实例化HTMLTestRunner
    runner = HTMLTestRunner(stream=file,
                            title="XXX网站自动化测试报告",
                            description="项目版本：2.3.4"
                                        "selenium: 3.141.0"
                                        "操作系统:win7"
                                        "pthon: 35.0+"
                                        "pycharm :社区版"
                                        "浏览器： Chrome92.0 或Firefox60.0",
                            tester="lilgaage"
                            )
    # 执行测试套件
    runner.run(suite)
