from API_Testing.Day10.test02.Tools.HTMLTestReportCN_New import HTMLTestRunner
import unittest
import time

# 生成测试套件
suite = unittest.defaultTestLoader.discover("./", "test*.py")

# 报告存放的路径
report_dir = "Reports/"

now_time = time.strftime("%Y%m%d_%H%M%S")

# HTML报告的名字
report_name = report_dir + "day10练习02" + now_time + "_Report.html"

# 执行测试套件，生成测试报告
with open(report_name, 'wb') as file:
    # 实例化HTMLTestRunner
    runner = HTMLTestRunner(stream=file,
                            title="day10练习02-学院信息接口测试",
                            description="增删改查的冒烟测试\t"
                                        "操作系统:win7\t"
                                        "python: 35.0+\t"
                                        "pycharm:社区版",
                            tester="LilGaage"
                            )
    # 执行测试套件
    runner.run(suite)
