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


def binary_search(my_list, find_val):
    left_index = 0
    right_index = len(my_list) - 1
    find_index = -1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if my_list[mid_index] < find_val:
            right_index = mid_index - 1
        elif my_list[mid_index] > find_val:
            left_index = mid_index + 1
        else:
            find_index = mid_index
            break
    return find_index


res_index = binary_search(list_num, 8)
if res_index == -1:
    print("Not Found")
else:
    print(f"找到数，对应的下标{res_index}")
