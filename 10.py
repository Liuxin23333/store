#一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。

a = -20
s = 3
x = -2
day = 1
while a < 0:
    a += s
    if a >= 0:
        break
    a += x
    if a >= 0:
        break
    day += 1
print(day,"天")
