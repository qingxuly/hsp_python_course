# bool类型的基本使用‘
num1 = 100
num2 = 200
if num1 > num2:
    print("num1 > num2")
if num1 < num2:
    print("num1 < num2")

# 表示把 num1 > num2 的结果赋给result变量
result = num1 > num2
print("result =", result)

# 查看result的类型
print("result的类型：", type(result))
print(type(1 > -1))

# 布尔类型可以和其他数据类型进行比较，比如数字、字符串等。在比较时，Python会将True视为1，False视为0。
b1 = False
b2 = True

print(b1 + 10)
print(b2 + 10)

# b1 = 0：表示赋值，把0赋给b1
# b1 == 0：表示判断b1是否和0相等
if b1 == 0:
    print("ok")
if b2 == 1:
    print("Hi")

# 在Python中，非0被视为真值，0被视为假值
if 0:
    print("哈哈")
if -1:
    print("嘻嘻")
if 1.1:
    print("呵呵")
if "哈哈":
    print("啧啧")
if None:
    print("滴滴")

