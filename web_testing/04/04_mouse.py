from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
'''
driver.get("http://www.baidu.com")
# 鼠标悬停
# 需求：在百度首页【更多】中点击音乐
# 实例化鼠标事件类
action = ActionChains(driver)
# 鼠标悬停在【更多】上
more = driver.find_element_by_link_text("更多")
# move_to_element悬停  perform执行（不调用不执行）
action.move_to_element(more).perform()
# 点击音乐
driver.find_element_by_link_text("音乐").click()
'''
'''
# 鼠标拖动
driver.get(r"C:\Administrator\Desktop\web_item\注册界面\拖拽1.html")
action = ActionChains(driver)
# 蓝块 源头
source = driver.find_element_by_id('div')
# 红块 目标
target = driver.find_element_by_id('box')
# 把蓝块拖到红块位置
action.drag_and_drop(source, target).perform()


driver.get(r"C:\Administrator\Desktop\web_item\注册界面\拖拽.html")
action = ActionChains(driver)
blue = driver.find_element_by_id('div')
# 向右移动300px
action.drag_and_drop_by_offset(blue,300,0).perform()
# 向下移动300px
action.drag_and_drop_by_offset(blue,0,300).perform()
'''

driver.get(r"C:\Users\Administrator\Desktop\web_item\测试小站本地版\demo.html")
action = ActionChains(driver)
left = driver.find_element_by_xpath('//*[@id="slider"]/span[1]')
# 获取滑块长度
slider_size = driver.find_element_by_id('slider').size
action.drag_and_drop_by_offset(left, slider_size['width'], 0).perform()

sleep(3)
driver.quit()


