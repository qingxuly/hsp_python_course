# 它会终结最近的外层循环，如果循环有可选的else子句，也会跳过该子句。
count = 0
while True:
    print("hi")
    count += 1
    if count == 3:
        break
    while True:
        print("ok")
        break
else:
    print("hello")

# 如果一个for循环被break所终结，该循环的控制变量会保持其当前值。
nums = [1, 2, 3, 4, 5]
for i in nums:
    if i > 3:
        break
print("i =", i)