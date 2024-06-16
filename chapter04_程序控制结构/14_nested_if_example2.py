# 出票系统：根据淡旺季的月份和年龄，打印票价
month = int(input("请输入当前的月份："))
age = int(input("请输入你的年龄："))

if 4 <= month <= 10:
    if age > 60:
        print("￥20")
    elif age >= 18:
        print("￥60")
    else:
        print("￥30")
else:
    if 18 <= age <= 60:
        print("￥60")
    else:
        print("￥20")
