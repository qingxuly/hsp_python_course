# 定义列表 list_name = ["Jack", "Lisa", "Hsp", "Paul", "Smith", "Kobe"]
# 取出前三个名字；取出后三个名字，，并且保证原来顺序
list_name = ["Jack", "Lisa", "Hsp", "Paul", "Smith", "Kobe"]
list_name_f = list_name[0:3:1]
list_name_b = list_name[-1:-4:-1]
list_name_b.reverse()
print(f"前三个名字：{list_name_f}")
print(f"后三个名字：{list_name_b}")
