import pandas
import json

# 读取csv文件名
# 定义csv文件的路径和文件名
csv_path = "csv.csv"
# sep参数指定csv文件的分隔符，默认值是逗号，如果是制表符，该值为：\t
datacsv = pandas.read_csv(csv_path, sep=',')
print("csv数据是：", datacsv)
# csv数据转换为json数据.self指定要转换的csv数据，orient是固定写法，要转为json格式，该值为：records
datajson = pandas.DataFrame.to_json(self=datacsv, orient="records")
print("json数据是：", datajson)
# json数据转换为list
datalist = json.loads(datajson)
print("list数据是：", datalist)

