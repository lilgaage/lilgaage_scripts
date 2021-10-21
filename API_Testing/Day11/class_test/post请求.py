import unittest
import ddt
import requests
from Day11.class_test import getcsv

# 获取参数化的数据
list01 = getcsv.datalist

@ddt.ddt()
class Dep01(unittest.TestCase):
    @ddt.data(*list01)
    # 将遍历取得list01列表中的每个元素，list01中有几个元素，Dep01将循环几次
    def test01(self,dptinfo):
        dptid = dptinfo["dep_id"]
        dptname = dptinfo["dep_name"]
        mastername = dptinfo["master_name"]
        slogan = dptinfo["slogan"]
        # 定义地址
        url = "http://127.0.0.1:8000/api/departments/"
        data = '{"data":[{"dep_id":"%s","dep_name":"%s","master_name":"%s","slogan":"%s"}]}' % (dptid, dptname, mastername, slogan)

        print("拼接的消息体数据为：", data)
        # 定制头部字段
        myheader = {"Content-Type": "application/json"}
        # 发送请求
        res = requests.post(url=url, data=data.encode("utf-8"), headers=myheader)
        print("获取到的新增响应报文为：", res.text)
        # 获取实际代码
        code_act = res.status_code
        # 获取预期代码
        code_expect = dptinfo["code"]
        # 比较
        self.assertEqual(str(code_act), str(code_expect))


if __name__ == '__main__':
    unittest.main()

