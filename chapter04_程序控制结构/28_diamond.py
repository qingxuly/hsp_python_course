# 空心菱形
n = 5
for i in range(n):
    if i == 0:
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
for i in range(n - 2, -1, -1):
    if i == 0 or i == n - 1:
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
