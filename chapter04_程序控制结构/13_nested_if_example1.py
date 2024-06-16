# 参加歌手比赛，若果初赛成绩大于8.0进入决赛，否则提示淘汰。并且根据性别提示进入男子组或女子组。输入成绩和性别，进行判断和输出信息。
score = float(input("请输入你的成绩："))
if score > 8.0:
    gender = input("请输入你的性别（男|女）：")
    if gender == "男":
        print("男子组决赛")
    else:
        print("女子组决赛")
else:
    print("淘汰")
