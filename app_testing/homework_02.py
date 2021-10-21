# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "4.4.2"
caps["deviceName"] = "127.0.0.1:62001"
caps["noReset"] = False
caps["appPackage"] = "com.tal.kaoyan"
caps["appActivity"] = "com.tal.kaoyan.ui.activity.SplashActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# 取消更新
el1 = driver.find_element_by_id("android:id/button2")
el1.click()
# 跳过开头动画
TouchAction(driver).tap(x=615, y=56).perform()
# 点击“注册”按钮
el2 = driver.find_element_by_id("com.tal.kaoyan:id/login_register_text")
el2.click()
# 输入用户名
el3 = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_username_edittext")
el3.send_keys("lilghost213")
# 输入密码
el4 = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_password_edittext")
el4.send_keys("lilghost123")
# 输入邮箱
el5 = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_email_edittext")
el5.send_keys("lilghost123@qq.com")
# 单击确定注册
el6 = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_register_btn")
el6.click()
# 单击“我”
el7 = driver.find_element_by_id("com.tal.kaoyan:id/myapptitle_leftbutton_image")
el7.click()
# 单击设置
TouchAction(driver).tap(x=678, y=73).perform()
# 单击退出登录
el8 = driver.find_element_by_id("com.tal.kaoyan:id/setting_logout_text")
el8.click()
# 单击确定退出登录
el9 = driver.find_element_by_id("com.tal.kaoyan:id/tip_commit")
el9.click()


driver.quit()

