"""
import random

#random() 生成（0,1）之间的随机小数
for i in range(10):
    print(random.random())
print("-"*50)
#uniform(a,b) 生成(a,b)范围内的随机小数
for i in range(10):
    print(random.uniform(1,2)) #生成（1,2）之间的随机小数
print("-"*50)
#randint(a,b) 生成[a,b]范围内的随机整数
for i in range(10):
    print(random.randint(1,10))
print("-"*50)
#randrange(a,b,c) 生成[a,b)之间的随机整数，步长为c
for i in range(10):
    print(random.randrange(2,7,2))
print("-"*50)
#练习：随机生成大写字母
for i in range(10):
    n = random.randint(65,90)
    print(chr(n)) #chr(),将十进制数转为ascll码所对应的字符
print("-"*50)
str1 = "QWERTYUIOPASDFGHJKLZXCVBNM"
index = random.randint(0,len(str1)-1)
print(str1[index])
print("-"*50)



import time

# time模块

# time() 时间戳 单位s
print(time.time())
# localtime() 时间元祖
print(time.localtime())
'''
time.struct_time(tm_year=2021, tm_mon=8, tm_mday=27, 
                    tm_hour=11, tm_min=4, tm_sec=5, 
                    tm_wday=4, tm_yday=239, tm_isdst=0)
                    年、月、日、时、分、秒、
                    tm_wday:一周中的第几天，取值范围0~6，0表示周一
                    tm_yday：一年中的第几天，取值范围1~366
                    tm_isdst：夏令时
'''
str2 = time.localtime()
print("今天周几？",str2.tm_wday+1)
print("今天周几？",str2[6]+1)
# 练习：求5天之后是周几？
str3 = time.localtime()
wd = str3.tm_wday+6
if wd>6:
    wd-=7
print("五天后周{}".format(wd))
# strftime(format格式) 格式化字符串
'''
%Y 四位数的年 %y 两位数的年
%m 月份
%d 天
%H hour 24小时制的时 %h 12小时制的时
%M  分钟
%S 秒
%w 一周中第几天，取值0~6,0表示周日
%W 一年中第几周
%j 一年中第几天
%A 星期英文全称
%a 星期英文缩写
'''
print(time.strftime("%Y-%m-%d"))
print(time.strftime("%A"))

#time方法
time.sleep(1) #暂停1秒后再执行
# 时间戳→时间元组 localtime（时间戳）
print(time.localtime()) #默认是当前系统时间
print(time.localtime(123678329))
# mktime(时间元组)
st = (2000,2,13,20,12,34,0,0,0)
ts = time.mktime(st)
print(ts) #950443954.0
print(time.localtime(ts)) #time.struct_time(tm_year=2000, tm_mon=2, tm_mday=13, tm_hour=20, tm_min=12, tm_sec=34, tm_wday=6, tm_yday=44, tm_isdst=0)
#时间元组→格式化时间字符串 strftime
print(time.strftime("%Y-%m-%d")) #默认当前系统时间
print(time.strftime("%Y-%m-%d",time.localtime(ts))) # 2000-02-13
#格式化时间字符串→时间元组 strfptime
print(time.strptime("1999-5-20","%Y-%m-%d"))
print(time.strptime("1999/5/20","%Y/%m/%d"))

#本地时间
print(time.localtime())
#UTC时间，伦敦时间
print(time.gmtime()) #比本地时间早8小时


# 练习：求自己出生那天是周几，一年中第几天？
st1 = (2000,2,13,0,0,0,0,0,0)
lilg = time.mktime(st1)
str_lilg = time.localtime(lilg)
print("出生那天周{}，是一年中的第{}天".format(str_lilg.tm_wday+1,str_lilg.tm_yday))
"""
import random

'''
ticket = 100
age = int(input("请输入年龄:"))
if age>=0:
    if age<12 or age>70:
        print("您可以免门票进入公园")
    elif 12<=age<=18 or 55<=age<=70:
        print("您的票价为：{}".format(ticket//2))
    else:
        print("您的票价为：{}".format(ticket))
else: print("输入的年龄不合法！")

count=0
for i in range(1,101):
    if i%7==0 or i//10==7 or i%10==7:
        continue
    count+=1
    print(i, end="\t")
    if count%5==0:
        print()

def str_count(str1):
    num=0
    str=0
    underline=0
    other=0
    for i in str1:
        if i.isalpha():
            num+=1
        elif i.isdigit():
            str+=1
        elif i == "_":
            underline+=1
        else:
            other+=1
    print("{}中字母个数为{}，数字个数为{}，下划线个数为{}，其他字符个数为{}".
                                format(str1,num,str,underline,other))
str_count("idhewidhe68532___ ")

import time
day = time.localtime()
print("三天前是一年中的第{}天".format(day.tm_yday-3))

class Tester:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("这是吃的方法")
    def drink(self):
        print("这是喝的方法")
    def test(self):
        print("这是测试的方法")
    def bug(self):
        print("这是提bug的方法")
test1 = Tester("lilgaage")
test1.eat()
test1.drink()
test1.test()
test1.bug()

list = []
for sroce in range(5):
    score = float(input("请输入成绩："))
    list.append(score)
print("最高分为：{}，最低分为{}".format(max(list),min(list)))
list.sort()
list.pop(0)
list.pop(-1)
print("去掉最高最低分后，平均分为：{}".format(sum(list)/3))
print(list)
'''

'''
import random
for i in range(5):
    print(random.randrange(0,101,3))

import random
for i in range(5):
    print("中奖号码为：{}".format(random.randint(1,100)))

import random
print(random.randint(10,20))


import random

verify_list = []
#将大小写字母、数字元素添加到验证码列表中
for i in range(65,90):
    verify_list.append(chr(i))
for j in range(97,122):
    verify_list.append(chr(j))
for k in range(48,58):
    verify_list.append(chr(k))
print("随机生成的验证码为：")
#根据列表索引随机遍历5个元素
for n in range(5):
    code = random.randrange(0, len(verify_list) - 1)
    print(verify_list[code],end="")


import time
str = "2019-10-10 23:40:00"
mkt = time.strptime(str,"%Y-%m-%d %H:%M:%S")
print(mkt)
print(time.mktime(mkt))

import time
time1 = "2020-10-01 23:40:00"
#先转换为时间元组
st = time.strptime(time1,"%Y-%m-%d %H:%M:%S")
print(time.strftime("%Y/%m/%d %H:%M:%S",st))

import time
st1 = "1949-10-1"
#转为时间元组
zg = time.strptime(st1,"%Y-%m-%d")
print("新中国成立那天周{}，是当年中的第{}天".format(zg.tm_wday+1,zg.tm_yday))

import time
t = time.localtime()
wd = t.tm_wday+6
if wd>6:
    wd-=7
print("五天后周{}".format(wd))

import time
t = time.localtime()
print("三天后是一年中的第{}天".format(t.tm_yday+3))

class Cat:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("这是吃的方法")
    def catch(self):
        print("这是抓老鼠的方法")
    def sleep(self):
        print("这是睡的方法")
c1 = Cat("瑰丝")
c1.eat()
c1.catch()
c1.sleep()

with open("CeshiFiles/a.txt",mode='w') as file1:
    file1.write("lizhangge\n")
    file1.write("18502792331")
with open("CeshiFiles/a.txt") as file2:
    ret = file2.read()
with open("CeshiFiles/b.txt",mode='w') as file3:
    file3.write(ret)

import random
print("欢迎来到随机石头剪刀布游戏，0代表石头，1代表布，2代表箭头")
user_game = int(input("您出什么呢："))
game = random.randint(0,2)
print("计算机出：",game)
if 0 <= user_game <=2:
    if user_game == game:
        print("平局!")
    elif user_game == game-1 or user_game ==2 and game==0:
        print("您输了！")
    else:
        print("您赢了！")
else:
    print("您的出拳不符规则，请重新开始游戏！")
'''

'''
import random
list1 = [2,34,56,78,543]
tup1 = (2,3,432,232,546)
#随机在序列中取一个元素
print(random.choice(list1))
print(random.choice(tup1))
#随机打乱列表的顺序
random.shuffle(list1)
print(list1)


#写入文件
file_A = open("CeshiFiles/c.txt",mode="w")
file_A.write("123456789\n")
file_A.write("dewddew")
file_A.close() #关闭文件



import time
# 3天以前是一年中第几天
t = time.time() - 3600 * 24 * 3
st= time.localtime(t)
print("三天前是一年中第{}天".format(st.tm_yday))

# 5. 输入某年某月某日，判断这一天是这一周的星期几
day = input('请以20xx-x-x格式输入时间：')
a = time.strptime(day, '%Y-%m-%d')
print('这是星期{}'.format(a[6]+1))
print('这是星期{}'.format(time.strftime("%w", a)))
'''
'''
请以20xx-x-x格式输入时间：2021-8-29
这是星期7
这是星期0
'''

list1 = [2,34,56,78,543]
try:
    #可能会出现异常的代码
    print(5/0)
    index = random.randint(0,10)
    print(index,list1[index])
except ZeroDivisionError:
    print("这是除零错误")
    raise
except IndexError: #此方法不能同时处理多个异常
    print("这是索引越界错误")
except (ZeroDivisionError,IndexError):
    print("此方法可同时处理多个异常")
else:
    print("没有异常执行...")
finally:
    print("有没有异常都执行...")