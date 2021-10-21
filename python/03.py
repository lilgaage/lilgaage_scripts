'''
#字符串
name = "ghost"
print(name, id(name), id("ghost")) #id()，获取变量在内存中的地址
name = "鬼瓷"
print(name, id(name), id("鬼瓷"))
str1 = "娃琳可"
print(len(str1)) #len()，获取字符串长度
print(str1[0]) #根据索引获取元素，变量名[索引]
print(str1[1])
print(str1[-1])
str2 = "0123456789" #切片，变量名[起始索引:结束索引:步长]，包头不包尾
print(str2[5:10:1])
print(str2[1:8:])
print(str2[:5:])
print(str2[::])
print(str2[::-1]) #逆序输出
print(str2[8:3:-1]) #步长为负，起始索引>结束索引

str3 = "鬼瓷就是娃琳可" #遍历字符串
for i in range(len(str3)): #遍历索引，然后依据索引获取元素
    print(i,str3[i])
for i in str3: #直接遍历字符串元素
    print(i)
#字符串方法
print(str3.count("鬼")) #count()，统计字符串中某一个元素出现的次数
print(str3.count("凯"))
print(str3.index("鬼")) #index()，从左开始查找字符的索引位置
print(str3.index("娃琳可")) #查找字符串，并显示符合条件的第一个元素的索引位置
print("娃琳可".index("娃琳"))
str4 = "sharining. in. the. dark"
print(str4.split()) #split(),拆分字符串，默认使用空格拆分
print(str4.split(".")) #指定拆分字符
print(str4.replace("dark","write")) #replace(),替换，默认替换所有
print(str4.replace("i","I",2)) #指定替换个数
str5 = "###***ghost###***  "
print(str5.strip())  #strip(),去除字符串左右空格
print(str5.strip("#")) #指定去除的元素，仅能替换引号附近的字符
print(str5.strip("*"))
print("ghost52".isalnum()) #判断字符串是否由字母和数字组成
print("ghost.52".isalpha()) #判断字符串是否由字母组成
print("52".isdigit()) #判断字符串是否由数字组成
print("GHOST".isupper()) #判断字符串是否由大写字母组成
print("ghsot".islower()) #判断字符串是否由小写字母组成
str6 = "娃琳可.ghsot"
print(str6.startswith("娃琳")) #判断字符串开头是否为指定元素
print(str6.endswith("ot")) #判断字符串结尾是否为指定元素
print(str6.startswith("g",4,9)) #根据索引截取字符串的一部分进行判断，含头不含尾
print(str6.endswith("t",4,9))


qq=input("请输入QQ号码：")
if qq.endswith("@qq.com") and qq[-8::-1].isdigit():
    print("QQ邮箱正确！")
else:
    print("输入不合法！")

if qq.endswith("@qq.com") and qq.replace("@qq.com","").isdigit():
    print("QQ邮箱正确！")
else:
    print("输入不合法！")

#format方法格式字符串
print("{}今年{}岁了。".format("ghost",22))
name = "娃琳可"
age = 22
print("{}今年{}岁。".format(name,age))


num=0
char=0
other=0
for i in "1234abcABCDE_":
    if i.isdigit():
        num+=1
    elif i.isalpha():
        char+=1
    else:
        other+=1
print("数字个数为%d，字母个数为%d，其他字符个数为%d" %(num,char,other))
'''
"""
#转义字符
\n 换行
\t tab键
\' 输出一个单引号
\" 输出一个双引号
\\ 输出一个\
\newline 长代码换行显示，在末尾加\表示这一行代码没有结束

#元字符
r/R 元字符，让转义字符失效

print("he\tlo\nGhost")
print(r"he\tlo\nGhost")
"""
'''
list1 = ["ghost","gaage","娃琳可","鬼瓷"]
print(list1[0])
print(list1[-1])
print(list1[::-1])
print(list1[0:2:])
print(list1[3:0:-1])
for i in list1:
    print(i)
for i in range(len(list1)):
    print(list1[i])

list2 = ["ghost","gaage","娃琳可","鬼瓷"]
print(list2.append("NYK")) #append(),新增元素
print(list2.append("love song"))
print(list2.pop()) #pop(),默认删除最后一个元素
print(list2.pop(4)) #删除指定索引元素
print(list.remove("gaage")) #remove(),从左开始删除一个指定元素
print(list2[-1]) #根据索引查元素
print(list2.count("鬼瓷")) #计数
print(list2.index("娃琳可")) #查索引
print(len(list2)) #元素个数
print(max(list2))
print(min(list2))
print(sum(list2))
print(list2.sort()) #sort(),排序
'''
''' 
S="20181178431"
count=0
for i in S:
    if i=="1":
        count+=1
print("S中1的个数为%d" %count)

count=0
for i in "24342916457834":
    if int(i)%2!=0:
        count+=1
print("字符串中奇数的个数为%d" %count)

sum=0
avg=0
for i in range(5):
    num=float(input("请输入数字："))
    sum+=num
    avg=sum/5
print("平均值为%.2f" %avg)

className = "软测0726"
classNum = 19
classMale = "71.86%"
print("班级名称是："+className+"，班级人数是"+str(classNum)+"人，班级男生占总人数"+classMale)
print("班级名称是：%s，班级人数是%d人，班级男生占总人数%s" %(className,classNum,classMale))
print("班级名称是：{}，班级人数是{}人，班级男生占总人数{}".format(className,classNum,classMale))

s=input("请输入：")
if s.isdigit():
    print("输入是数字")
else:
    print("输入不合法！")

#1
score = []
score.append(68)
score.append(87)
score.append(92)
score.append(100)
score.append(76)
score.append(88)
score.append(54)
score.append(89)
score.append(76)
score.append(61)
#2
print(score[2])
#3
print(score[:6:])
#4
num = 76
print(score.count(num))
#5
print(score.index(100))
#6
score.append(59)
score[score.index(59)] = 60
print(score)
#7
print(len(score))
#8
score.sort()
print(score)
print("最大值为",score[-1],"最小值为",score[0])
#9
print(score.pop())
#10
score.append(88)
print(score)
score.remove(88)
print(score)

psum=0
nsum=0
sum=0
for i in range(1,100):
    if i%2!=0:
        psum+=i
    else:
        nsum+=i
sum=psum-nsum
print("1-2+3-4+5 ... 99=%d" %sum)

for i in range(3):
    passwd = input("请输入密码：")
    if passwd == "123456":
        n=int(input("请选择业务，按1取款，按2存款，按3转账："))
        if n == "1":
            print("取款即将开始...")
        elif n == "2":
            print("存款即将开始")
        else:
            print("转账即将开始...")
            break
    elif i<2:
        print("密码错误，请重新输入！")
    else:
        print("密码错误次数超过3次，账户已被锁定！")
'''
score = []
for i in (68,87,92,100,76,88,54,89,76,61):
    score.append(i)
print(score)







