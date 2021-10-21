import time

from selenium import webdriver
from time import sleep
import unittest

# 测试类
class Case03(unittest.TestCase):
    # 每一个test开头的方法执行前都会执行setUp方法
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://www.baidu.com")

    # 每一个test开头的方法执行后都会执行tearDown方法
    def tearDown(self) -> None:
        sleep(2)
        self.driver.quit()

    def test_xueshu(self):
        driver = self.driver
        driver.find_element_by_link_text('学术').click()
        driver.switch_to.window(driver.window_handles[1])
        try:
            # 预期结果
            Expected = "https://xueshu.baidu.com"
            # 获取当前网页URL 实际结果
            Actual = driver.current_url
            # 断言
            self.assertEqual(Expected, Actual)
            # 在百度学术搜索自己名字
            driver.find_element_by_id('kw').send_keys('lilgaage')
            driver.find_element_by_id('su').click()
            sleep(2)
            # 动态时间
            now = time.strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file("images/img_{}_百度学术搜索lilgaage.png".format(now))
        # 捕获到指定异常--->断言失败
        except AssertionError:
            print("断言失败，进入的不是百度学术页面")
            # 截图
            now = time.strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file("images/img_{}_断言失败_不是百度学术搜索.png".format(now))
            # 抛出异常
            raise
        finally:
            print("断言结束")


if __name__ == '__main__':
    unittest.main()

