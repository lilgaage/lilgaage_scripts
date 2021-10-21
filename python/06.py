'''
i = float(input("请输入当月利润，以万元为单位："))
if i >=0:
    if i<=10:
        print("当月该发奖金：{}万元".format(i*0.1))
    elif i<=20:
        print("当月该发奖金：{}万元".format(10*0.1+(i-10)*0.075))
    elif i<=40:
        print("当月该发奖金：{}万元".format(10*0.1+10*0.75+(i-20)*0.05))
    elif i<=60:
        print("当月该发奖金：{}万元".format(10*0.1+10*0.75+20*0.05+(i-40)*0.03))
    elif i<=100:
        print("当月该发奖金：{}万元".format(10*0.1+10*0.75+20*0.05+(i-40)*0.03))
    else:
        print("当月该发奖金：{}万元".format(10*0.1+10*0.75+20*0.05+40*0.03+(i-100)*0.01))
else:
    print("请输入的利润不合法！")
'''
import random

deposit = 5000
while True:
    dice1 = random.randint(1, 3)
    dice2 = random.randint(1, 3)
    dice3 = random.randint(1, 3)
    dice = dice1 + dice2 + dice3
    bet = input("请选择押大押小，1为小，2为大，输Q/q停止游戏：")
    if bet == "1" or bet == "2":
        if bet == "1":
            print("您选择押小")
        else:
            print("您选择押大")
        if 3<= dice <=10 and bet == "1" or 11 <= dice <=18 and bet == "2":
            deposit=deposit*2
            print("骰子点数为：{}".format(dice))
            print("恭喜您押中了！现有余额为：{}".format(deposit))
        else:
            deposit=deposit/2
            print("骰子点数为：{}".format(dice))
            print("好可惜，没有押中，再接再厉吧！现有余额为：{}".format(deposit))
            if deposit < 800:
                add = input("请选择是否充值1000元，1为确认充值，0为不充值：")
                if add == "1" or add == "0":
                    if add == "1":
                        deposit = deposit + 1000
                        print("现有余额为：{}".format(deposit))
                    else:
                        print("您的余额不足，游戏停止！")
                        break
                else:
                    print("输入不合法，请重新输入！")
                    #充值输入不合法时重新进入循环押金会减少一半，所以加上
                    deposit = deposit * 2
    elif bet == "Q" or bet == "q":
        print("游戏停止，祝您生活愉快！")
        break
    else:
        print("输入不合法，请重新输入！")

