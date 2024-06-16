# 如果外层循环次数为m次，内层为n次，则内层循环体实际上需要执行m*n次。
for i in range(2):
    for j in range(3):
        print("i=", i, "j=", j)
