n1 = 100


def f1():
    # global 关键字标明使用全局变量 n1
    global n1
    n1 = 200
    print(n1)


f1()
print(n1)
