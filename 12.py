'''
猜数字游戏
1.添加计数打印功能
2.添加次数金币功能和锁定系统功能。
'''
import random

print("开局有3000分，每次猜对就给300，猜错就扣除200，当猜错15回的时候就game over")
life = 3000
i = 0
time = 0
while i < 15:
    a = 0
    Ran = random.randint(1, 20)
    while 1:
        num = input("猜个数吧╮(╯▽╰)╭：")
        num = int(num)
        if num == Ran:
            print("猜对了_(:з」∠)_")
            life = life + 300
            time += 1
            print("已经猜了", time, "次了")
            break
        elif num > Ran:
            print("大了")
            life = life - 200
            i = i + 1
            time += 1
            print("已经猜了", time, "次了")
        else:
            print("小了")
            life = life - 200
            i = i + 1
            time += 1
            print("已经猜了", time, "次了")
        a = a + 1
        if i == 15:
            break
    print("还剩下", life)
print("游戏结束，还剩", life)
