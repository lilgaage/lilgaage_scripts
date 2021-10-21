import requests
import unittest

class Departments006(unittest.TestCase):
    def test001_update_right(self):
        # 覆盖所有参数，返回正常，状态码为200
        # 定义地址
        url = "http://127.0.0.1:8000/api/departments/flower/"
        # 定义消息体数据
        json01 = {
            "data":
                [
                    {
                        "dep_id": "flower",
                        "dep_name": "百花仙子",
                        "master_name": "其实就是花园的园丁",
                        "slogan": "人无千日好，花无百日红。",
                    }
                ]
        }
        res = requests.put(url, json=json01)
        print("更新接口返回的响应报文为：", res.text)
        try:
            # 获取实际代码
            code_act = res.status_code
            # 预期代码
            code_expect = 200
            # 比较
            self.assertEqual(code_act, code_expect)
        except AssertionError:
            raise

    def test002_update_inverse(self):
        # 缺少必填参数master_name，提示错误，状态码为400
        # 定义地址
        url = "http://127.0.0.1:8000/api/departments/ErlangGod/"
        # 定义消息体数据
        json01 = {
            "data":
                [
                    {
                        "dep_id": "ErlangGod",
                        "dep_name": "二郎神",
                        "slogan": "二郎神有梅山兄弟和哮天犬。",
                    }
                ]
        }
        res = requests.put(url, json=json01)
        print("更新接口maste_name缺失，返回的响应报文为：", res.text)
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
    
