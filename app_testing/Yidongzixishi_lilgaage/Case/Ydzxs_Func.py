from appium import webdriver
from time import sleep
import time

# 配置capability信息
desired_caps = \
        {
            # 操作系统
            "platformName": "Android",
            "platformVersion": "4.4.2",
            # 设备
             "deviceName": "127.0.0.1:62001",
            # APP
            "appPackage": "com.offcn.yidongzixishi",
            "appActivity": "com.offcn.yidongzixishi.SplashActivity",
             # 是否重置APP的状态  ---- 重置
            "noReset": False,
            # 输入法守护
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }


# 选择国家公务员、取消升级的方法
def select_cancel(self):
    # 选择国家公务员
    self.driver.find_element_by_id('com.offcn.yidongzixishi:id/tv_subject_name').click()
    # 取消升级
    self.driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()

# 登录移动自习室的方法
def login(self):
    # 清空账号框
    self.driver.find_element_by_id('com.offcn.yidongzixishi:id/et_phone').clear()
    # 输入账号
    self.driver.find_element_by_id('com.offcn.yidongzixishi:id/et_phone').send_keys("18502792331")
    # 输入密码
    self.driver.find_element_by_id('com.offcn.yidongzixishi:id/et_pwd').send_keys("18502792331")
    # 点击 立即登录
    self.driver.find_element_by_id('com.offcn.yidongzixishi:id/btn_login').click()

# 退出登录的方法
def logout(self):
    # 点击【我】
    self.driver.find_element_by_id('com.offcn.yidongzixishi:id/iv_mine').click()
    # 点击头像
    self.driver.find_element_by_id('com.offcn.yidongzixishi:id/iv_user').click()
    # 点击 退出登录
    self.driver.find_element_by_id('com.offcn.yidongzixishi:id/loginOut').click()

# 截图的方法
def PrtSc(self, title):
    now = time.strftime("%Y%m%d_%H%M%S")
    self.driver.get_screenshot_as_file("../images/img_{}_{}.png".format(title, now))
