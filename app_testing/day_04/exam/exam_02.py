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
            "appPackage": "com.baidu.BaiduMap",
            "appActivity": "com.baidu.baidumaps.WelcomeScreen",
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
# 点击搜索框
driver.find_element_by_id('com.baidu.BaiduMap:id/to').click()
# 搜索中公教育
driver.find_element_by_id('com.baidu.BaiduMap:id/c6a').send_keys("中公教育")
# 点击搜索
driver.find_element_by_id('com.baidu.BaiduMap:id/c68').click()
# 截图
sleep(1)
now = time.strftime("%Y%m%d_%H%M%S")
driver.get_screenshot_as_file("../images/img_百度地图搜索中公教育_{}.png".format(now))

sleep(2)
driver.quit()
