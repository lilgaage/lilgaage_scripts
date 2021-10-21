# 导包
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
# 实例化webdriver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# 隐式等待
driver.implicitly_wait(30)
# 截图
now = time.strftime("%Y%m%d_%H%M%S")
driver.get_screenshot_as_file("images/img_打开考研帮_{}.png".format(now))

'''
# id定位实现登录-退出
# # 取消升级
# driver.find_element_by_id('android:id/button2').click()
# # 跳过引导页
# driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
# sleep(2)
# # 输入账号密码
# driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys("lilghost213")
# driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys("lilghost123")
# sleep(2)
# # 点击登录按钮
# driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
# # 点击“我”模块
# driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
# # 点击设置
# driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButtonWraper').click()
# # 点击退出登录
# driver.find_element_by_id('com.tal.kaoyan:id/setting_logout_text').click()
# # 确定退出登录
# driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()

# # 相对元素定位
# # 点击注册按钮
# driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
# # 注册添加头像
# father = driver.find_element_by_id('com.tal.kaoyan:id/activity_register_parentlayout')
# father.find_element_by_class_name('android.widget.ImageView').click()

# xpath定位
# 取消升级---绝对路径
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/'
                             'android.widget.FrameLayout/'
                             'android.widget.FrameLayout/'
                             'android.widget.LinearLayout/'
                             'android.widget.LinearLayout[3]/'
                             'android.widget.LinearLayout/'
                             'android.widget.Button[1]').click()
# 跳过引导页
driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
sleep(2)
# # 清空账号输入框----相对路径
# driver.find_element_by_xpath('//android.widget.EditText').clear()
# # 输入账号----元素属性定位
# driver.find_element_by_xpath('//*[@text="请输入用户名"]').send_keys("lilghost213")
# # 输入密码----属性与逻辑结合
# driver.find_element_by_xpath('//*[@class="android.widget.EditText" and @index="3"]')\
#     .send_keys("lilghost123")
sleep(2)
# 点击注册按钮
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
# 点击添加头像-----属性与层级结合
driver.find_element_by_xpath('//*[@resource-id="com.tal.kaoyan:id/activity_register_parentlayout"]/'
                             'android.widget.ImageView').click()
# list定位
driver.find_elements_by_id('com.tal.kaoyan:id/item_image')[2].click()
'''
# 课堂练习
'''
1. 进入注册界面，点击头像按钮---->添加头像
2. 输入注册信息，点击【立即注册】
直接成功跳转至院校信息选择界面
提示【客户端版本过低】---->点击【返回】-【试试看】--->院校信息选择界面
3. 完善院校及专业信息完成注册
4. 退出账号

# 取消升级
driver.find_element_by_id('android:id/button2').click()
# 跳过引导页
driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
sleep(2)
# 点击注册按钮
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
# 点击添加头像
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()
# 选择第二个头像
driver.find_elements_by_id('com.tal.kaoyan:id/item_image')[1].click()
# 单击保存
driver.find_element_by_id('com.tal.kaoyan:id/save').click()
# 输入注册信息
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys("gaageghost213")
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys("gaageghost213")
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys("gaageghost213@qq.com")
sleep(2)
# 点击立即注册按钮
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()
# 选择目标院校
driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()
# 点击广东
driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')[13].click()
# 选择中山大学
driver.find_element_by_id('com.tal.kaoyan:id/university_search_item_name').click()
# 选择目标专业
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
# 选择法学
driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')[2].click()
# 点击法学
driver.find_element_by_id('com.tal.kaoyan:id/major_group_title').click()
# 选择法学
driver.find_element_by_id('com.tal.kaoyan:id/major_search_item_name').click()
# 点击进入考研帮
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()
# 点击“我”模块
driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
# 点击设置
driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButtonWraper').click()
# 点击退出登录
driver.find_element_by_id('com.tal.kaoyan:id/setting_logout_text').click()
# 确定退出登录
driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()
'''

# 取消升级
driver.find_element_by_id('android:id/button2').click()
# 跳过引导页
driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
sleep(2)
# 输入账号密码
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys("lilghost213")
driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys("lilghost123")
sleep(2)
# 点击登录按钮
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
sleep(2)
# 点击【我知道了】
driver.tap([(270,461),(371,472)],1000)
sleep(2)
# 屏幕向上滑动
driver.swipe(380,1080,380,168,1000)
sleep(2)
# 点击查看第四条信息
driver.find_elements_by_id('com.tal.kaoyan:id/date_recommend_info_title')[3].click()




# #退出会话
# sleep(5)
# driver.quit()

