from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r"C:\Users\Administrator\Desktop\web_item\注册界面\prompt.html")

# 点击prompt按钮，警告框出现
driver.find_element_by_id('prompt').click()
sleep(1)
# 获取警告框
alter = driver.switch_to.alert
# 获取提示框信息
print("对话框信息为：", alter.text)
# 取消按钮
alter.dismiss()
sleep(1)
driver.find_element_by_id('prompt').click()
alter.send_keys('李张格')
# 接收警告
alter.accept()

sleep(1)
driver.quit()






