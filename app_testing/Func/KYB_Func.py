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
            "appPackage": "com.tal.kaoyan",
            "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
             # 是否重置APP的状态  ---- 重置
            "noReset": False,
            # 输入法守护
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }


# 取消更新、跳过开场页面方法
def cancel_skip(self):
    # 取消升级
    self.driver.find_element_by_id('android:id/button2').click()
    # 跳过引导页
    self.driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
    sleep(2)


# 登录考研帮方法
def login(self):
    driver = self.driver
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys("lilghost213")
    driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys("lilghost123")
    sleep(2)
    # 点击登录按钮
    driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
    sleep(2)


# 退出考研帮方法
def logout(self):
    driver = self.driver
    # 点击“我”模块
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
    # 点击设置
    driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButtonWraper').click()
    # 点击退出登录
    driver.find_element_by_id('com.tal.kaoyan:id/setting_logout_text').click()
    # 确定退出登录
    driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()


# 截图的方法
def PrtSc(self, title):
    now = time.strftime("%Y%m%d_%H%M%S")
    self.driver.get_screenshot_as_file("../images/img_{}_{}.png".format(title, now))
