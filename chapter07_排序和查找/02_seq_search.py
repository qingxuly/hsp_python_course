names_list = ["白眉鹰王", "金毛狮王", "紫衫龙王", "青翼蝠王"]
find_name = "金毛狮王"


# 使用list.index完成查找
res_index = names_list.index(find_name)
print("res_index:", res_index)


def seq_search(my_list, find_val):
    """
    功能：顺序查找指定的元素
    :param my_list: 传入的列表（即要查找的列表）
    :param find_val: 要查找的值/元素
    :return: 如果查找到则返回对应的索引下标，否则返回-1
    """
    find_index = -1
    for i in range(len(my_list)):
        if my_list[i] == find_val:
            print(f"恭喜，找到对应的值{find_val} 下标是{i}")
            break
    else:
        print(f"没有找到对应的值{find_val}")
    return find_index


res_index = seq_search(names_list, find_name)
print("res_index:", res_index)


# 编写查找函数，把满足查询条件的元素的下标都返回
def seq_search2(my_list, find_val):
    find_index = []
    for i in range(len(my_list)):
        if my_list[i] == find_val:
            # 将找到的下标添加到find_index
            find_index.append(i)
    return find_index


names_list = ["白眉鹰王", "金毛狮王", "紫衫龙王", "金毛狮王", "青翼蝠王"]
find_name = "金毛狮王"
res_index = seq_search2(names_list, find_name)
print("res_index:", res_index)
