import unittest
from unittest_05 import Case01

# 实例化测试套件
suite = unittest.TestSuite()

# 给测试套件添加测试用例
# # 方法1 addTest(类名(方法名)) 添加指定类中指定的以test开头的方法
# suite.addTest(Case01('test_001'))
# suite.addTest(Case01('test_002'))
# suite.addTest(Case01('test_004'))

# 方法2 addTest.makeSuite(类名) 添加指定类中所有以test开头的方法
suite1 = unittest.TestSuite()
suite1.addTest(unittest.makeSuite(Case01))

# 实例化测试执行
runner = unittest.TextTestRunner()
# 调用run方法执行测试套件
runner.run(suite1)
