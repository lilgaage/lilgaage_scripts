from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.baidu.com")
action = ActionChains(driver)
# 获取当前的窗口句柄
current_handle = driver.current_window_handle
print("百度首页的窗口句柄是：",current_handle, type(current_handle))
# 在【更多】上悬停鼠标
more = driver.find_element_by_link_text("更多")
action.move_to_element(more).perform()
# 点击音乐
driver.find_element_by_link_text("音乐").click()
# 获取所有窗口句柄
handles = driver.window_handles
print("所有的窗口句柄是：",handles,type(handles))
# 切换到新窗口--根据索引获取新窗口句柄
driver.switch_to.window(handles[1])
# 遍历获取新句柄
for handle in handles:
    # 判断是否等于当前窗口的句柄
    if handle != current_handle:
        handles_music = handle
        # 切换窗口
        driver.switch_to.window(handles_music)
driver.find_element_by_css_selector('[placeholder="请输入歌名、歌词、歌手或专辑"]').send_keys("no 808")
driver.find_element_by_class_name('el-input__icon').click()

 