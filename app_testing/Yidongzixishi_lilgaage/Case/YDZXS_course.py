from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from time import sleep
from Ydzxs_Func import *
import unittest


class Case01(unittest.TestCase):
    def setUp(self) -> None:
        # 实例化webdriver
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        # 隐式等待
        self.driver.implicitly_wait(30)
        # 跳过开头
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/skip').click()
        # 登录
        login(self)
        # 选择公务员、取消升级
        select_cancel(self)
        # 点击【课程】
        self.driver .find_element_by_id('com.offcn.yidongzixishi:id/iv_coach').click()


    def tearDown(self) -> None:
        # 退出登录
        logout(self)
        # 暂停、退出会话
        sleep(3)
        self.driver.quit()

    def test_course_001(self):
        try:
            # 预期结果
            Expected = "【国考】上岸刷刷刷"
            sleep(3)
            # 获取文本
            Actual = self.driver.find_element_by_id('com.offcn.yidongzixishi:id/courseTitle').text
            self.assertEqual(Expected, Actual)
            # 截图
            sleep(1)
            PrtSc(self, '课程列表成功加载')
        except AssertionError:
            # 截图
            sleep(1)
            PrtSc(self, '课程列表未被加载')
            raise

    def test_course_002(self):
        # 点击排序下拉列表
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/tvSort').click()
        # 点击综合排序
        self.driver.find_elements_by_id('com.offcn.yidongzixishi:id/textName')[0].click()
        sleep(1)
        PrtSc(self, '课程列表综合排序结果')

    def test_course_003(self):
        # 点击排序下拉列表
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/tvSort').click()
        # 点击综合排序
        self.driver.find_elements_by_id('com.offcn.yidongzixishi:id/textName')[1].click()
        sleep(1)
        PrtSc(self, '课程列表人气排序结果')

    def test_course_004(self):
        # 点击排序下拉列表
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/tvSort').click()
        # 点击综合排序
        self.driver.find_elements_by_id('com.offcn.yidongzixishi:id/textName')[2].click()
        sleep(1)
        PrtSc(self, '课程列表价格正序排序结果')

    def test_course_005(self):
        # 点击排序下拉列表
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/tvSort').click()
        # 点击综合排序
        self.driver.find_elements_by_id('com.offcn.yidongzixishi:id/textName')[3].click()
        sleep(1)
        PrtSc(self, '课程列表价格倒序排序结果')

    def test_course_006(self):
        # 点击排序下拉列表
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/tvSort').click()
        # 点击综合排序
        self.driver.find_elements_by_id('com.offcn.yidongzixishi:id/textName')[4].click()
        sleep(1)
        PrtSc(self, '课程列表最新排序结果')

    def test_course_007(self):
        # 点击【放大镜】图标
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/iv_coach_search').click()
        # 输入【公务员】
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/et_search_course_title').send_keys("公务员")
        # 回车
        self.driver.press_keycode(66)
        try:
            # 预期结果
            Expected = "公务员联考申论模拟（4套）+视频讲解"
            sleep(3)
            # 获取文本
            Actual = self.driver.find_element_by_id('com.offcn.yidongzixishi:id/courseTitle').text
            self.assertEqual(Expected, Actual)
            # 截图
            sleep(1)
            PrtSc(self, '搜索公务员结果页面')
        except AssertionError:
            # 截图
            sleep(1)
            PrtSc(self, '非搜索公务员结果页面')
            raise

    def test_course_008(self):
        # 点击【放大镜】图标
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/iv_coach_search').click()
        # 输入【公务员】
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/et_search_course_title').send_keys("公务员")
        # 点击【取消】
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/tv_search_course_cancel').click()
        try:
            # 预期结果
            Expected = "【国考】上岸刷刷刷"
            sleep(3)
            # 获取文本
            Actual = self.driver.find_element_by_id('com.offcn.yidongzixishi:id/courseTitle').text
            self.assertEqual(Expected, Actual)
            # 截图
            sleep(1)
            PrtSc(self, '取消搜索后返回到课程列表')
        except AssertionError:
            # 截图
            sleep(1)
            PrtSc(self, '取消搜索后未能返回到课程列表')
            raise

    def test_course_009(self):
        # 点击【放大镜】图标
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/iv_coach_search').click()
        # 输入【公务员】
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/et_search_course_title').send_keys("公务员")
        # 回车
        self.driver.press_keycode(66)
        # 点击【取消】
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/tv_search_course_cancel').click()
        # 再次点击【放大镜】图标
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/iv_coach_search').click()
        # 点击【搜索历史】中的【公务员】
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/tv_search_course_item_content').click()
        try:
            # 预期结果
            Expected = "公务员联考申论模拟（4套）+视频讲解"
            sleep(3)
            # 获取文本
            Actual = self.driver.find_element_by_id('com.offcn.yidongzixishi:id/courseTitle').text
            self.assertEqual(Expected, Actual)
            # 截图
            sleep(1)
            PrtSc(self, '搜索公务员结果页面')
        except AssertionError:
            # 截图
            sleep(1)
            PrtSc(self, '非搜索公务员结果页面')
            raise

    def test_course_010(self):
        # 屏幕向上滑动
        TouchAction(self.driver).press(x=379, y=1043).move_to(x=0, y=-60).perform()

    def test_course_011(self):
        try:
            # 预期结果
            Expected = "￥0"
            sleep(3)
            # 获取文本
            Actual = self.driver.find_element_by_id('com.offcn.yidongzixishi:id/coursePrice').text
            self.assertEqual(Expected, Actual)
            # 截图
            sleep(1)
            PrtSc(self, '课程列表会显示课程价格')
        except AssertionError:
            # 截图
            sleep(1)
            PrtSc(self, '课程列表未显示课程价格')
            raise

    def test_course_012(self):
        try:
            # 预期结果
            Expected = "1课时"
            sleep(3)
            # 获取文本
            Actual = self.driver.find_element_by_id('com.offcn.yidongzixishi:id/courseClassHour').text
            self.assertEqual(Expected, Actual)
            # 截图
            sleep(1)
            PrtSc(self, '课程列表会显示课程时长')
        except AssertionError:
            # 截图
            sleep(1)
            PrtSc(self, '课程列表未显示课程时长')
            raise

    def test_course_013(self):
        # 点击第一个课程
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/courseImg').click()
        try:
            # 预期结果
            Expected = "介绍"
            sleep(3)
            # 获取文本
            Actual = self.driver.find_element_by_id('android.widget.TextView').text
            self.assertEqual(Expected, Actual)
            # 截图
            sleep(1)
            PrtSc(self, '可以查看课程详情')
        except AssertionError:
            # 截图
            sleep(1)
            PrtSc(self, '不能查看课程详情')
            raise

    def test_course_014(self):
        # 点击第一个课程
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/courseImg').click()
        # 点击【收藏】图标
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/toolbar_collect').click()

    def test_course_015(self):
        # 点击第一个课程
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/courseImg').click()
        # 点击【分享】图标
        self.driver.find_element_by_id('com.offcn.yidongzixishi:id/toolbar_share').click()
        # 点击分享到新浪微博
        self.driver.find_element_by_name('android.widget.ImageView').click()
        try:
            # 预期结果
            Expected = "图文分享"
            sleep(3)
            # 获取文本
            Actual = self.driver.find_element_by_name('android.widget.TextView').text
            self.assertEqual(Expected, Actual)
            # 截图
            sleep(1)
            PrtSc(self, '弹出分享到新浪微博页面')
        except AssertionError:
            # 截图
            sleep(1)
            PrtSc(self, '未弹出分享到新浪微博页面')
            raise


if __name__ == '__main__':
    unittest.main()
