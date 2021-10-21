from ddt import unpack
import unittest
import requests
import ddt

list_departments = [{
                    "dep_id": "jiabaoyu",
                    "dep_name": "贾宝玉",
                    "master_name": "荣国府",
                    "slogan": "他是意象化的小说人物，是作家的心灵的映像。"
                },
                {
                    "dep_id": "lindaiyu",
                    "dep_name": "林黛玉",
                    "master_name": "荣国府",
                    "slogan": "一朝春尽红颜老，花落人亡两不知。"
                },
                {
                    "dep_id": "xuebaochai",
                    "dep_name": "薛宝钗",
                    "master_name": "蘅芜苑",
                    "slogan": "聚叶泼成千点墨，攒花染出几痕霜。"
                }]

@ddt.ddt()
class Departments(unittest.TestCase):
    @ddt.data(*list_departments)
    # unpack根据data取到的数据后，又根据逗号进行拆分
    @unpack
    def test_insert(self, dep_id, dep_name, master_name, slogan):
        # 定义地址
        url = "http://127.0.0.1:8000/api/departments/"
        # 定义消息体数据
        json_dep =\
            {
                "data":
                    [
                        {
                            "dep_id": dep_id,
                            "dep_name": dep_name,
                            "master_name": master_name,
                            "slogan": slogan
                        }
                    ]
            }
        res_post = requests.post(url, json=json_dep)
        print("新增信息返回的响应报文为：", res_post.text)


if __name__ == '__main__':
    unittest.main()

