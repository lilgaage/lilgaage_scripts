import requests

# 定义通用地址
url = "http://127.0.0.1:8000/api/departments/"

# 1.1查询所有
res_get11 = requests.get(url)
print("查询所有接口返回的响应报文：", res_get11.text)

# 1.2查询指定
# 定义地址
url12 = "http://127.0.0.1:8000/api/departments/little_fox/"
res_get12 = requests.get(url12)
print("查询指定接口返回的响应报文：", res_get12.text)

# 1.3列表查询
# 定义参数列表
para13 = {"$dep_id_list": "little_fox,moon"}
res_get13 = requests.get(url, para13)
print("列表查询接口返回的响应报文：", res_get13.text)

# 1.4列表组合查询
# 定义参数列表
para14 = {"$dep_id_list": "little_fox,moon", "$dep_name_list": "百花仙子,孙悟空"}
res_get14 = requests.get(url, para14)
print("列表组合查询接口返回的响应报文：", res_get14.text)

# 1.5条件查询
# 定义参数列表
para15 = {"dep_name": "嫦娥"}
res_get15 = requests.get(url, para15)
print("条件查询接口返回的响应报文：", res_get15.text)

# 1.6条件组合查询
# 定义参数列表
para16 = {"dep_name": "孙悟空", "master_name": "花果山水帘洞"}
res_get16 = requests.get(url, para16)
print("条件组合查询接口返回的响应报文：", res_get16.text)

# 1.7模糊查询
# 定义参数列表
para17 = {"blur": "1", "slogan": "百日红"}
res_get17 = requests.get(url, para17)
print("模糊查询接口返回的响应报文：", res_get17.text)

# 1.8模糊组合查询
# 定义参数列表
para18 = {"blur": "1", "dep_name": "哥", "slogan": "梅山兄弟"}
res_get18 = requests.get(url, para18)
print("模糊组合查询接口返回的响应报文：", res_get18.text)

# 2.1新增单个
# 定义消息体数据
json01 = \
    {
        "data":
            [
                {
                    "dep_id": "jiabaoyu",
                    "dep_name": "贾宝玉",
                    "master_name": "荣国府",
                    "slogan": "荣国府衔玉而诞的公子"
                }
            ]
    }
# 调用方法，发送请求
res_post21 = requests.post(url, json=json01)
print("新增单个接口返回的响应报文：", res_post21.text)

# 2.2新增多个
# 定义消息体数据
json02 = \
    {
        "data":
            [
                {
                    "dep_id": "xuebaochai",
                    "dep_name": "薛宝钗",
                    "master_name": "蘅芜苑",
                    "slogan": "聚叶泼成千点墨，攒花染出几痕霜。"
                },
                {
                    "dep_id": "lindaiyu",
                    "dep_name": "林黛玉",
                    "master_name": "荣国府",
                    "slogan": "一朝春尽红颜老，花落人亡两不知。"
                }
            ]
    }
# 调用方法，发送请求
res_post22 = requests.post(url, json=json02)
print("新增接口返回的响应报文：", res_post22.text)

# 3.1更新
# 定义地址
url31 = "http://127.0.0.1:8000/api/departments/jiabaoyu/"
# 定义消息体数据
json31 = \
    {
        "data":
            [
                {
                    "dep_id": "jiabaoyu",
                    "dep_name": "贾宝玉",
                    "master_name": "荣国府",
                    "slogan": "他是意象化的小说人物，是作家的心灵的映像。"
                }
            ]
    }
# 调用方法，发送请求
res_put31 = requests.put(url31, json=json31)
print("更新接口返回的响应报文：", res_put31.text)

# 4.1删除单个
# 定义地址
url41 = "http://127.0.0.1:8000/api/departments/jiabaoyu/"
# 调用方法，发送请求
res_delete41 = requests.delete(url41)
print("删除单个接口返回的响应报文：", res_delete41)

# 4.2删除多个
# # 定义地址
# url42 = "http://127.0.0.1:8000/api/departments/?$dep_id_list=xuebaochai,lindaiyu"
# 定义参数列表
para42 = {"$dep_id_list": "xuebaochai,lindaiyu"}
res_delete42 = requests.delete(url, params=para42)
print("删除多个接口返回的响应报文：", res_delete42)

