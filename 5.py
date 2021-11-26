'''
有以下两个数，使用+，-号实现两个数的调换。
                               A=56
                               B=78
实现效果：
                               A=78
                               B=56
'''
A = 56
B = 78
C = 0
print("A=",A)
print("B=",B)
while True:
    n = input("请输入操作命令：")
    if n == "+" or n == "-":
        C = A
        A = B
        B = C
        print("A=",A)
        print("B=",B)
    else:
        print("gun")
