num_list = [1, 8, 10, 89, 1000, 1234]


def binary_search(my_list, find_val):
    """
    功能：完成二分查找
    :param my_list: 要查找的列表（该列表是由大小顺序）
    :param find_val: 要查找的元素/值
    :return:  如果找到返回对应的下标，若果没有找到，返回-1
    """
    left_index = 0
    right_index = len(my_list) - 1
    find_index = -1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        # 如果mid_index>find_val，则到如果mid_index左边查找
        if my_list[mid_index] > find_val:
            right_index = mid_index - 1
        # 如果mid_index<find_val，则到如果mid_index右边查找
        elif my_list[mid_index] < find_val:
            left_index = mid_index + 1
        else:
            find_index = mid_index
            break
    return find_index


res_index = binary_search(num_list, 1)
if res_index == -1:
    print("没有找到该数")
else:
    print(f"找到数，对应的下标{res_index}")

num_list = [1234, 1000, 89, 10, 8, 1]
