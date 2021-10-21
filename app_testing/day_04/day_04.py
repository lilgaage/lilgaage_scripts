# 导包
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from app_testing.Func.KYB_Func import *
from time import sleep

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
# 实例化webdriver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# 隐式等待
driver.implicitly_wait(30)

# # 取消升级
# driver.find_element_by_id('android:id/button2').click()
# sleep(2)
# # 引导页向左滑动
# size = driver.get_window_size()
# print(size, type(size))  # {'width': 720, 'height': 1280} <class 'dict'>
# x = size['width']
# y = size['height']
# for i in range(3):
#     driver.swipe(x*0.8, y*0.5, x*0.2, y*0.5, 1000)
#     sleep(1)


# # 判断【我】按钮是否存在
# try:
#     myself = driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
# except NoSuchElementException:
#     print("首次登录")
# else:
#     print("非首次登录")
#     # 点击【我】
#     myself.click()
#     # 点击【头像】
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_userheader').click()
# finally:
#     # 取消升级
#     driver.find_element_by_id('android:id/button2').click()
#     # 跳过引导页
#     driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
#     sleep(2)
#     # 登录
#     driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys("lilghost213")
#     driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys("lilghost123")
#     sleep(2)
#     # 点击登录按钮
#     driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
#     sleep(2)


# # 键盘操作
# # 取消升级
# driver.find_element_by_id('android:id/button2').click()
# # 跳过引导页
# driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
# sleep(2)
# # 登录
# username = driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext')
# print("账号文本框text属性值是：", username.text)
# username.send_keys("lilghost213")
# print("账号文本框text属性值是：", username.get_attribute("text"))
# print("账号文本框class属性值是：", username.get_attribute("className"))
# pwd = driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext')
# pwd.send_keys("lilghost123")
# print("密码框id属性值是：", username.get_attribute("resourceId"))
#
# sleep(2)
# # tab键切换
# driver.press_keycode(61)
# # 点击登录按钮-----》回车键
# driver.press_keycode(66)
# sleep(2)
# now = time.strftime("%Y%m%d_%H%M%S")
# driver.get_screenshot_as_file("../images/img_发送按键登录成功_{}.png".format(now))


# 退出会话


# 关闭当前APP
# driver.close_app()
# # 判断考研帮APP是否已安装
# print("考研帮APP是否已安装", driver.is_app_installed('com.tal.kaoyan'))
# # 卸载考研帮
# driver.remove_app('com.tal.kaoyan')
# sleep(1)
# # 判断考研帮APP是否已安装
# print("考研帮APP是否已安装", driver.is_app_installed('com.tal.kaoyan'))
# # 安装移动自习室app
# driver.install_app(r'C:\Users\Administrator\Desktop\App\App\yidongzixishi_4.6.1.apk')
# sleep(1)
# # 启动移动自习室
# driver.start_activity('com.offcn.yidongzixishi', 'com.offcn.yidongzixishi.SplashActivity')



# 取消升级
driver.find_element_by_id('android:id/button2').click()
# 跳过引导页
driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
sleep(2)
# 登录
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys("lilghost213")
driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys("lilghost123")
# 点击【我知道了】
TouchAction(driver).tap(x=398, y=512).perform()
sleep(2)
# 长按在【论坛】
luntan = driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum')
TouchAction(driver).long_press(luntan, duration=3000).release().perform()
sleep(2)
# 屏幕向上滑动
TouchAction(driver).press(x=379, y=1043).move_to(x=0, y=-60).perform()


sleep(5)
driver.quit()

