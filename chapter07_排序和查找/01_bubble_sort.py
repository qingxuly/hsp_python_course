# 列表：[24, 69, 80, 57, 13] 有5个元素，使用冒泡排序法使其排成一个从小到大的有序列表。

# 使用sort方法完成排序
num_list = [24, 69, 80, 57, 13]
print("排序前".center(32, "="))
print(f"num_list: {num_list}")

num_list.sort()
print("排序后".center(32, "="))
print(f"num_list: {num_list}")


# 定义函数-完成排序
def bubble_sort(my_list):
    """
    功能；对传入的列表排序-顺序是从小到大
    :param my_list:传入的列表
    :return:无
    """
    # i变量控制多少轮排序
    for i in range(1, len(my_list)):
        # j变量控制比较的次数，同时可以作为比较元素的索引下标
        for j in range(len(my_list) - i):
            # 如果前面的数 > 后面的数，就交换
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        # print(f"第{i}轮排序后的结果 my_list: {my_list}")
    print(f"排序后的结果 my_list: {my_list}")


num_list = [24, 69, 80, 57, 13]
bubble_sort(num_list)
num_list = [24, 69, 80, 57, 13, 0, 900]
bubble_sort(num_list)
