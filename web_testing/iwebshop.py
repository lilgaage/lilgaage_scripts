from selenium import webdriver
from time import sleep
import unittest

class Case01(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://127.0.0.1:8080/iwebshop/")

    def tearDown(self) -> None:
        sleep(3)
        self.driver.quit()

    def test_register(self):
        # 注册账号
        driver = self.driver
        driver.find_element_by_link_text("免费注册").click()
        driver.find_element_by_name('email').send_keys("1915768931@qq.com")
        driver.find_element_by_name('username').send_keys("李张格")
        driver.find_element_by_name('password').send_keys("lzg123456")
        driver.find_element_by_name('repassword').send_keys("lzg123456")
        # 手动输验证码
        sleep(30)
        driver.find_element_by_class_name('submit_reg').click()

    def test_login(self):
        # 登录
        driver = self.driver
        driver.find_element_by_link_text('登录').click()
        driver.find_element_by_name('login_info').send_keys("lilgaage")
        driver.find_element_by_name('password').send_keys("123456")
        driver.find_element_by_name('remember').click()
        driver.find_element_by_class_name('submit_login').click()


    def test_join_cart(self):
        # 加入购物车
        driver = self.driver
        driver.find_element_by_link_text('登录').click()
        driver.find_element_by_name('login_info').send_keys("lilgaage")
        driver.find_element_by_name('password').send_keys("123456")
        driver.find_element_by_name('remember').click()
        driver.find_element_by_class_name('submit_login').click()
        driver.find_element_by_link_text('首页').click()
        driver.find_element_by_link_text("女装").click()
        driver.find_element_by_link_text("莉兰秀人 限时折扣 促销 夏季 新款真丝连衣裙").click()
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_link_text("白色").click()
        driver.find_element_by_link_text("S").click()
        driver.find_element_by_class_name('add').click()
        driver.find_element_by_id('join_car').click()

    def test_address(self):
        # 填写收货地址
        driver = self.driver
        driver.find_element_by_link_text('登录').click()
        driver.find_element_by_name('login_info').send_keys("lilgaage")
        driver.find_element_by_name('password').send_keys("123456")
        driver.find_element_by_name('remember').click()
        driver.find_element_by_class_name('submit_login').click()
        driver.find_element_by_link_text('地址管理').click()
        driver.find_element_by_css_selector('[alt="收货人不能为空"]').send_keys("李张格")
        driver.find_element_by_css_selector('[value="423"]').click()
        driver.find_element_by_name('address').send_keys("广东省广州市海珠区")
        driver.find_element_by_name('mobile').send_keys("18502792331")
        driver.find_element_by_name('zip').send_keys("510220")
        driver.find_element_by_css_selector('[value="保存"]').click()

    def test_search(self):
        driver = self.driver
        driver.find_element_by_id('word').send_keys("香水")
        driver.find_element_by_css_selector('[value="商品搜索"]').click()



if __name__ == '__main__':
    unittest.main()
