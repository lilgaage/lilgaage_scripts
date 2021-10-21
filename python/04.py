'''
#元组
tup1 = ("ghost","gaage","娃琳可","鬼瓷")
print(tup1[-1])
print(tup1[0])
print(tup1[::-1])
print(tup1[1:2:2])
for i in range(len(tup1)):
    print(tup1[i],end="\t")
for i in tup1:
    print(i,end="\t")
tup2 = ("ghost")
tup3 = ("ghost",)
print(type(tup2),type(tup3)) #	<class 'str'> <class 'tuple'>
tup4 = ("ghost","gaage","娃琳可","鬼瓷")
list1 = list(tup4) #元组转列表
tup5 = tuple(list1)#列表转元组
print(list1,tup5,sep="\n")
str1 = "ghost"
list2 = list(str1)#字符串转列表
tup6 = tuple(str1)#字符串转元组
print(list2,tup6,sep="\n")
tup7 = (1,2,3,4,5,6,7,8,9,10)
print(max(tup7))
print(min(tup7))
print(sum(tup7))
print(len(tup7))
'''
'''
#字典 无序，没有索引 键值对key:value
dic1 = {"name":"ghost","age":22,"height":178.5,"job":["vocal","rap","dance"]}
print(dic1["name"]) #根据键查对应的值
print(dic1["job"])
print(len(dic1))

for i in dic1: #遍历所有的key
    print(i)
for key in dic1.keys(): #遍历所有的key
    print(key)
for value in dic1.values():#遍历所有的value
    print(value)
print("-"*30)
for item in dic1.items(): #以元组方式遍历所有的键值对
    print(item)
    for i in item: #遍历key和value构成的元组
        print(i)
print("-"*30)
for key,value in dic1.items(): #遍历所有的键和值
    print(key,"----",value)

dic1["weight"] = 49.6 #增加
print(dic1)
dic1["name"] = "lilghost" #修改
dic1.pop("weight") #pop(key),根据key删除一个元素
dic1.popitem() #popitem(),随机删除一个元素
print(dic1.keys()) #查询所有键 dict_keys(['name', 'age', 'height'])
print(dic1.values()) #查询所有值 dict_values(['lilghost', 22, 178.5])
print(dic1.items()) # dict_items([('name', 'lilghost'), ('age', 22), ('height', 178.5)])
print(dic1.get("age"))
'''
'''
#函数不调用不会执行
def area_length():  #无参无返回值
    PI = 3.1415926
    r =float(input("请输入半径："))
    s =PI * r ** 2
    l = 2 * PI * r
    print("半径为{}的圆面积是{}，周长是{}".format(r,s,l))
area_length() #调用函数

def sum_product(n1,n2):    #有参无返回值
    sum=n1+n2
    product=n1*n2
    print("{}，{}和为{}，积为{}".format(n1,n2,sum,product))
sum_product(3,4)

def area_length(r):  #有参有返回值
    PI = 3.1415926
    s =PI * r ** 2
    l = 2 * PI * r
    return "半径为{}的圆面积是{}，周长是{}".format(r,s,l)
#返回值必须有变量进行接收
str1 = area_length(4)
print(str1)

def sum_product(n1,n2):    #有参有返回值
    sum=n1+n2
    product=n1*n2
    return "{}，{}和为{}，积为{}".format(n1,n2,sum,product)
#返回值必须有变量进行接收
num1 = sum_product(3,4)
print(num1)

def sum_product(n1,n2):    #有参有返回值
    sum=n1+n2
    product=n1*n2
    return sum,product
print("两个数的和、积为：",sum_product(4,5)) #多个返回值，返回类型为一个元祖
ret = sum_product(3,5)
print("两个数的和、积为：",ret[0],ret[1])

def product(p):
    pro=1
    for i in range(1,p+1):
        pro*=i
    print("{}的阶乘为：{}".format(p,pro))
product(5)

def product(p):
    pro=1
    for i in range(1,p+1):
        pro*=i
    return pro
print("5的阶乘为:",product(5))
'''
'''
#引入模块
from python.day04ceshi import ceshi01
#调用模块
ceshi01.say_hello()
print("鬼瓷的职业是："+ceshi01.job)

import time
print(time.localtime())
from time import sleep
print("start...") 
sleep(5) #隔5秒后再执行
import random
print(random.randint(1,10))
'''

'''
#1
dict = {"k1":"v1","k2":"v2","k3":"v3"}
for key in dict.keys():
    print(key)
print("-"*30)
#2
for value in dict.values():
    print(value)
print("-"*30)
#3
dict["k4"]="v4"
print(dict)
print("-"*30)
#4
dict.pop("k1")
print(dict)
print("-"*30)
#5
print(dict.get("k6"))

def sum(n):
    s=0
    for i in range(1,n+1):
        s +=i
    print("1+2+3+4+……+{}的和为{}".format(n,s))
sum(6)

def count_str(str):
    num=0
    char=0
    other=0
    space=0
    for i in str:
        if i.isdigit():
            num+=1
        elif i.isalpha():
            char+=1
        elif i == " ":
            space+=1
        else:
            other+=1
    print("数字个数为%d，字母个数为%d，空格个数为%d,其他字符个数为%d" %(num,char,space,other))
count_str("deg.;'w d32 ' 324d =-")

def multiply_divide(num,num1):
    if num1 == 0:
        return False
    else:
        mul = num * num1
        div = num / num1
        return mul,div
print(multiply_divide(3,0))


a = {'001': {'name': '张三', 'age': 20, 'address': '北京', 'score': 88},
     '002': {'name': '李四', 'age': 20, 'address': '山东', 'score': 78},
     '003': {'name': '王五', 'age': 20, 'address': '北京', 'score': 95},
     '004': {'name': '小明', 'age': 20, 'address': '河北', 'score': 90}
     }
for value in a.values():
        if value["address"] == "北京":
            value["hous_allowance"] = 1000
        print(value)
'''
tup = (17, 12, 23, 4,43, 63,56, 72, 14, 39)
print(sum(tup))
for i in tup:
    if i%7==0 or i//10==7 or i%10==7:
        print(i,end="\t")
print("最大值为{}其下标是{}，最小值为{}其下标是{}".format(
    max(tup),tup.index(max(tup)),min(tup),tup.index(min(tup))))





