# 脚本步骤：
# ①导包
# ②实例化webdriver，打开浏览器
# ③打开被测URL
# ④定位、操作元素
# ⑤暂停、退出浏览器

# 导入selenium webdriver
# from selenium import webdriver
# from time import sleep
# # 实例化浏览器，打开浏览器
# diver = webdriver.Chrome()
# 打开URL地址
# diver.get("http://www.baidu.com")
# #定位、操作元素
# #百度搜索中秋节
# keyword_element = diver.find_element_by_id("kw")
# keyword_element.send_keys("中秋节")
# diver.find_element_by_id("su").click()
# sleep(3)
# diver.close()

# diver = webdriver.Chrome()
# diver.get("http://www.baidu.com")
# diver.find_element_by_id("kw").send_keys("襄阳")
# diver.find_element_by_id("su").click()
# sleep(5)
# diver.close()

from selenium import webdriver
from time import sleep
diver = webdriver.Chrome()
diver.get("https://www.offcn.com")
sleep(1)
diver.find_element_by_link_text("了解中公").click()

sleep(1)
diver.quit()
#
# # diver.get(r"C:\Users\Administrator\Desktop\web_item\注册界面\注册A.html")
# # # xpath元素属性与层级结合
# # diver.find_element_by_xpath("//p[@id='p1']/input").send_keys("李张格")
# # diver.find_element_by_id("passwordA").send_keys("lizhangge")
# # # xpath元素属性与逻辑结合定位
# # diver.find_element_by_xpath("//*[@name='telA' and @id='telA']").send_keys("18502792331")
# # # xpath元素属性定位
# # diver.find_element_by_xpath("//input[@placeholder='电子邮箱A']").send_keys("1915768931@qq.com")
# # # xpath绝对路径定位
# # diver.find_element_by_xpath("/html/body/form/div/fieldset/button").click()
# # # xpath相对路径定位
# # diver.find_element_by_xpath("//p[6]/a").click()
#
#
#
# sleep(5)
# diver.quit()


