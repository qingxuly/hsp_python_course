s_history = {"小明", "张三", "李四", "王五", "Lily", "Bob"}
s_politic = {"小明", "小花", "小红", "二狗"}
s_english = {"小明", "Lily", "Bob", "Davil", "李四"}

# 求选课学生共有多少人
total = s_history.union(s_politic).union(s_english)
print("总人数：", len(total))

# 求只选了第一个学科（history）的学生数量和学生姓名
total_history = s_history.difference(s_politic).difference(s_english)
print("数量：", len(total_history), "姓名：", total_history)

# 求只选了一门学科的学生数量和学生姓名
total_politic = s_politic.difference(s_english).difference(s_history)
total_english = s_english.difference(s_history).difference(s_politic)
total_one = total_history.union(total_politic).union(total_english)
print("数量：", len(total_one), "姓名：", total_one)

# 求选了三门学科的学生数量和学生姓名
total_three = s_history.intersection(s_politic).intersection(s_english)
print("数量：", len(total_three), "姓名：", total_three)
