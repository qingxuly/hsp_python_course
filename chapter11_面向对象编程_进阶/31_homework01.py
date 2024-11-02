class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __str__(self):
        return f'{self.name}, {self.age}, {self.job}'


p1 = Person('smith', 21, 'python')
p2 = Person('king', 30, 'java')
p3 = Person('tom', 40, '老师')

my_list = [p1, p2, p3]
for p in my_list:
    print(p)

# 实现按照age从大到小排序。

# 解决方案1：冒泡排序
# def bubble_sort(my_list: list[Person]):
#     for i in range(1, len(my_list)):
#         # j变量控制比较的次数，同时可以作为比较元素的索引下标
#         for j in range(len(my_list) - i):
#             # 如果前面的年龄 < 后面的年龄，就交换
#             if my_list[j].age < my_list[j + 1].age:
#                 my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]


# bubble_sort(my_list)
# print("排序后".center(50, '='))
#
# for p in my_list:
#     print(p)


# 解决方案2：直接使用列表的 .sort
# key=lambda ele: ele.age 表示指定按照列表元素的age属性进行排序。
# reverse=True 表示倒序
print("排序后".center(50, '='))
my_list.sort(key=lambda ele: ele.age, reverse=True)
for p in my_list:
    print(p)
