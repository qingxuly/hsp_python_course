# 打印 1~100 之间所有是9的倍数的整数，统计个数及总和
i = 1
max_num = 100
count = 0
sum = 0

while i <= max_num:
    if i % 9 == 0:
        print(i)
        count += 1
        sum += i
    i += 1
print("count:", count)
print("sum:", sum)
