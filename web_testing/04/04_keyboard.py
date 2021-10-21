from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r"C:\Users\Administrator\Desktop\web_item\注册界面\注册A.html")
# 账号输入“李张格213”
username = driver.find_element_by_id('userA')
username.send_keys("李张格213")
sleep(1)
# 删除3
username.send_keys(Keys.BACK_SPACE)
sleep(1)
# 删除1
username.send_keys(Keys.BACKSPACE)
sleep(1)
# 删除2
username.send_keys(Keys.BACK_SPACE)
sleep(1)
# 全选用户名
username.send_keys(Keys.CONTROL, 'a')
sleep(1)
# 复制用户名
username.send_keys(Keys.CONTROL, 'c')
sleep(1)
# 粘贴到密码框
passwd = driver.find_element_by_id('passwordA')
passwd.send_keys(Keys.CONTROL, 'v')
sleep(1)
# 切换到下一个框
passwd.send_keys(Keys.TAB)
sleep(1)
# 在手机号输入框点击回车
driver.find_element_by_id('telA').send_keys(Keys.ENTER)

sleep(3)
driver.quit()




