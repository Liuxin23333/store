# 编程实现99乘法表的倒叙打印

i = 9
while i < 10 and i > 0:
    o = 1
    while o <= i:
        print("%d*%d=%d" % (i, o, i * o), end="\t")
        o += 1

    print("")
    i = i - 1
