# 使用while循环实现NxN乘法表的打印。

def NN(s):
    i = 1
    while i <= s:
        n = 1
        while n <= i:
            print("%d*%d=%d" % (i, n, i * n), end="\t")
            n += 1
        print()
        i += 1


N = int(input("请输入打印的乘法表："))
NN(N)
