# 演示元组常用操作
tuple_a = (100, 200, 300, 400, 600, 200)
print("tuple_a 元组元素个数：", len(tuple_a))
print("tuple_a 元组最大元素：", max(tuple_a))
print("tuple_a 元组最小元素：", min(tuple_a))

# tuple.count(obj)：统计某个元素在列表中出现的次数
print("100出现的次数：", tuple_a.count(100))
print("200出现的次数：", tuple_a.count(200))

# tuple.index(obj)：从列表中找出某个值第一个匹配项的索引位置
print("200第1次出现在元组的索引：", tuple_a.index(200))
# 如果找不到，会报错：ValueError: tuple.index(x): x not in tuple
# print("1000第1次出现在元组的索引：", tuple_a.index(1000))  # ValueError: tuple.index(x): x not in tuple

# x in s：s中的某项等于x 则结果为True，否则为False
print(300 in tuple_a)  # True
