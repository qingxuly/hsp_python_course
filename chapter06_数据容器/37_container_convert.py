str_a = "hello"
list_a = ["jack", "tom", "mary"]
tuple_a = ("hsp", "tim")
set_a = {"red", "green", "blue"}
dict_a = {"0001": "小倩", "0002": "黑山老妖"}
# list([iterable])：iterable可以是序列、支持迭代的容器或其他可迭代对象，<br />将指定的容器转成列表
print(list(str_a))
print(list(tuple_a))
print(list(set_a))
print(list(dict_a))
print("-" * 60)

# str(容器)：将制定的容器转为字符串
print(str(list_a))
print(str(tuple_a))
print(str(set_a))
print(str(dict_a))
print("-" * 60)

# tuple([iterable])：iterable可以是序列、支持迭代的容器或其他可迭代对象，<br />将指定的容器转成元组
print(tuple(str_a))
print(tuple(list_a))
print(tuple(set_a))
print(tuple(dict_a))
print("-" * 60)

# set([iterable])：iterable可以是序列、支持迭代的容器或其他可迭代对象，<br />将指定的容器转成集合
print(set(str_a))
print(set(list_a))
print(set(tuple_a))
print(set(dict_a))
