from selenium import webdriver
from time import sleep
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")
sleep(2)
# 获取cookie
print("百度id的cookie：", driver.get_cookie('BAIDUID'))
print("百度的所有cookie：", driver.get_cookies())
# 添加cookie
driver.add_cookie({"name": "BAIDUID", "value": "D44A76A2C6331E3E8A42ABFDD851D890:FG=1"})
driver.add_cookie({"name": "BDUSS", "value": "WkxYnpJTGt4ZmgwS3p5OVZhVk8xMmhqS2ZXb1FjbHY5dFhaMmtzbEg5WjdJVmxoRVFBQUFBJCQAAAAAAAAAAAEAAACj~ZlRbW5udWFuAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHuUMWF7lDFha"})
sleep(1)
# 刷新
driver.refresh()
sleep(2)
# 截图保存
now_time = time.strftime("%Y%m%d_%H%M%S")
driver.get_screenshot_as_file("images/img_{}_cookie自动登录百度.png".format(now_time))

sleep(3)
driver.quit()
