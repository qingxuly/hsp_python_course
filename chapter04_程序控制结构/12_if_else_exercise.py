# 婚嫁
height = float(input("请输入身高（cm）："))
money = float(input("请输入财富（万）："))
handsome = (input("请输入颜值（帅，不帅）："))

if height > 180 and money > 1000 and handsome == "帅":
    print("我一定要嫁给他")
elif height > 180 or money > 1000 or handsome == "帅":
    print("嫁吧，比上不足，比下有余")
else:
    print("不嫁")
