# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。

lst = list(eval(input("请输入10个整数（用逗号隔开）：")))
avg = sum(lst)/len(lst)
a = sum(lst)
v = max(lst)
print("最大值：",v)
print("平均值：",avg)
print("和：",a)