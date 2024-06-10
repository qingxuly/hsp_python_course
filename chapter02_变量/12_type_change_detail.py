# 显示类型转换注意事项
n1 = 100
n2 = 123.65
print(str(n1))
print(str(n2))

print(float(n1))
print(int(n2))

n3 = "12.56"
print(float(n3))
# print(int(n3))  # ValueError: invalid literal for int() with base 10: '12.56'

n4 = "hello"  # ValueError: could not convert string to float: 'hello'
# print(float(n4))
# print(int(n4))

i = 10
j = float(i)
print("i的值：", i, "i的类型：", type(i))
print("j的值：", j, "j的类型：", type(j))

k = str(i)
print("i的值：", i, "i的类型：", type(i))
print("k的值：", k, "k的类型：", type(k))
