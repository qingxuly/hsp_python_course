change = 3
for i in range(1, 4):
    name = input("请输入你的姓名：")
    passwd = int(input("请输入你的密码："))
    change -= 1
    if name == "张无忌" and passwd == 888:
        print("登录成功")
        break
    else:
        print(f"姓名或密码错误，还有{3 - i}次机会")
