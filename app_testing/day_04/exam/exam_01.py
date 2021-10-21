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
            "appPackage": "com.tencent.mobileqq",
            "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
             # 是否重置APP的状态  ---- 重置
            "noReset": False,
            # 输入法守护
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }
# 实例化webdriver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# 隐式等待
driver.implicitly_wait(30)
# 点击登录按钮
driver.find_element_by_id('com.tencent.mobileqq:id/btn_login').click()
# 输入账号
driver.find_element_by_class_name('android.widget.EditText').send_keys("1915768931")
# 输入密码
driver.find_element_by_id('com.tencent.mobileqq:id/password').send_keys("123321123321")
# 点击登录按钮
driver.find_element_by_id('com.tencent.mobileqq:id/login').click()
# 截图
sleep(1)
now = time.strftime("%Y%m%d_%H%M%S")
driver.get_screenshot_as_file("../images/img_登录QQ_{}.png".format(now))

sleep(2)
driver.quit()
