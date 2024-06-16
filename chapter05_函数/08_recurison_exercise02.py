# 猴子吃桃
"""
day == 10，桃子树：1
day == 9, 桃子树：(day10的桃子树+1）*2
...
"""


def peach(day):
    if day == 10:
        return 1
    else:
        return (peach(day + 1) + 1) * 2


print(peach(1))
