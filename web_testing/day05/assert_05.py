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

    def test_tieba(self):
        driver = self.driver
        driver.find_element_by_link_text('贴吧').click()
        sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        Expected = "百度贴吧"
        Actual = driver.title
        # 断言
        self.assertIn(Expected, Actual)

    def test_xueshu(self):
        driver = self.driver
        driver.find_element_by_link_text('学术').click()
        driver.switch_to.window(driver.window_handles[1])
        Expected = "https://xueshu.baidu.com/"
        Actual = driver.current_url
        # 断言
        self.assertEqual(Expected, Actual)

    def test_001(self):
        self.assertEqual(4*5, 20)

    def test_002(self):
        # AssertionError: '李张格' != 'lilgaage'
        self.assertEqual("李张格", "lilgaage")

    def test_003(self):
        self.assertIn("ghost", "lilghost")

    def test_004(self):
        # AssertionError: '瑰丝' not found in '小瑰'
        self.assertIn("瑰丝", "小瑰")

if __name__ == '__main__':
    unittest.main()

