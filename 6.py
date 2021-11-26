#实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）


name = "root"
mima = "admin"


for i in range(0,3):
    n = input("请输入用户名：")
    s = input("请输入密码：")
    if n == name and s == mima:
        print("登录成功")
        break
    else:
        print("gun")
