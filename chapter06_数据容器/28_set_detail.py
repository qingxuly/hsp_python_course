# 不重复元素组成，可以理解成自动去重
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(f"basket: {basket}")

# 无序，也就是你定义元素的顺序和取出的顺序不能保证一致
# 集合底层会按照自己的一套算法来存储和取数据，所以每次取出顺序是不变的
set_a = {100, 200, 300, 400, 500}
print(f"set_a: {set_a}")
print(f"set_a: {set_a}")
print(f"set_a: {set_a}")

set_a = {100, 200, 300, 400, 500}
# print(set_a[0])  # TypeError: 'set' object is not subscriptable

basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
for ele in basket:
    print(ele)

set_b = {}  # 定义空集合不对，这是空字典
set_c = set()  # 创建空集合
print(f"set_b: {type(set_b)}")
print(f"set_c: {type(set_c)}")
