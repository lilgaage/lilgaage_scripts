import time

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")
sleep(2)
# 截图保存在目录
driver.get_screenshot_as_file("images/img01_百度首页.png")
# 获取当前时间
now_time = time.strftime("%Y%m%d_%H%M%S")
driver.find_element_by_id('kw').send_keys("李张格")
driver.find_element_by_id('su').click()
sleep(3)
driver.get_screenshot_as_file("images/img_{}_李张格首页.png".format(now_time))
driver.find_element_by_link_text('免费学无人机,武汉一高校社团开“飞手”培训课被“秒光”-...').click()
# 切换窗口
driver.switch_to.window(driver.window_handles[1])
sleep(3)
driver.get_screenshot_as_file("images/img_{}_无人机新闻.png".format(now_time))
driver.find_element_by_link_text('首页').click()
driver.get_screenshot_as_file("images/img_{}_站长头条首页.png".format(now_time))



sleep(3)
driver.quit()
