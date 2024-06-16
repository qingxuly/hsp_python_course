# 随机生成 1-100 的一个数，直到生成了97这个数，看看一共用了多少次
import random

count = 0
while True:
    count += 1
    n = random.randint(1, 100)
    print(n)
    if n == 97:
        break
print("count =", count)
