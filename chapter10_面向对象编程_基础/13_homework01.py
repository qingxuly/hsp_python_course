# 1、编写A01，定义方法max_lst，实现求某个float 列表list = [1.1, 2.9, -1.9, 67.9]的最大值，并返回。
"""
    思路分析
    1. 类名：A01
    2. 方法：max_lst(self, lst), 功能：返回列表的最大值
"""


class A01:
    def max_lst(self, lst):
        return max(lst)


# 测试
a = A01()
print("最大值：", a.max_lst([1.1, 2.9, -1.9, 67.9]))

