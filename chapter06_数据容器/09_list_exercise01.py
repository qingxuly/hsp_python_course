# 循环从键盘输入5个成绩，保存到列表，并输出。
scores = []
for _ in range(5):
    score = float(input("请输入成绩："))
    scores.append(score)
print(f"成绩情况：{scores}")
