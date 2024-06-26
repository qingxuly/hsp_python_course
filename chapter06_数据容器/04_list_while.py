# 内置函数 len()可以返回对象的长度（元素个数）。
list_color = ["red", "green", "blue", "yellow", "white", "black"]
index = 0
while index < len(list_color):
    print(f"第{index + 1}个元素是：{list_color[index]}")
    index += 1
