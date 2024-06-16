# 打印空心金字塔
"""
思路分析
    - 先死后活
    1、先不考虑层数的变化，嘉定就是5层，后面做活
    - 化繁为简
    1、打印矩形
    2、打印直角三角形
    3、打印金字塔
    4、打印空心金字塔
"""

total_level = 5
for i in range(total_level):
    for j in range(total_level):
        print("*", end="")
    print("")

total_level = 5
for i in range(total_level + 1):
    for j in range(i):
        print("*", end="")
    print("")

total_level = 5
for i in range(total_level + 1):
    for k in range(total_level - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print("")

# 总层数
total_level = 5
# i 控制层数
for i in range(1, total_level + 1):
    # k 控制输出空格数
    for k in range(total_level - i):
        print(" ", end="")
    # j 控制每层输出的*号个数
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i == total_level:
            print("*", end="")
        else:
            print(" ", end="")
    # 每层输出后，换行
    print("")
