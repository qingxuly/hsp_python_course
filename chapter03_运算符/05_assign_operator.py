# 赋值运算符
num1 = 10
i = 100
i += 100  # => i = i + 100
print("i =", i)
i -= 100  # => i = i - 100
print("i =", i)
i *= 3  # i = i * 3
print("i =", i)

# 有两个变量，a 和 b，要求将其进行交换，最终打印结果
# 方法1
a = 30
b = 40
print(f"没有交换前 a={a} b={b}")
temp = a
a = b
b = temp
print(f"交换后 a={a} b={b}")

# 方法2
a = 30
b = 40
print(f"没有交换前 a={a} b={b}")
a, b = b, a
print(f"交换后 a={a} b={b}")

# 方法3
a = 30
b = 40
print(f"没有交换前 a={a} b={b}")
a = a + b
b = a - b
a = a - b
print(f"交换后 a={a} b={b}")
