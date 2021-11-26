# 用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）

a = 20
num = [None] * a
for i in range(a):
    num[i] = i + 1
print(num)
rusult = 0

for i in range(len(num)):
    factorial = 1
    for j in range(i + 1):
        factorial = factorial * num[j]
        rusult += factorial
print("结果为", rusult)
