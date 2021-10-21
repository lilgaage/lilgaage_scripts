from selenium import webdriver
from time import sleep
import time
# 导入测试框架
import unittest

# 测试类
class Case01(unittest.TestCase):
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
        self.driver.find_element_by_link_text('hao123').click()

    def test_002(self):
        self.driver.find_element_by_link_text('地图').click()

    def test_003(self):
        driver = self.driver
        now_time = time.strftime("%Y%m%d_%H%M%S")
        driver.find_element_by_id('kw').send_keys('李张格')
        driver.find_element_by_id('su').click()
        sleep(1)
        driver.get_screenshot_as_file("images/img_{}_李张格首页.png".format(now_time))
        driver.find_element_by_link_text('免费学无人机,武汉一高校社团开“飞手”培训课被“秒光”-...').click()
        # 切换窗口
        driver.switch_to.window(driver.window_handles[1])
        sleep(1)
        driver.get_screenshot_as_file("images/img_{}_无人机新闻.png".format(now_time))
        driver.find_element_by_link_text('首页').click()
        driver.get_screenshot_as_file("images/img_{}_站长头条首页.png".format(now_time))

    def test_004(self):
        self.driver.find_element_by_link_text('新闻').click()

    def test_005(self):
        self.driver.find_element_by_link_text('贴吧').click()


# 自测代码
if __name__ == '__main__':
    # 自动搜索脚本中所有以test开头的方法并执行
    unittest.main()


