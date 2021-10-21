from selenium.webdriver.support.select import Select
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r"C:\Users\Administrator\Desktop\web_item\注册界面\注册A.html")
# driver.find_element_by_css_selector('[value="sh"]').click()
# sleep(2)
# driver.find_elements_by_tag_name('option')[4].click()
# sleep(2)
# driver.find_element_by_css_selector('#selectA > option:nth-child(3)').click()

# select类定位下拉列表
# 导包 from selenium.webdriver.support.select import Select
# 先定位下拉框
citys = driver.find_element_by_id('selectA')
# 实例化select类
s1 = Select(citys)
# 索引
s1.select_by_index(1)
sleep(1)
# 值
s1.select_by_value('sz')
sleep(1)
# 可视化文本
s1.select_by_visible_text('A广州')

sleep(3)
driver.quit()