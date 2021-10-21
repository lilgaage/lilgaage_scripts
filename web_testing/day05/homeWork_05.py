from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
from time import sleep
import time

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('中公教育')
# driver.find_element_by_id('su').click()
# driver.find_element_by_partial_link_text('公务员考试网').click()
# # 切换窗口
# driver.switch_to.window(driver.window_handles[1])
# action = ActionChains(driver)
# # 定位悬停
# user_service = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/ul/li[6]')
# action.move_to_element(user_service).perform()
# sleep(2)
# # 截图
# now = time.strftime("%Y%m%d_%H%M%S")
# driver.get_screenshot_as_file("images/img_{}_中公教育用户服务.png".format(now))


# driver.get(r'C:\Users\Administrator\Desktop\web_item\注册界面\注册B.html')
# driver.find_element_by_id('userB').send_keys("李张格")
# driver.find_element_by_id('passwordB').send_keys("lizhangge")
# driver.find_element_by_id('telB').send_keys("18502792331")
# driver.find_element_by_id('emailB').send_keys("191576893@qq.com")
# # 定位下拉框
# citys = driver.find_element_by_id('selectB')
# c1 = Select(citys)
# c1.select_by_index(0)
# sleep(1)
# c1.select_by_value('sh')
# sleep(1)
# c1.select_by_visible_text('广州B')
# sleep(1)
# c1.select_by_index(3)
# sleep(1)
# c1.select_by_index(4)
# sleep(1)
# c1.select_by_index(5)
action = ActionChains(driver)
more = driver.find_element_by_link_text("更多")
action.move_to_element(more).perform()
driver.find_element_by_link_text("图片").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_id('kw').send_keys("国庆")
driver.find_element_by_class_name('s_newBtn').click()
now = time.strftime("%Y%m%d_%H%M%S")
driver.get_screenshot_as_file('images/img_{}_国庆图片.png'.format(now))

sleep(3)
driver.quit()

