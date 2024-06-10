# python 根据该变量使用的上下文在运行时决定的
var1 = 10  # int类型
print(type(var1))
var1 = 1.1  # float类型
print(type(var1))
var1 = 'hello'  # string类型
print(type(var1))

# 在运算的时候，数据类型会向高精度自动转换，float的精度高于int
var2 = 10
var3 = 1.2
var4 = var2 + var3
print("var4=", var4, "var4的类型：", type(var4))
var2 = var2 + 0.1
print("var2=", var2, "var2的类型：", type(var2))
