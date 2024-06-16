# 自定义cry 函数，输出“喵喵喵”
# 定义函数
def cry():
    print("喵喵喵")


# 调用函数
cry()


# 自定义cal01 函数，可以计算从 1+...+1000的结果
def cal01():
    total = 0
    for i in range(1, 1001):
        total += i
    print("total =", total)


cal01()


# 自定义cal02 函数，该函数可以接收一个n，计算从 1+...+n 的结果
def cal02(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("total =", total)


# (10) 表示我调用函数时，出入了实参 10，即把10赋给了形参n：n = 10
cal02(10)


# 自定义get_sum 函数，可以计算两个数的和，并返回结果
def get_sum(num1, num2):
    return num1 + num2


"""
1.调用get_sum(10, 50) 调用get_sum
2.(10, 50) 表示传入了两个实参10, 50，把10赋给num1，把50赋给num2
3.result 就是接收get_sum 函数返回的结果
"""
result = get_sum(20, 30)
print("result =", result)


# 使用函数解决计算问题
def cal04():
    n1 = float(input("请输入第一个数："))
    n2 = float(input("请输入第二个数："))
    oper = input("请输入运算符 + - * / ：")
    res = 0.0
    if oper == "+":
        res = n1 + n2
    elif oper == "-":
        res = n1 - n2
    elif oper == "*":
        res = n1 * n2
    elif oper == "/":
        res = n1 / n2
    else:
        print("输入的运算符错误")

    print(n1, oper, n2, "=", res)


cal04()
