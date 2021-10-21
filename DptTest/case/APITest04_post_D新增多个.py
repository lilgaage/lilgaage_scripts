import unittest
import requests

class Departments004(unittest.TestCase):
    def setUp(self) -> None:
        # 定义地址
        self.url = "http://127.0.0.1:8000/api/departments/"
        # 定制头部字段
        self.myheader = {"Content-Type": "application/json"}

    def tearDown(self) -> None:
        pass

    def test001_C_add_more001(self):
        # 定义消息体数据
        data = '{"data":[{"dep_id":"洪荒巨兽","dep_name":"移山填海","master_name":"两百万年","slogan":"鸿蒙时代"},{"dep_id":"异兽祖巫","dep_name":"洪荒巫术","master_name":"百万年","slogan":"洪荒时代"},{"dep_id":"仙秦始皇","dep_name":"飞升仙界","master_name":"十万年","slogan":"太古时代"}]}'
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


if __name__ == '__main__':
    unittest.main()

