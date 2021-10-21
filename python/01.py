'''
print("0213")
name="lilgaage"
age=21
print(name,age)
print("李张格")
print("ghost")
print(99.05)
name="lilgaage"
age=21
sex="女"

name=input("请输入姓名：")
age=input("请输入年龄：")
hobby=input("请输入爱好：")
print(name+"今年"+age+"岁了，她最喜欢的事情是"+hobby)
# print(type(age)) # 查看age类型


age=21 #整数
salary=7432.43 #浮点数
percent=0.00000000000000000000012 #=1.2e-22  科学计数法
print(percent,type(percent))
b1=False #布尔值
b2=True
c1=complex(3,4) #复数等于实数+虚数
str1="lilgaage" #字符串
list1=['lilgaage','lizhangge','ghost'] #列表
tup1=('lilgaage','lizhangge','ghost') #元组
dic1={"name":"lilgaage","age":21,"sex":"女","hobby":["种树","养鸡"]} #字典
set1={'ghost',22,"gaage",21} #集合

print(list1,tup1,dic1,set1,sep="\n")


import keyword #查看关键字
print(keyword.kwlist)


print(int(23.6)) #直接取整
print(int('765')) #纯数字的字符串才能转换成整数，不能有小数点
print(float(23))
print(float(12.89))
print(float('56.9'))
print(str(34.7))
print(str(76))
name="ghost"
age=22
print(name+"今年"+str(age)+"岁")

chr() #按照utf8编码表，把十进制数转换为对应的字符
eval()#把数学表达式构成的字符串计算并输出结果

print(eval('123+90*0.1'))
'''

# **幂运算
# //地板除 直接取整






#name="lilgaage"
#title="组长"
#email="1915768931@qq.com"

#string='hello'
#string1='python'
#print(string+string1)
#print(string,string1)

#name=input("请输入姓名：")
#age=input("请输入年龄：")
#hometown=input("请输入家乡：")
#salary=input("请输入期望工资")
#print(name+"今年"+str(age)+"岁，来自"+hometown+"，他的期望现在是"+salary+"元")

#num1=int('123')
#print(num1)

# &#x674E;&#x5F20;&#x683C;
#print(chr(26446)+chr(24352)+chr(26684))

s=5000
t=s//60//60
m=(s-t*60*60)//60
s=(s-t*60*60)%60
print('5000秒=%d时%d分%d秒'%(t,m,s))

print("我爱你"*5)