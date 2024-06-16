n1 = 100


def f1():
    # n1 重新定义了
    n1 = 200
    print(n1)


f1()
print(n1)
