from appium.webdriver.common.touch_action import TouchAction

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
        # 退出登录
        logout(self)
        # 暂停、退出会话
        sleep(3)
        self.driver.quit()

    def test_mytask001(self):
        # 点击 添加学习任务
        driver = self.driver
        driver.find_element_by_id('com.tal.kaoyan:id/task_no_task').click()
        # 添加背单词任务
        driver.find_element_by_id('com.tal.kaoyan:id/btnHot1').click()
        # 结束重复时间
        driver.find_element_by_id('com.tal.kaoyan:id/activity_date_addtask_selectdate_commitbtn').click()
        # 单击确定
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
        # 添加第二个背单词任务
        driver.find_element_by_id('com.tal.kaoyan:id/ivAddTask').click()
        # 添加背单词任务
        driver.find_element_by_id('com.tal.kaoyan:id/btnHot1').click()
        # 结束重复时间
        driver.find_element_by_id('com.tal.kaoyan:id/activity_date_addtask_selectdate_commitbtn').click()
        # 单击确定
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
        sleep(3)
        # 截图
        PrtSc(self, "验证能否添加两个相同的任务")

    def test_mytask002(self):
        driver = self.driver
        # 单击添加任务
        driver.find_element_by_id('com.tal.kaoyan:id/ivAddTask').click()
        # 单击“更多常用任务”
        driver.tap([(294, 349), (426, 379)], 1000)
        # 添加“看视频学习”
        driver.find_elements_by_id('com.tal.kaoyan:id/llButton')[5].click()
        # 单击确定
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
        sleep(3)
        # 截图
        PrtSc(self, "验证能否添加更多常用任务")

    def test_mytask003(self):
        driver = self.driver
        # 单击添加任务
        driver.find_element_by_id('com.tal.kaoyan:id/ivAddTask').click()
        # 自定义任务框输入“干饭”
        driver.find_element_by_id('com.tal.kaoyan:id/activity_date_addtask_tasktitle').send_keys("干饭")
        # 单击确定
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
        sleep(3)
        # 截图
        PrtSc(self, "验证能否添加自定义任务")

    def test_mytask004(self):
        driver = self.driver
        # 勾选我的任务列表前的第一个小方块
        driver.find_elements_by_id('com.tal.kaoyan:id/home_task_select')[0].click()
        # 勾选我的任务列表前的第二个小方块
        driver.find_elements_by_id('com.tal.kaoyan:id/home_task_select')[0].click()
        # 勾选我的任务列表前的第三个小方块
        driver.find_elements_by_id('com.tal.kaoyan:id/home_task_select')[1].click()
        # 勾选我的任务列表前的第四个小方块
        driver.find_elements_by_id('com.tal.kaoyan:id/home_task_select')[2].click()
        sleep(3)
        # 截图
        PrtSc(self, "验证勾选我的任务栏列表前的框是否代表任务已完成")

    def test_mytask005(self):
        driver = self.driver
        # 点击展开我的任务列表
        driver.find_element_by_id('com.tal.kaoyan:id/task_info_showall_text').click()
        # 勾选我的任务列表前的第一个小方块
        driver.find_elements_by_id('com.tal.kaoyan:id/home_task_select')[0].click()
        sleep(3)
        # 截图
        PrtSc(self, "验证取消勾选我的任务栏列表前的框，是否会重新出现任务列表")

    def test_mytask006(self):
        driver = self.driver
        # 单击添加任务
        driver.find_element_by_id('com.tal.kaoyan:id/ivAddTask').click()
        # 添加专业课任务
        driver.find_element_by_id('com.tal.kaoyan:id/btnHot3').click()
        # 取消勾选“全天”
        driver.find_element_by_id('com.tal.kaoyan:id/activity_date_addtask_allday_switch').click()
        # 单击“提醒”
        driver.find_element_by_id('com.tal.kaoyan:id/activity_date_addtask_tip_layout').click()
        # 选择“提前一周”
        driver.find_elements_by_id('com.tal.kaoyan:id/tvTitle')[8].click()
        # 单击确定
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
        sleep(3)
        # 截图
        PrtSc(self, "验证任务能否设置提前一周提醒")

    def test_mytask007(self):
        # 点击 添加学习任务
        driver = self.driver
        driver.find_element_by_id('com.tal.kaoyan:id/ivAddTask').click()
        # 添加做英语阅读任务
        driver.find_element_by_id('com.tal.kaoyan:id/btnHot4').click()
        # 单击结束重复时间页面的确定
        driver.find_element_by_id('com.tal.kaoyan:id/activity_date_addtask_selectdate_commitbtn').click()
        # 点击“全天”button
        driver.find_element_by_id('com.tal.kaoyan:id/activity_date_addtask_allday_switch').click()
        # 单击“提醒”
        driver.find_element_by_id('com.tal.kaoyan:id/activity_date_addtask_tip_layout').click()
        # 选择“提前一周”
        driver.find_elements_by_id('com.tal.kaoyan:id/tvTitle')[8].click()
        # 单击确定
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
        sleep(3)
        # 截图
        PrtSc(self, "验证设置全天任务能否提前一周提醒")

    def test_mytask008(self):
        driver = self.driver
        # 单击任务列表第一个任务
        driver.find_elements_by_id('com.tal.kaoyan:id/home_task_title')[0].click()
        # 在打开的页面单击“删除”
        driver.find_element_by_id('com.tal.kaoyan:id/ivDelete').click()
        # 点击删除整个任务
        driver.find_element_by_id('com.tal.kaoyan:id/btnDeleteAllTask').click()
        sleep(3)
        # 截图
        PrtSc(self, "验证能否删除已完成任务")

    def test_mytask009(self):
        driver = self.driver
        # 单击任务列表中已完成的任务
        driver.find_elements_by_id('com.tal.kaoyan:id/home_task_title')[3].click()
        # 在打开的页面单击“删除”
        driver.find_element_by_id('com.tal.kaoyan:id/ivDelete').click()
        sleep(3)
        # 截图
        PrtSc(self, "验证能否删除未完成任务")

    def test_mytask010(self):
        # 点击论坛
        self.driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum').click()
        sleep(2)
        # 屏幕向上滑动
        for i in range(5):
            TouchAction(self.driver).press(x=379, y=1043).move_to(x=0, y=-1000).perform()
            sleep(1)
        # 截图
        PrtSc(self, "验证能否刷新论坛信息")


if __name__ == '__main__':
    unittest.main()
