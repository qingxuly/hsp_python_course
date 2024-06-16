# 定义两个变量int类型，判断二者之和，是否能被3又能被5整除，打印提示信息。
num1 = 10
num2 = 5
if (num1 + num2) % 3 == 0 and (num1 + num2) % 5 == 0:
    print(f"{num1 + num2} 可以被3又能被5整除")
else:
    print(f"{num1 + num2} 不可以被3又能被5整除")
