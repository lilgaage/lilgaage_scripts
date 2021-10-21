import requests
import unittest

class Departments005(unittest.TestCase):
    def setUp(self) -> None:
        # 定义地址
        self.url = "http://127.0.0.1:8000/api/departments/"

    def tearDown(self) -> None:
        pass

    def test001_select_right(self):
        # 查询所有学院信息，返回正常，状态码为200
        res = requests.get(self.url)
        print("1.1接口返回的响应报文为：", res.text)
        try:
            # 获取实际代码
            code_act = res.status_code
            # 预期代码
            code_expect = 200
            # 比较
            self.assertEqual(code_act, code_expect)
        except AssertionError:
            raise

    def test002_select_inverse(self):
        # 1.3接口，参数值类型错误，提示错误，状态码为400
        # 定义参数列表
        para = {"dep_name": True}
        res = requests.get(self.url, para)
        print("1.3接口参数值类型错误返回的响应报文为：", res.text)
        try:
            # 获取实际代码
            code_act = res.status_code
            # 预期代码
            code_expect = 400
            # 比较
            self.assertEqual(code_act, code_expect)
        except AssertionError:
            raise


if __name__ == '__main__':
    unittest.main()

