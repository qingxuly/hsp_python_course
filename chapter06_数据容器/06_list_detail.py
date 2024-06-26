list1 = []
list2 = list()

print(list1, type(list1))
print(list2, type(list2))

list3 = [100, "jack", 4.5, True, "jack"]
print(list3)

# 嵌套列表
list4 = [100, "tom", ["天龙八部", "笑傲江湖", 300]]
print(list4)

list5 = [1, 2]
# print(list5[2])  # IndexError: list index out of range

list6 = ["red", "green", "blue", "yellow", "white", "black"]
print(list6[-1])
print(list6[-6])
# 依然不能索引越界
# print(list6[-7])  # IndexError: list index out of range

# 通过`列表[索引]=新值`对数据进行更新，使用`列表.append(值)`方法来添加元素，使用`del语句`来删除列表的元素，注意不能超出有效索引范围。
list_a = ["天龙八部", "笑傲江湖"]
print("list_a:", list_a)
list_a[0] = "雪山飞狐"
print("list_a:", list_a)
list_a.append("倚天屠龙")
print("list_a:", list_a)
del list_a[1]
print("list_a:", list_a)

# 列表是可变序列（要注意其使用特点）。
list1 = [1, 2.1, "hsp"]
print(f"list1: {list1} 地址：{id(list1)} 第三个元素地址 {id(list1[2])}")
list1[2] = "python"
print(f"list1: {list1} 地址：{id(list1)} 第三个元素地址 {id(list1[2])}")

# 扩展一下，列表在赋值时的特点
list1 = [1, 2.1, "hsp"]
list2 = list1
list2[0] = 500
print("list2:", list2)
print("list1:", list1)


# 列表在函数传参时的特点
def f1(l):
    l[0] = 100
    print("l的id:", id(l))


list10 = [1, 2.1, 200]
print("list10的id:", id(list10))
f1(list10)
print("list10:", list10)
