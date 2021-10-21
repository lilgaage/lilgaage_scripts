import requests
import unittest
import ddt

list_name = [{"dep_name": "小狐狸"}, {"dep_name": "嫦娥"}, {"dep_name": "百花仙子"}]

@ddt.ddt()
class Select(unittest.TestCase):
    @ddt.data(*list_name)
    def test_select(self, para):
        # 定义地址
        url = "http://127.0.0.1:8000/api/departments/"
        res_get = requests.get(url, para)
        print("查询返回的响应报文为：", res_get.text)


if __name__ == '__main__':
    unittest.main()

