'''
n=True
if n:
	print("去长沙")
age=int(input("请输入您的年龄："))
if age>=21:
	print("去")
else:
	print("不去")

age=int(input("请输入一个整数："))
if 1<=age<=120:
	print("该年龄输入正确！")
else:
	print("您的输入有误！")

age=int(input("请输入您的年龄："))
if age>150 or age<0:
	print("您的输入有误！")
elif age<12:
	print("儿童")
elif age<38:
	print("青少年")
elif age<60:
	print("中年")
else:
	print("老年")

num=int(input("请输入一个数字："))
if 1<=num<=7:
	if num==1:
		print("星期一")
	elif num==2:
		print("星期二")
	elif num==3:
		print("星期三")
	elif num==4:
		print("星期四")
	elif num==5:
		print("星期五")
	elif num==6:
		print("星期六")
	else:
		print("星期日")
else:
	print("您的输入不合法！")


i=1
while i<=5:
	print("第%d次说我爱你" %i)
	i+=1
print("end......")

i=1
sum=0
while i<=10:
	if i%2==0:
		sum+=i
	i+=1
print("10以内2的倍数和=",sum)

i=1
sum=0
while i<=100:
	if i%3==0:
		sum+=i
	i+=1
print("100以内3的倍数和=",sum)

i=0
sum=0
while i<=100:
	sum+=i
	i+=3
print("100以内3的倍数和=",sum)

i=0
while i<=100:
	if i%3==0:
		i+=1
		continue #跳出本次循环
	print(i)
	i+=1

while True:
	n=int(input("请输入一个整数，输入0结束循环："))
	if n==0:
		break
	print(n**2)


i=1
count=0
while i<=100:
	#个位不包含9，十位也不包含9
	if i%10==9 or i//10==9:
		i+=1
		continue #跳出本次循环
	count+=1 
	print(i,end="\t")
	if count%5==0: #输出5个换一行
		print() #换行
	i+=1
print()


i=0
while i<5:
	j=0
	while j<=i:
		print("*",end=" ")
		j+=1
	print()
	i+=1


for i in range(True):
	i=int(input("请输入一个整数，输入0结束循环："))
	if i==0:
		break
	print(i**2)

count=0
for i in range(101):
	if i%10==9 or i//10==9:
		continue
	count+=1 
	print(i,end="\t")
	if count%5==0:
		print() 
print()



month=int(input("请输入月份："))
if 1<=month<=12:
	if 3<=month<=5:
		print("spring")
	elif 6<=month<=8:
		print("summer")
	elif 9<=month<=11:
		print("autumn")
	else:
		print("winter")
else:
	print("您输入的月份有误！")

i=1
product=1
while i<=10:
	product*=i
	i+=1
print("10! =",product)


for n in range(100,1000):
	i=n//100
	j=n//10%10
	k=n%10
	if i**3+j**3+k**3==n:
		print(n)

sum=0
for i in range(5):
	score=int(input("请输入成绩:"))
	sum+=score
	avg=sum/5
print("该同学平均成绩为",avg)

sum=0
for i in range(101):
	if i%7!=0 and i%3!=0:
		sum+=i
print("100以内不是7的倍数也不是3的倍数的和是",sum)

count=0
for i in range(1,101):
	if i%7==0:
		count+=1
		print(i,end="\t")
		if count%5==0:
			print()

i=1
while i<=9:
	j=1
	while j<=i:
		print("%d*%d=%d" %(j,i,i*j),end=" ")
		j+=1
	print()
	i+=1

while True:
	num=input("请输入一个0~10之间的整数,输入Q/q退出循环：")
	if num=="q" or num=="Q":
		break
	elif num=="1":
		print("壹")
	elif num=="2":
		print("贰")
	elif num=="3":
		print("叁")
	elif num=="4":
		print("肆")
	elif num=="5":
		print("伍")
	elif num=="6":
		print("陆")
	elif num=="7":
		print("柒")
	elif num=="8":
		print("捌")
	elif num=="9":
		print("玖")
	elif num=="10":
		print("拾")

count=0
for i in range(101):
	if i%10==6 or i//10==6 or i%6==0:
		continue
	count+=1 
	print(i,end="\t")
	if count%5==0:
		print() 
 '''
for i in range(3):
	name=input("请输入用户名：")
	passwd=input("请输入密码：")
	if name=="root" and passwd=="test123":
		print("登陆成功")
		break
	elif i<2:
		print("登陆失败，请重新输入！")
	else:
		print("错误次数超过3次，请明天再试！")















