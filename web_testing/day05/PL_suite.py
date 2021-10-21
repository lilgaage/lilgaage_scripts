import unittest

# discover()方法生成测试套件
suite = unittest.defaultTestLoader.discover('./', 'ca*.py')
# 执行测试套件
unittest.TextTestRunner().run(suite)
