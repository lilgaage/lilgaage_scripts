import unittest
import requests

class Departments003(unittest.TestCase):
    def setUp(self) -> None:
        # 定义地址
        self.url = "http://127.0.0.1:8000/api/departments/"
        # 定制头部字段
        self.myheader = {"Content-Type": "application/json"}

    def tearDown(self) -> None:
        pass

    def test001_C_type_error001(self):
        # 定义消息体数据
        data = '{"data":[{"dep_id":true,"dep_name":"长老","master_name":"盛京仙门","slogan":"玄金战体"}]}'
        # 发送请求
        res = requests.post(url=self.url, data=data.encode("utf-8"), headers=self.myheader)
        print("获取到的新增响应报文为：", res.text)
        try:
            # 获取实际代码
            code_act = res.status_code
            # 预期代码
            code_expect = 400
            # 比较
            self.assertEqual(code_act, code_expect)
        except AssertionError:
            raise

    def test002_C_type_error002(self):
        # 定义消息体数据
        data = '{"data":[{"dep_id":"望月鸾羽","dep_name":34.58,"master_name":"盛京仙门","slogan":"阴阳百宝箱"}]}'
        # 发送请求
        res = requests.post(url=self.url, data=data.encode("utf-8"), headers=self.myheader)
        print("获取到的新增响应报文为：", res.text)
        try:
            # 获取实际代码
            code_act = res.status_code
            # 预期代码
            code_expect = 400
            # 比较
            self.assertEqual(code_act, code_expect)
        except AssertionError:
            raise

    def test003_C_type_error003(self):
        # 定义消息体数据
        data = '{"data":[{"dep_id":"望月鸾云","dep_name":"真传弟子","master_name":12345,"slogan":"阴阳百宝箱"}]}'
        # 发送请求
        res = requests.post(url=self.url, data=data.encode("utf-8"), headers=self.myheader)
        print("获取到的新增响应报文为：", res.text)
        try:
            # 获取实际代码
            code_act = res.status_code
            # 预期代码
            code_expect = 400
            # 比较
            self.assertEqual(code_act, code_expect)
        except AssertionError:
            raise

    def test004_C_type_error004(self):
        # 定义消息体数据
        data = '{"data":[{"dep_id":"天轮真君","dep_name":"掌门","master_name":"万法仙门","slogan":false}]}'
        # 发送请求
        res = requests.post(url=self.url, data=data.encode("utf-8"), headers=self.myheader)
        print("获取到的新增响应报文为：", res.text)
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

