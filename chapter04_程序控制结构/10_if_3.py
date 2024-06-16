# 参加Python考试，根据得分获得对应奖励
score = int(input("请输入成绩[整数]："))
if score >= 0 and score <= 100:
    if score == 100:
        print("BWM")
    elif score > 80 and score <= 99:
        print("iphone13")
    elif score >= 60 and score <= 80:
        print("ipad")
    else:
        print("none")
else:
    print(score, "不在0~100")
