def f1():
    for i in range(1, 5):
        if i == 3:
            return
            # break
            # continue
        print("i =", i)
    print("结束for循环！")


f1()
