'''
编程实现下列图形的打印

'''
s = 12
for i in range(7):
    for n in range(s):
        print(end=" ")
    s = s - 1
    for m in range(0, i + 1):
        print(" *", end="")

    print("")
