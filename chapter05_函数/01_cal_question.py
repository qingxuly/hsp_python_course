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
