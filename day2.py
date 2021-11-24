'''
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：如果键盘输入大于随机数弹出友好提示信息“猜大了”，猜小了
起始金额  5000 才对一次给300 猜错扣除100 猜错15次结束
'''
import random

money = 5000
a = 0
while a < 15:

    Ran = random.randint(1, 10000)
    num = int(input("请输入一个数字："))
    if num == Ran:
        print("老铁牛批666")
        money = money + 10000
        a = 0
        print(money)
    elif num > Ran:
        print("老铁牛批就差一点了，再来一次")
        money = money - 200
        a += 1
        print(money)
    elif num < Ran:
        print("老铁牛批就差一点点点了，再来一次")
        money = money - 200
        a += 1
        print(money)

print("真拉啊老铁别猜了换人吧")

