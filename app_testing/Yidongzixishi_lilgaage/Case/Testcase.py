from appium import webdriver
from time import sleep,strftime
import unittest
class case(unittest.TestCase):
    def setUp(self) -> None:
        #配置文件
        caps = {
            # 操作系统
            "platformName": "Android",
            "platformVersion": "4.4.2",
            # 设备id
            "deviceName": "127.0.0.1:62001",
            # app
            "appPackage": "com.offcn.yidongzixishi",
            "appActivity": "com.offcn.yidongzixishi.SplashActivity",
            # 是否重置App的状态---> 不重置
            "noReset": True,
            # 输入法守护
            "resetKeyboard": True,
            "unicodeKeyboard": True
        }
        #实例化对象
        self.driver = webdriver.Remote('127.0.0.1:4723/wd/hub',caps)
        self.driver.implicitly_wait(10)

    def test_001(self):
        '''
        验证设置是否能进入修改密码模块
        '''
        #点击设置
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/mineSettting').click()
        #点击修改密码
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rlModifyPwd').click()
        #断言是否进入修改密码页面
        try:
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/headTitle').text
            exp = '修改密码'
            self.assertEqual(act,exp)
        #若不是进入修改密码页面则截图
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/pad{}.png'.format(new_time))
            raise

    def test_002(self):
        '''
        验证意见反馈，预留信息填写手机号
        '''
        #点击设置
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/mineSettting').click()
        #点击意见反馈
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_feed_back').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/feedContent').send_keys('这是一个意见反馈')
        driver.find_element_by_id('com.offcn.yidongzixishi:id/contactContent').send_keys('17521727122')
        driver.find_element_by_id('com.offcn.yidongzixishi:id/sbumitContent').click()
        #提交是否成功
        try:
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/headTitle').text
            exp = '设置'
            self.assertEqual(act,exp)
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/意见反馈{}.png'.format(new_time))
            raise

    def test_003(self):
        '''
        验证意见反馈预留信息写汉字
        '''
        #点击设置
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/mineSettting').click()
        #点击意见反馈
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_feed_back').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/feedContent').send_keys('这是一个意见反馈')
        driver.find_element_by_id('com.offcn.yidongzixishi:id/contactContent').send_keys('张三')
        driver.find_element_by_id('com.offcn.yidongzixishi:id/sbumitContent').click()
        # 提交是否成功
        try:
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/headTitle').text
            exp = '意见反馈'
            self.assertEqual(act, exp)
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/意见反馈{}.png'.format(new_time))
            raise

    def test_004(self):
        '''
        验证点击移动自习室官网链接跳转页面是否正确
        '''
        #点击设置
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/mineSettting').click()
        #点击关于
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_about').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/tv_net_url').click()
        #获取跳转页面标题进行断言
        try:
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_all').text
            exp = '移动自习室'
            self.assertIn(exp,act)
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/移动自习室官网{}.png'.format(new_time))
            raise

    def test_005(self):
        '''
        验证点击微课查看微课功能
        '''
        #取消升级
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        #点击我的微课
        driver.find_element_by_id('com.offcn.yidongzixishi:id/mineGridViewImg').click()
        #断言进入页面是否正确
        try:
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/headTitle').text
            exp = '我的微课'
            self.assertEqual(act,exp)
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/我的微课{}.png'.format(new_time))
            raise

    def test_006(self):
        '''
        验证查看私信功能
        '''
        #取消升级
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        #点击右上角私信图标
        driver.find_element_by_id('com.offcn.yidongzixishi:id/mineMessage').click()
        try:
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/headTitle').text
            exp = '私信'
            self.assertEqual(act,exp)
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/我的私信{}.png'.format(new_time))
            raise

    def test_007(self):
        '''
        验证查看学员专享功能
        '''
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        #点击学员专享
        driver.find_elements_by_id('com.offcn.yidongzixishi:id/mineGridViewTitle')[1].click()
        try:
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/headTitle').text
            exp = '学员专享'
            self.assertEqual(act,exp)
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/学员专享{}.png'.format(new_time))
            raise

    def test_008(self):
        '''
        验证查看直播课堂功能
        '''
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        #点击直播课堂
        driver.find_elements_by_id('com.offcn.yidongzixishi:id/mineGridViewTitle')[2].click()
        try:
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/headTitle').text
            exp = '直播课堂'
            self.assertEqual(act,exp)
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/直播课堂{}.png'.format(new_time))
            raise
    def test_009(self):
        '''
        验证查看考研课程功能
        '''
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        #点击考研课程
        driver.find_elements_by_id('com.offcn.yidongzixishi:id/mineGridViewTitle')[3].click()
        try:
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/headTitle').text
            exp = '考研课程'
            self.assertEqual(act,exp)
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/考研课程{}.png'.format(new_time))
            raise

    def test_010(self):
        '''
        验证查看练习记录功能
        '''
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        #点击练习记录
        driver.find_elements_by_id('com.offcn.yidongzixishi:id/mineGridViewTitle')[4].click()
        try:
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/headTitle').text
            exp = '练习记录'
            self.assertEqual(act,exp)
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/练习记录{}.png'.format(new_time))
            raise

    def test_011(self):
        '''
        验证查看试题收藏功能
        '''
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        #点击试题收藏
        driver.find_elements_by_id('com.offcn.yidongzixishi:id/mineGridViewTitle')[5].click()
        try:
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/headTitle').text
            exp = '试题收藏'
            self.assertEqual(act,exp)
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/试题收藏{}.png'.format(new_time))
            raise

    def test_012(self):
        '''
        验证查看课程收藏功能
        '''
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        #点击课程收藏
        driver.find_elements_by_id('com.offcn.yidongzixishi:id/mineGridViewTitle')[6].click()
        try:
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/headTitle').text
            exp = '课程收藏'
            self.assertEqual(act,exp)
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/课程收藏{}.png'.format(new_time))
            raise

    def test_013(self):
        '''
        验证查看我的订单已支付订单
        '''
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        #点击已支付订单
        driver.find_elements_by_id('com.offcn.yidongzixishi:id/mineGridViewTitle')[7].click()
        driver.find_elements_by_id('com.offcn.yidongzixishi:id/tv_title')[1].click()
        try:
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/tv_confirm_or_cancel').text
            exp = '已支付'
            self.assertEqual(act,exp)
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/已支付订单{}.png'.format(new_time))
            raise

    def test_014(self):
        '''
        验证查看已取消订单详情
        '''
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        #点击已取消订单
        driver.find_elements_by_id('com.offcn.yidongzixishi:id/mineGridViewTitle')[7].click()
        driver.find_elements_by_id('com.offcn.yidongzixishi:id/tv_title')[2].click()
        #进入详情页
        driver.find_element_by_id('com.offcn.yidongzixishi:id/tv_dingdan').click()
        try:
            #获取页面标题断言
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/headTitle').text
            exp = '订单详情'
            self.assertEqual(act,exp)
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/订单详情{}.png'.format(new_time))
            raise
    def test_015(self):
        '''
        验证绑定优惠券功能
        '''
        driver = self.driver
        driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
        #点击优惠券
        driver.find_elements_by_id('com.offcn.yidongzixishi:id/mineGridViewTitle')[8].click()
        driver.find_element_by_id('com.offcn.yidongzixishi:id/btn_bind_coupon').click()
        try:
            #获取页面标题断言
            act = driver.find_element_by_id('com.offcn.yidongzixishi:id/headTitle').text
            exp = '绑定优惠券'
            self.assertEqual(act,exp)
        except:
            new_time = strftime("%Y%m%d_%H%M%S")
            driver.get_screenshot_as_file('../image/订单详情{}.png'.format(new_time))
            raise



    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
