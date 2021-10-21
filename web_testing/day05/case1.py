from selenium import webdriver
from time import sleep
import time
# 导入测试框架
import unittest

# 测试类
class Case02(unittest.TestCase):
    # 每一个test开头的方法执行前都会执行setUp方法
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://www.baidu.com")

    # 每一个test开头的方法执行后都会执行tearDown方法
    def tearDown(self) -> None:
        sleep(3)
        self.driver.quit()

    def test_001(self):
        self.driver.find_element_by_link_text('学术').click()

    def test_002(self):
        self.driver.find_element_by_link_text('直播').click()

    def test_003(self):
        self.driver.find_element_by_link_text('新闻').click()

    def test_004(self):
        self.driver.find_element_by_link_text('视频').click()


# 自测代码
if __name__ == '__main__':
    # 自动搜索脚本中所有以test开头的方法并执行
    unittest.main()


