import unittest
import ddt
import requests
# 列表
list01 = [{"dep_id": "诗", "dep_name": "唐诗", "master_name": "李白", "slogan": "床前明月光", "code": 201}, {"dep_id": "词", "dep_name":"宋词", "master_name": "苏轼", "slogan": "醉里挑灯看剑", "code": 201}, {"dep_id": "曲", "dep_name": "元曲", "master_name": "关汉卿", "slogan": "窦娥冤", "code": 201}]

@ddt.ddt()
class OutputNum(unittest.TestCase):
    @ddt.data(*list01)
    # dptname将遍历取得list01列表中的每个元素，list01中有几个元素，output01将循环几次

    def test01(self,dptinfo):
        # dptinfo的值为：{"dep_id":"诗","dep_name":"唐诗","master_name":"李白","slogan":"床前明月光"}
        print("当前的学院信息为：", dptinfo)
        print("当前的学院id为：", dptinfo["dep_id"])
        print("当前的学院名为：", dptinfo["dep_name"])
        print("当前的院长名为：", dptinfo["master_name"])
        print("当前的口号为：", dptinfo["slogan"])
        dptid = dptinfo["dep_id"]
        dptname = dptinfo["dep_name"]
        mastername = dptinfo["master_name"]
        slogan = dptinfo["slogan"]
        #地址
        url = "http://127.0.0.1:8000/api/departments/"
        #数据，理解为主，如果不理解，采用第二种方式
        # data = '{"data":[{"dep_id":"' \
        #         + dptid + \
        #         '","dep_name":"' \
        #         + dptname + \
        #          '","master_name":"' \
        #        + mastername + \
        #        '","slogan":"' \
        #        + slogan + \
        #        '"}]}'
        # 建议以下写法
        data = '{"data":[{"dep_id":"%s","dep_name":"%s","master_name":"%s","slogan":"%s"}]}' % (dptid, dptname, mastername, slogan)
        # data = '{"data":[{"dep_id":{},"dep_name":{},"master_name":{},"slogan":{}}]}'.format(
        # dptid, dptname, mastername, slogan)      (x)

        print("拼接的消息体数据为：", data)
        # 头部字段
        myheader = {"Content-Type": "application/json"}
        #请求
        res = requests.post(url=url, data=data.encode("utf-8"), headers=myheader)
        print("获取到的新增响应报文为：", res.text)
#       获取实际代码
        code_act = res.status_code
#       获取预期代码
        code_expect = dptinfo["code"]
#         比较
        self.assertEqual(str(code_act), str(code_expect))


if __name__ == '__main__':
    unittest.main()

