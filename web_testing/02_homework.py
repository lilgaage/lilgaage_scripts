from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

# 4.实现需求：打开中公官网www.offcn.com，并点击【了解中公】
driver.get("https://www.offcn.com")
sleep(1)
driver.find_element_by_link_text("了解中公").click()

sleep(5)
driver.quit()
'''
#3.在注册B.html中输入注册信息，然后使用get_attribute()获取用户输入的数据并打印
driver.get(r"C:\Users\Administrator\Desktop\web_item\注册界面\注册B.html")
driver.find_element_by_id('userB').send_keys("李张格")
driver.find_element_by_id('passwordB').send_keys("lizhangge")
driver.find_element_by_id('telB').send_keys("18502792331")
driver.find_element_by_id('emailB').send_keys("1915768931@qq.com")
username = driver.find_element_by_id("userB").get_attribute("value")
passwd = driver.find_element_by_id('passwordB').get_attribute('value')
telphone = driver.find_element_by_id('telB').get_attribute('value')
email = driver.find_element_by_id('emailB').get_attribute('value')
print("用户输入信息有：",username,passwd,telphone,email,sep="\n")

sleep(1)
driver.quit()
'''
