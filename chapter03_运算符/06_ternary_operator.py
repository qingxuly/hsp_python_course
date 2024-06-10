# 三元运算符
# 获取两个数的最大值
a = 10
b = 80
max = a if a > b else b
print(f"max={max}")

# 获取三个数的最大值
a = 10
b = 30
c = 20
max1 = a if a > b else b
max2 = max1 if max1 > c else c
print(f"max2={max2}")

# 可以支持嵌套使用，但是可读性差，不推荐
max = (a if a > b else b) if (a if a > b else b) > c else c
print(f"max={max}")
