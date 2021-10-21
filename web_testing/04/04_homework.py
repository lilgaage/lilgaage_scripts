from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
# 3.实现需求：在百度首页点击更多中的音乐，在百度音乐界面搜索《追梦赤子心》
action = ActionChains(driver)
current_handle = driver.current_window_handle
print("百度首页的窗口句柄是：", current_handle, type(current_handle))
more = driver.find_element_by_link_text("更多")
action.move_to_element(more).perform()
driver.find_element_by_link_text("音乐").click()
handles = driver.window_handles
print("所有的窗口句柄是：", handles, type(handles))
driver.switch_to.window(handles[1])
driver.find_element_by_css_selector('[placeholder="请输入歌名、歌词、歌手或专辑"]').send_keys("追梦赤子心")
driver.find_element_by_class_name('el-input__icon').click()

# # 4.实现需求：在百度首页点击【更多】中的【知道】，然后再知道页面搜索“南京”
# action = ActionChains(driver)
# current_handle = driver.current_window_handle
# more = driver.find_element_by_link_text("更多")
# action.move_to_element(more).perform()
# driver.find_element_by_link_text("知道").click()
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# driver.find_element_by_id('kw').send_keys('南京')
# driver.find_element_by_id('search-btn').click()

# # 5.实现需求：百度搜索广州，点击打开广州_百度百科，然后滚动条向下移动1000像素
# current_handle = driver.current_window_handle
# driver.find_element_by_id('kw').send_keys("广州")
# driver.find_element_by_id('su').click()
# driver.find_element_by_partial_link_text('百度百科').click()
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# js = "window.scrollTo(0,1000)"
# driver.execute_script(js)

# # 6.实现需求：百度搜索中公教育，点击打开中公官网，然后鼠标悬停在IT就业
# current_handle = driver.current_window_handle
# driver.find_element_by_id('kw').send_keys("中公教育")
# driver.find_element_by_id('su').click()
# driver.find_element_by_link_text('公务员考试网-2022国考公务员报名/时间/职位-培训-中公教育').click()
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# action = ActionChains(driver)
# more = driver.find_element_by_link_text("IT 就 业")
# action.move_to_element(more).perform()

sleep(3)
driver.quit()
