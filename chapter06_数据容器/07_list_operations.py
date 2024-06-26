# 演示列表常用操作
list_a = [100, 200, 300, 400, 600]
print("list_a 列表元素个数：", len(list_a))
print("list_a 列表最大元素：", max(list_a))
print("list_a 列表最小元素：", min(list_a))

# list.append(obj)：在列表末尾添加新的对象
list_a.append(900)
print("list_a：", list_a)

# list.count(obj)：统计某个元素在列表中出现的次数
print("100出现的次数：", list_a.count(100))

# list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list_b = [1, 2, 3]
list_a.extend(list_b)
print("list_a：", list_a)

# list.index(obj)：从列表中找出某个值第一个匹配项的索引位置
print("300第1次出现在序列的索引是：", list_a.index(300))
# 如果找不到，会报错：ValueError
# print("1000第1次出现在序列的索引是：", list_a.index(1000))  # ValueError: 1000 is not in list

# list.insert(index, obj)：将对象插入列表
list_a.insert(1, 666)
print("list_a：", list_a)

# list.pop([index=-1])：移除列表中的一个元素（默认最后一个元素），并返回该元素的值
print(list_a.pop())
print("list_a：", list_a)

# list.remove(obj)：移除列表中某个值的第一个匹配项                                             |
list_a.remove(666)
print("list_a：", list_a)

# list.reverse()：反向列表中元素
list_a.reverse()
print("list_a：", list_a)

# list.sort(key=None, reverse=False)：对原列表进行排序
list_a.sort()
print("list_a：", list_a)

# list.copy()：复制列表
list_c = list_a.copy()
print("list_c：", list_a)

# list.clear()：清空列表
list_a.clear()
print("list_a：", list_a)
