import requests

# 定义地址
# url = "http://127.0.0.1:8000/api/departments/"

# get请求，查询所有学院信息
# 调用方法，发送请求
res01 = requests.request("get", url)
print("request方法获取的get响应报文为：", res01.text)

# get请求不带参数
# 调用方法，发送请求
res02 = requests.get(url)
print("get请求不带参数返回", res02)
print("get请求不带参数返回的报文文本为：", res02.text)
print("get请求不带参数返回的状态码为：", res02.status_code)
print("get请求不带参数返回的头部字段为：", res02.headers)

# get请求带参数
# 定义参数列表，分析清楚参数名和参数值分别是什么
para03 = {"dep_name": "小狐狸"}
# 发送请求，获取响应，存入一个变量
res03 = requests.get(url, para03)
print("get请求带参数返回的响应报文文本为：", res03.text)

# post请求带消息体数据，方式一：纯文本格式
# 定制请求头，指定消息体格式为json
myheader04 = {"Content-Type": "application/json"}
# 定义消息体数据，纯文本格式
data = '{"data":[{"dep_id":"flower","dep_name":"百花仙子","master_name":"百花园","slogan":"花无百日红"}]}'
# 发送请求，获取响应，存入变量
# 调用encode方法，转换编码格式
res04 = requests.post(url, data.encode("utf-8"), headers=myheader04)
print("post请求带纯文本消息体数据返回的响应报文为：", res04.text)

# 定义地址
url = "http://127.0.0.1:8000/api/departments/"

# post请求带消息体数据，方式二：json格式
# 定义消息体数据，json格式
json01 = \
    {
        "data":
            [
                {
                    "dep_id": "monkey",
                    "dep_name": "孙悟空",
                    "master_name": "花果山水帘洞",
                    "slogan": "知恩不报非君子，万古千秋作骂名。"
                }
            ]
    }
# 发送请求，存入变量
res05 = requests.post(url, json=json01)
print("post带json格式消息体数据返回的响应报文为：", res05.text)

