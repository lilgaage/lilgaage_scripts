print("7. ATM机操作模拟")
'''
    模仿ATM机常用操作（登录，取款，转账，存款，查询，退卡）
    Atm机，验证密码，若三次密码都不对，则强制退出系统；
    成功的话，调用相关操作；
'''

# 默认账户金额
money = 10000
# 输错密码的次数
count = 0
while count < 3:
    # pwd - --银行卡密码
    pwd = input("请输入你的银行卡密码：")
    if pwd == "123456":
        print("密码正确!")
        print("-" * 30)
        b = True  # 循环条件
        # 密码输入成功后循环操作，直到选择退卡结束循环
        while b:
            print("请选择您要进行的操作：")
            print("0：取款            1：转账")
            print("2：存款            3：查询")
            print("                  4：退卡")
            print("-" * 30)
            # num---选择的操作
            num = int(input())
            # 取款操作
            if num == 0:
                # x - --取款金额
                x = int(input("请输入您要取款的金额："))
                # 只能取款100的整数倍
                if x <= 0 or x % 100 != 0 or x > 5000:
                    print("请输入合法的金额（100的正整数倍,且不大于5000）！")
                    print("-" * 30)
                elif money < x:
                    print("您的账户余额不足，取款失败，请重新输入！")
                else:
                    # 账户上的钱 - 要取的钱
                    money -= x
                    print("取款成功，请取走您的钞票！")
                    print("-" * 30)
            # 转账操作
            elif num == 1:
                # acc---转账账户
                acc = input("请输入您要转入的账户：")
                # 关于账户的判断，判断是不是由纯数字构成，以及长度(未实现）
                # x---转账金额
                x = float(input("请输入您要转入的金额："))
                if money < x:
                    print("您的账户余额不足，转账失败！")
                    print("-" * 30)
                else:
                    money -= x
                    print("转账成功！")
                    print("您向账户{}转账{}元人民币".format(acc, x))
                    print("-" * 30)
                '''
                # 默认一个转账账户，用于判断账户输入不正确的情况
                account = "120110119"
                if acc != account:
                    print("您输入的转入账户不正确，转账失败！")
                    print("-" * 30)
    
                elif money < x:
                    print("您的账户余额不足，转账失败！")
                    print("-" * 30)
    
                else:
                    money -= x
                    print("转账成功！")
                    print("-" * 30)
                '''
            # 存款操作
            elif num == 2:
                # 这里存款金额手动输入,x----存款金额
                x = int(input("请输入您要存款的金额："))
                if x <= 0 or x % 100 != 0 or x > 10000:
                    print("请输入合法的金额（100的正整数倍,单次最多放100张）！")
                    print("-" * 30)
                else:
                    money += x
                    print("存款成功！")
                    print("-" * 30)
            # 查询操作
            elif num == 3:
                print("您的账户余额为：", money)
                print("-" * 30)
            # 退卡操作
            elif num == 4:
                print("您已成功退出！")
                print("-" * 30)
                # 结束内循环
                b = False
                # 结束外循环
                count = 3
                print("-" * 30)
            # 其他选项
            else:
                print("输入错误，请选择正确的操作！")
                print("-" * 30)

    # 密码输错时的处理
    else:
        # 错误计数 + 1
        count += 1
        if count == 3:
            print("***密码错误，您的卡已被没收，请到人工营业厅取回您的卡***")
            print("-" * 30)
        else:
            print("密码错误，您还有" + str(3 - count) + "次机会！")

print("******感谢您的光临，欢迎下次再来********")
