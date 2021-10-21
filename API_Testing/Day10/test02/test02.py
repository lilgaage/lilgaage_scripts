import requests
import unittest

class Case001(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_001_insert(self):
        # 增
        # 定义地址
        url = "http://127.0.0.1:8000/api/departments/"
        # 定义消息体数据
        json01 = \
            {
                "data":
                    [
                        {
                            "dep_id": "python01",
                            "dep_name": "python01",
                            "master_name": "python01",
                            "slogan": "python01"
                        }
                    ]
            }
        # 调用方法，发送请求
        res_post01 = requests.post(url, json=json01)
        Expected = 201
        # 获取状态码
        Actual = res_post01.status_code
        self.assertEqual(Expected, Actual)
        print("post方法返回的响应报文：", res_post01.text)

    def test_002_select(self):
        # 查
        # 定义地址
        url_get = "http://127.0.0.1:8000/api/departments/python01/"
        # 调用方法，发送请求
        res_get01 = requests.get(url_get)
        # 预期结果
        Expected = 200
        # 获取状态码，实际结果
        Actual = res_get01.status_code
        # 比较预期结果和实际结果
        self.assertEqual(Expected, Actual)
        print("get方法返回的响应报文：", res_get01.text)

    def test_003_update(self):
        # 改
        # 定义地址
        url_put = "http://127.0.0.1:8000/api/departments/python01/"
        # 定义消息体数据
        json11 = \
            {
                "data":
                    [
                        {
                            "dep_id": "python01",
                            "dep_name": "python01",
                            "master_name": "python01",
                            "slogan": "他是作家的心灵的映像。"
                        }
                    ]
            }
        # 调用方法，发送请求
        res_put01 = requests.put(url_put, json=json11)
        # 预期结果
        Expected = 200
        # 获取状态码，实际结果
        Actual = res_put01.status_code
        # 比较预期和实际
        self.assertEqual(Expected, Actual)
        print("post方法返回的响应报文：", res_put01.text)

    def test_delete_004(self):
        # 删
        # 定义地址
        url_delete = "http://127.0.0.1:8000/api/departments/python01/"
        # 调用方法，发送请求
        res_delete01 = requests.delete(url_delete)
        Expected = 204
        # 获取状态码
        Actual = res_delete01.status_code
        self.assertEqual(Expected, Actual)
        print("delet方法返回的响应报文：", res_delete01)


if __name__ == '__main__':
    unittest.main()

