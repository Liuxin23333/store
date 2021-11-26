# 实现输入10个数字，并打印10个数的求和结果

print("请输入10个整数：")
a = 1
Sum = 0
while a < 11:
    n = int(input(""))
    a += 1
    Sum += n

print("这10个数的和为：", Sum)
