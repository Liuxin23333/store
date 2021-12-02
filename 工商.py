from random import randint
from typing import Dict, Any

print("*********************************")
print("*\t\t中国工商银行\t\t\t\t*")
print("*\t\t账户管理系统\t\t\t\t*")
print("*\t\t\tV1.0\t\t\t\t*")
print("*********************************")
print("*\t\t\t\t\t\t\t\t*")
print("*1.开户\t\t\t\t\t\t\t*")
print("*2.存钱\t\t\t\t\t\t\t*")
print("*3.取钱\t\t\t\t\t\t\t*")
print("*4.转账\t\t\t\t\t\t\t*")
print("*5.查询\t\t\t\t\t\t\t*")
print("*6.Bye！\t\t\t\t\t\t*")
print("*********************************")

bank = {}
yinhang = "ICBC"


def useradd():
    account = str(randint(10000000, 99999999))
    username = input("请输入您的名字：")
    password = input("请输入您的密码：")
    country = input("请输入您的国家：")
    province = input("请输入您的省份：")
    street = input("请输入您的街道：")
    menhao = input("请输入您的门牌号：")
    pan = bankadd(account, username, password, country, province, street, menhao)
    if pan == 1:
        print("开户成功")
        print("")
        info = '''
                *******ICBC*******
                    1.账号：%s
                    2.姓名：%s
                    3.密码：******
                    4.国家：%s
                    5.省份：%s
                    6.街道：%s
                    7.门牌号：%s
                    8.余额：%s
                    9.开户行：中国工商银行
        
        '''
        print(info % (account, username, country, province, street, menhao, bank[account]["money"]))
    elif pan == 2:
        print("账号重复")
    elif pan == 3:
        print("用户库已满")


def bankadd(account, username, password, country, province, street, menhao, ):
    if account in bank:
        return 2
    elif len(bank) > 100:
        return 3
    bank[account] = {
        "account": account,
        "username": username,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "menhao": menhao,
        "money": 0,
        "yinhang": yinhang
    }
    return 1


def cun():
    account_cun = input("请输入您的存钱账号：")
    money_cun = int(input("请输入您要存的金额："))
    pan2 = cunadd(account_cun, money_cun)
    if pan2 == True:
        print("存钱成功，当前您的余额为：", bank[account_cun]["money"])
    elif pan2 == False:
        print("请输入正确的账号")


def cunadd(account_cun, money_cun):
    if account_cun in bank:
        bank[account_cun]["money"] += money_cun
        return True
    else:
        return False


def qu():
    account_qu = input("请输入您的取钱账号：")
    password_qu = input("请输入您的密码：")
    money_qu = int(input("请输入您要取的金额："))
    pan3 = quadd(account_qu, password_qu, money_qu)
    if pan3 == 1:
        print("请输入正确的账号")
    if pan3 == 2:
        print("密码错误")
    if pan3 == 3:
        print("余额不足")
    if pan3  == 0:
        bank[account_qu]["money"] -= money_qu
        print("取款成功，您当前的余额为：", bank[account_qu]["money"])


def quadd(account_qu, password_qu, money_qu):
    if account_qu in bank:
        if password_qu == bank[account_qu]["password"]:
            if int(bank[account_qu]["money"]) >= int(money_qu):
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

def zhuan():
    account_zhuan = input("请输入您的转出账号：")
    password_zhuan = input("请输入密码：")
    account_zhuan2 = input("请输入您的转入账号：")
    money_zhuan = int(input("请输入您要转的金额："))
    pan4 = zhuanadd(account_zhuan,password_zhuan,account_zhuan2,money_zhuan)
    if pan4 == 0:
        bank[account_zhuan]["money"] -= money_zhuan
        print("转账成功，您当前的余额为：",bank[account_zhuan]["money"])
    if pan4 == 1:
        print("请输入正确的账号")
    if pan4 == 2:
        print("请输入正确的密码")
    if pan4 == 3:
        print("余额不足")

def zhuanadd(account_zhuan,password_zhuan,account_zhuan2,money_zhuan):
    if account_zhuan in bank and account_zhuan2 in bank:
        if password_zhuan in bank[account_zhuan]["password"]:
            if bank[account_zhuan]["money"] >= money_zhuan:
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1



def cha():
    account_cha = input("请输入您要查询的账号：")
    password_cha = input("请输入密码：")
    if account_cha in bank:
        if password_cha == bank[account_cha]["password"]:
            info = '''
                    *******ICBC*******
                    1.当前账号：%s
                    2.密码：******
                    3.余额：%s
                    4.居住地址：%s%s%s%s
                    5.开户行：中国工商银行
            
            '''
            print(info %(account_cha,bank[account_cha]["money"],bank[account_cha]["country"],
                bank[account_cha]["province"],bank[account_cha]["street"],bank[account_cha]["menhao"]))
        else:
            print("密码错误")
    else:
        print("请输入正确的账号")

while True:
    account_input = input("请输入您的操作：")
    if account_input == "1":
        useradd()

    elif account_input == "2":
        cun()

    elif account_input == "3":
        qu()

    elif account_input == "4":
        zhuan()

    elif account_input == "5":
        cha()

    elif account_input == "6":
        print("Bye!")
        break

    else:
        print("gun")

