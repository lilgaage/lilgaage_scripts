from common.HTMLTestReportCN_New import HTMLTestRunner
import unittest
import time
import os

# 获取文件根目录
path_root = os.path.realpath(__file__).split("test_run")[0]
print(path_root)

# 定义测试用例所在路径
# 生成测试套件
path_suite = path_root+"case\\"
suite = unittest.defaultTestLoader.discover(path_suite, "APITest*.py")

# 报告存放的路径
report_dir = path_root+"report\\"

now_time = time.strftime("%Y%m%d_%H%M%S")

# HTML报告的名字
report_name = report_dir + "学院增删改查接口测试" + now_time + "_Report.html"

# 执行测试套件，生成测试报告
with open(report_name, 'wb') as file:
    # 实例化HTMLTestRunner
    runner = HTMLTestRunner(stream=file,
                            title="学院增删改查接口测试",
                            description="操作系统:win7\t"
                                        "python: 35.0+\t"
                                        "pycharm:社区版",
                            tester="LilGaage"
                            )
    # 执行测试套件
    runner.run(suite)
