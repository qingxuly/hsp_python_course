# 1、生成一个 [1, 2, 3, 4, 5]
r1 = range(1, 6, 1)
r1 = range(1, 6)
print("r1 = ", list(r1))

# 2、生成一个 [0, 1, 2, 3, 4, 5]
r2 = range(0, 6, 1)
r2 = range(0, 6)
print("r2 = ", list(r2))

# 3、生成一个 r3 =  [1, 3, 5, 7, 9]
r3 = range(1, 10, 2)
print("r3 = ", list(r3))

# 4、输出10句"hello, python"
for i in range(10):
    print("hello, python")
