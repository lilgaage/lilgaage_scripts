from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r"C:\Users\Administrator\Desktop\web_item\注册界面\注册实例.html")
driver.find_element_by_id('user').send_keys("李张格")
sleep(2)
# 切换到注册A页面
driver.switch_to.frame('idframe1')
driver.find_element_by_id('userA').send_keys("小瑰")
sleep(2)
# 切换到默认页面
driver.switch_to.default_content()
sleep(2)
# 切换到注册B页面
driver.switch_to.frame('myframe2')
driver.find_element_by_id('userB').send_keys("瑰丝")
sleep(2)
driver.switch_to.default_content()
sleep(2)
driver.find_element_by_link_text('淘宝').click()

sleep(3)
driver.quit()

