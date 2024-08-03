import random

list_num = []
for _ in range(10):
    list_num.append(random.randint(1, 100))
print("list_num", list_num)


def bubble_sort(my_list):
    for i in range(1, len(my_list)):
        for j in range(len(my_list) - i):
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]


bubble_sort(list_num)
print("list_num", list_num)
