import unittest
import requests

class Departments002(unittest.TestCase):
    def setUp(self) -> None:
        # 定义地址
        self.url = "http://127.0.0.1:8000/api/departments/"
        # 定制头部字段
        self.myheader = {"Content-Type": "application/json"}

    def tearDown(self) -> None:
        pass

    def test001_B_surplus(self):
        # 定义消息体数据
        data = '{"data":[{"dep_id":"琉璃仙","dep_name":"小琉璃","master_name":"郭晓婷","slogan":"修炼剑心通明","another":"灵剑派"}]}'
        # 发送请求
        res = requests.post(url=self.url, data=data.encode("utf-8"), headers=self.myheader)
        print("获取到的新增响应报文为：", res.text)
        try:
            # 获取实际代码
            code_act = res.status_code
            # 预期代码
            code_expect = 201
            # 比较
            self.assertEqual(code_act, code_expect)
        except AssertionError:
            raise

    def test002_B_lack_slogan(self):
        # 定义消息体数据
        data = '{"data":[{"dep_id":"test213","dep_name":"test213","master_name":"test213"}]}'
        # 发送请求
        res = requests.post(url=self.url, data=data.encode("utf-8"), headers=self.myheader)
        print("获取到的新增响应报文为：", res.text)
        try:
            # 获取实际代码
            code_act = res.status_code
            # 预期代码
            code_expect = 201
            # 比较
            self.assertEqual(code_act, code_expect)
        except AssertionError:
            raise

    def test003_B_lack_dpid(self):
        # 定义消息体数据
        data = '{"data":[{"dep_name":"掌门","master_name":"盛京仙门","slogan":"大乘"}]}'
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

    def test004_B_lack_dpname(self):
        # 定义消息体数据
        data = '{"data":[{"dep_id":"天月","master_name":"盛京仙门","slogan":"合体"}]}'
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

    def test005_B_lack_mtname(self):
        # 定义消息体数据
        data = '{"data":[{"dep_id":"琼华","dep_name":"首席弟子","slogan":"合体"}]}'
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

