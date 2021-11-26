# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）

a = int(input("请输入第一个边长："))
b = int(input("请输入第二个边长："))
c = int(input("请输入第三个边长："))
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("等边")
    elif a == b or b == c or a == c:
        print("等腰")
    elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("∟")
    else:
        print("普三")
else:
    print("gun")
