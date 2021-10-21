from app_testing.Func.KYB_Func import *
import unittest

class Case01(unittest.TestCase):
    def setUp(self) -> None:
        # 实例化webdriver
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        # 隐式等待
        self.driver.implicitly_wait(30)
        # 取消更新、跳过开场页面
        cancel_skip(self)
        # 登录
        login(self)
        # 点击【我知道了】
        self.driver.tap([(270, 461), (371, 472)], 1000)

    def tearDown(self) -> None:
        # 暂停、退出会话
        sleep(3)
        self.driver.quit()

    def test_luntan001(self):
        # 点击论坛
        self.driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum').click()
        # 点击第四条资讯
        self.driver.find_elements_by_id('com.tal.kaoyan:id/hot_thread_item_title')[3].click()
        sleep(2)
        # 截图
        PrtSc(self, "论坛模块第4条资讯")


if __name__ == '__main__':
    unittest.main()
