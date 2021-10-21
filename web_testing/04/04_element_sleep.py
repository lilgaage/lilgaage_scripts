from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
# 实例化等待类
wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
# 显示等待判断搜索框是否存在，如果存在输入搜索内容
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#kw"))).send_keys("中公教育")
driver.find_element_by_id('su').click()

wait = WebDriverWait(driver, 10.0)



sleep(3)
driver.quit()