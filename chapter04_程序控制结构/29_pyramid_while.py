# while实现空心金字塔
i = 0
n = 5
while i < n:
    if i == 0 or i == n - 1:
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
    i += 1
