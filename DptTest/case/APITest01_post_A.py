import unittest
import ddt
import requests
from data import getcsv

# 获取参数化的数据
list01 = getcsv.datalist

@ddt.ddt()
class Departments001(unittest.TestCase):
    @ddt.data(*list01)
    # dptname将遍历取得list01列表中的每个元素

    def test001_A(self,dptinfo):
        if dptinfo["dep_id"] == None:
            dpid = ""
        else:
            dpid = dptinfo["dep_id"]
        if dptinfo["dep_name"] == None:
            dpname = ""
        else:
            dpname = dptinfo["dep_name"]
        if dptinfo["master_name"] == None:
            mtname = ""
        else:
            mtname = dptinfo["master_name"]
        if dptinfo["slogan"] == None:
            slogan = ""
        else:
            slogan = dptinfo["slogan"]

        # 定义地址
        url = "http://127.0.0.1:8000/api/departments/"
        data = '{"data":[{"dep_id":"%s","dep_name":"%s","master_name":"%s","slogan":"%s"}]}' % (dpid, dpname, mtname, slogan)

        print("拼接的消息体数据为：", data)
        # 定制头部字段
        myheader = {"Content-Type": "application/json"}
        # 发送请求
        res = requests.post(url=url, data=data.encode("utf-8"), headers=myheader)
        print("获取到的新增响应报文为：", res.text)
        try:
            # 获取实际状态码
            code_act = res.status_code
            # 获取预期状态码
            code_expect = dptinfo["code"]
            # 比较
            self.assertEqual(str(code_act), str(code_expect))
        except AssertionError:
            raise 


if __name__ == '__main__':
    unittest.main()

