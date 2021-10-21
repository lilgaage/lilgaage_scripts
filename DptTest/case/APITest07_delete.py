import requests
import unittest

class Departments005(unittest.TestCase):
    def test001_delete_right(self):
        # 删除单个学院信息，返回正常，状态码为200
        # 定义地址
        url = "http://127.0.0.1:8000/api/departments/曲/"
        res = requests.delete(url)
        try:
            # 获取实际代码
            code_act = res.status_code
            # 预期代码
            code_expect = 204
            # 比较
            self.assertEqual(code_act, code_expect)
        except AssertionError:
            raise

    def test002_delete_inverse(self):
        # 删除不存在的学院信息，提示错误，状态码为400
        # 定义地址
        url = "http://127.0.0.1:8000/api/departments/小玉/"
        res = requests.get(url)
        try:
            # 获取实际代码
            code_act = res.status_code
            # 预期代码
            code_expect = 404
            # 比较
            self.assertEqual(code_act, code_expect)
        except AssertionError:
            raise


if __name__ == '__main__':
    unittest.main()

