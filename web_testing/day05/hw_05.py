from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep
import unittest
import time

class Case01(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get('http://www.baidu.com')

    def tearDown(self) -> None:
        sleep(2)
        self.driver.quit()

    def test_gz(self):
        driver = self.driver
        action = ActionChains(driver)
        # 先定位【更多】
        more = driver.find_element_by_link_text('更多')
        action.move_to_element(more).perform()
        driver.find_element_by_link_text('知道').click()
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_id('kw').send_keys('广州')
        driver.find_element_by_id('search-btn').click()
        sleep(1)
        now = time.strftime("%Y%m%d_%H%M%S")
        driver.get_screenshot_as_file("images/img_{}_广州的知道页面.png".format(now))

    def test_sh(self):
        driver = self.driver
        driver.find_element_by_id('kw').send_keys('上海')
        driver.find_element_by_id('su').click()
        driver.find_element_by_partial_link_text('百度百科').click()
        driver.switch_to.window(driver.window_handles[1])
        js = "window.scrollTo(0,1000)"
        driver.execute_script(js)
        sleep(1)
        now = time.strftime("%Y%m%d_%H%M%S")
        driver.get_screenshot_as_file("images/img_{}_上海百度百科.png".format(now))

    def test_zg(self):
        driver = self.driver
        driver.find_element_by_id('kw').send_keys('中公教育')
        driver.find_element_by_id('su').click()
        driver.find_element_by_partial_link_text('公务员考试网').click()
        driver.switch_to.window(driver.window_handles[1])
        try:
            Expected = "https://www.offcn.com"
            Actual = driver.current_url
            self.assertEqual(Expected, Actual)
        except AssertionError:
            now = time.strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file("images/img_{}_断言失败，不是中公官网.png".format(now))
        else:
            action = ActionChains(driver)
            it_work = driver.find_element_by_link_text('IT 就 业')
            action.move_to_element(it_work).perform()
            now = time.strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file("images/img_{}_断言成功，中公官网IT就业页面.png".format(now))

# 自测代码
if __name__ == '__main__':
    unittest.main()
