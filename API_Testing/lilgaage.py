import requests
import re

# 作业01

# 定义地址
url_re = "http://127.0.0.1:8000/api/departments/"
#查询所有学院信息
res = requests.get(url_re).text
print(res)
# 正则表达式匹配
re_dpt = '\{"dep_id":"\d{1,10}","dep_name":"[\\u4e00-\\u9fa5_A-Z_a-z]{1,20}","master_name":"[\\u4e00-\\u9fa5_A-Z_a-z]{1,20}","slogan":"\D{0,20}"\}'

print("匹配上的学院信息有：", re.findall(re_dpt, res))


# 作业02

# 定义地址
url = "http://127.0.0.1:8000/api/departments/"
# 查询所有学院信息
res_get = requests.get(url)
# 提取第三个学院id
reg = re.findall('"dep_id":"(.*?)","dep_name":"(.*?)","master_name":"(.*?)","slogan":"(.*?)"', res_get.text)[2]
print(reg)
# 删除第三个学院信息
url_delete = "http://127.0.0.1:8000/api/departments/" + reg[0] + "/"
res_delete = requests.delete(url_delete)
print("删除第三个学院的状态码为：", res_delete.status_code)
# 新增第三个学院信息
# 定制消息头
myheader = {"Content-Type": "application/json"}
# 定义消息体数据
data = '{"data":[{"dep_id":"%s","dep_name":"%s","master_name":"%s","slogan":"%s"}]}' % (reg[0], reg[1], reg[2], reg[3])
# 发送请求
res_post = requests.post(url, data.encode('utf-8'), headers=myheader)
print("新增第三个学院信息：", res_post.text)
