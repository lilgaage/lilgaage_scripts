from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.offcn.com")
# 滚动条处于中间位置
js3 = "window.scrollTo(0,3000)"
driver.execute_script(js3)
sleep(2)
# 滚动条处于顶部
js2 = "window.scrollTo(0,0)"
driver.execute_script(js2)
sleep(2)
# 滚动条处于底部
js1 = "window.scrollTo(0,8000)"
driver.execute_script(js1)
sleep(2)
driver.find_element_by_link_text('职位查询').click()

sleep(2)
driver.quit()