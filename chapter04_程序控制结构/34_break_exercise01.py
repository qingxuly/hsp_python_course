# 1 - 100以内的求和，求出当和第一次大于20的当前控制循环的变量是多少。

sum = 0
for i in range(1, 101):
    sum += i
    if sum > 20:
        break
print(i)
