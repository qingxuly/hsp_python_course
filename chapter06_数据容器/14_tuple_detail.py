# 注意事项和使用细节
tuple_a = ()
tuple_b = tuple()
print(f"tuple_a : {tuple_a}")
print(f"tuple_b : {tuple_b}")

tuple_c = (100, "jack", 4.5, True, "jack")
print(f"tuple_c : {tuple_c}")

# 嵌套元组
tuple_d = (100, "tom", ("天龙八部", "笑傲江湖", 300))
print(f"tuple_d : {tuple_d}")

tuple_e = (1, 2.1, "hsp")

print(tuple_e[1])
# 索引越界
# print(tuple_e[3])  # IndexError: tuple index out of range

tuple_f = (1, 2.1, "hsp")

# 不能修改
# tuple_f[2] = "python"  # TypeError: 'tuple' object does not support item assignment

tuple_g = (1, 2.1, "hsp", ["jack", "tom", "mary"])
print(tuple_g[3])
print(tuple_g[3][0])

# 修改
tuple_g[3][0] = "HSP"
print(tuple_g)
# 不能替换整个列表元素
# tuple_g[3] = [10, 20]  # TypeError: 'tuple' object does not support item assignment

# 删除
del tuple_g[3][0]
print(tuple_g)

# 增加
tuple_g[3].append("smith")
print(tuple_g)

tuple_h = (1, 2.1, "hsp", ["jack", "tom", "mary"])
print(tuple_h[-2])

tuplg_i = (100,)
print(f"tuplg_i : {tuplg_i}", type(tuplg_i))
# 输出 tuplg_i : (100,) <class 'tuple'>

tuplg_j = (100)
print(f"tuplg_j : {tuplg_j}", type(tuplg_j))
# 输出 tuplg_j : 100 <class 'int'>

