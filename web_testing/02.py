from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# #name属性值定位
# driver.find_element_by_name("wd").send_keys("李张格")
# #class属性值定位
# driver.find_element_by_class_name("s_btn").click()
# #标签名定位
# # driver.find_element_by_tag_name("button").click()
# #网页加载需要时间
# sleep(3)
# #超链接文本定位元素
# driver.find_element_by_link_text("免费学无人机,武汉一高校社团开“飞手”培训课被“秒光”-...").click()
# #超链接部分文本定位元素
# # driver.find_element_by_partial_link_text("免费学无人机").click()


diver = webdriver.Chrome()
diver.get(r"C:\Users\Administrator\Desktop\web_item\注册界面\注册A.html")

#浏览器操作
sleep(1)
# # 自定义浏览器大小
# diver.set_window_size(500,300)
# sleep(1)
# # 自定义浏览器位置
# diver.set_window_position(300,300)
# sleep(1)
# # 最大化
# diver.maximize_window()
# sleep(1)
# # 打开百度
# diver.find_element_by_partial_link_text("百度").click()
# sleep(1)
# # 输入搜索内容，然后刷新
# diver.find_element_by_id("kw").send_keys("李张格")
# sleep(1)
# diver.refresh()
# sleep(1)
# # 回退
# diver.back()
# sleep(1)
# # 前进
# diver.forward()
# sleep(1)
# # 点击打开新闻
# diver.find_element_by_link_text("新闻").click()


user_size = diver.find_element_by_id("userA").size
print("账号文本框大小为：",user_size)
print("当前网页标题是：",diver.title)
print("当前网页网址是：",diver.current_url)
print("第一个超链接文本时：",diver.find_element_by_tag_name("a").text)
diver.find_element_by_id("userA").send_keys("李张格")
print("用户输入的手机号是：",diver.find_element_by_id("userA").get_attribute("value"))
print("span标签是否可见：",diver.find_element_by_tag_name("span").is_displayed())
print("取消按钮是否可用：",diver.find_element_by_id("cancelA").is_enabled())
'''
账号文本框大小为： {'height': 29, 'width': 183}
当前网页标题是： 注册A
当前网页网址是： file:///C:/Users/Administrator/Desktop/web_item/%E6%B3%A8%E5%86%8C%E7%95%8C%E9%9D%A2/%E6%B3%A8%E5%86%8CA.html
第一个超链接文本时： A访问 新浪 网站
用户输入的手机号是： 李张格
span标签是否可见： False
取消按钮是否可用： False
'''



# # xpath元素属性与层级结合定位
# diver.find_element_by_xpath("//p[@id='p1']/input").send_keys("李张格")
# diver.find_element_by_xpath('//*[@id="passwordA"]').send_keys("lizhangge")
# # xpath元素属性与逻辑结合定位
# diver.find_element_by_xpath("//*[@name='telA' and @id='telA']").send_keys("18502792331")
# # xpath元素属性定位
# diver.find_element_by_xpath("//input[@placeholder='电子邮箱A']").send_keys("1915768931@qq.com")
# diver.find_element_by_xpath('//*[@id="selectA"]/option[4]').click()
# diver.find_element_by_xpath('//*[@id="xja"]').click()
# sleep(5)
# # xpath绝对路径定位
# diver.find_element_by_xpath("/html/body/form/div/fieldset/button").click()
# # # xpath相对路径定位
# # diver.find_element_by_xpath("//p[6]/a").click()

# # css选择器定位
# # 层级选择器
# diver.find_element_by_css_selector("#p1>input").send_keys("李张格")
# # 属性选择器
# diver.find_element_by_css_selector('[type="password"]').send_keys("lizhangge")
# # class选择器
# diver.find_element_by_css_selector('.telA').send_keys("18502792331")
# # id选择器
# diver.find_element_by_css_selector('#emailA').send_keys("1915768931@qq.com")
# # 元素选择器
# diver.find_element_by_css_selector('button').click()
# diver.find_element_by_css_selector('[value="cq"]').click()
# diver.find_element_by_css_selector('[value="jza"]').click()

# # list定位
# diver.find_elements_by_tag_name("input")[0].send_keys("李张格")
# diver.find_elements_by_tag_name("input")[1].send_keys("lzg")
# diver.find_elements_by_css_selector('#telA')[0].send_keys("127362128932")
# diver.find_elements_by_xpath('//input')[3].send_keys("123231@163.com")
# diver.find_elements_by_xpath("//button")[0].click()

# # By类定位
# diver.find_element(By.ID, 'userA').send_keys("小瑰")
# diver.find_element(By.CSS_SELECTOR, '#passwordA').send_keys("ghost")
# diver.find_element(By.CLASS_NAME, "telA").send_keys("12346432234")
# diver.find_element(By.XPATH, '//*[@id="emailA"]').send_keys("1234@162.com")
# sleep(3)
# diver.find_element(By.TAG_NAME, 'button').click()

# # xpath css扩展
# # start-with:属性值的开头
# diver.find_element_by_xpath('//input[starts-with(@id,"use")]').send_keys("瑰丝")
# # contains：属性值的某一部分
# diver.find_element_by_xpath('//*[contains(@type,"pass")]').send_keys("guisi")
# sleep(3)
# # $：结尾
# diver.find_element_by_css_selector('[type$="word"]').send_keys("xiaoguixiaosi")
# # ^：开头
# diver.find_element_by_css_selector('[class^="tel"]').send_keys("123456754322")
# # *：包含某一部分
# diver.find_element_by_css_selector('[id*="mail"]').send_keys("12343@qq.com")
# # text()="" 文本等于
# diver.find_element_by_xpath('//*[text()="注册用户A"]').click()
# sleep(3)
# diver.find_element_by_xpath('//a[text()="A百度一下，你就知道"]').click()

# #元素的操作方法 send_keys clear click
# diver.find_element_by_id("userA").send_keys("lilgaage")
# sleep(1)
# diver.find_element_by_xpath('//p[@id="p1"]/input').clear()
# sleep(1)
# diver.find_element_by_css_selector('#userA').send_keys("李张格")
# sleep(1)
# diver.find_element_by_tag_name("button").click()


sleep(5)
diver.quit()
