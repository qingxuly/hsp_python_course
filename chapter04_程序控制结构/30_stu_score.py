"""
统计3个班成绩情况，每个班有5名同学，要求：
1、求出每个班的平均分和所有班的平均分，学生的成绩从键盘输入
2、统计三个班及格人数

编程思想：（1）化繁为简（2）先死后活【先考虑3个班，每个班5名同学】
# 化繁为简
1. 先统计1个班成绩情况，求出一个班的平均分
2. 统计3个班成绩情况，求出各个班的平均分、所有班级的平均分和 及格人数
"""

total = 0.0
pass_num = 0
class_num = 3
student_num = 5
# 循环地处理3个班级的成绩
for j in range(class_num):
    # 统计一个班成绩情况
    sum = 0.0
    for i in range(student_num):
        score = float(input(f"请输入第{j + 1}班的 第{i + 1}个学生的成绩："))
        # 判断是否及格
        if score >= 60.0:
            pass_num += 1
        sum += score
    print(f"第{j + 1}班级的情况：平均分{sum / 5}")
    total = total + sum
print(f"所有班级的平均分 {total / (student_num * class_num)}，及格人数 {pass_num}")
