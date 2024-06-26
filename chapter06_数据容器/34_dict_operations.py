dict_a = {"one": 1, "two": 2, "three": 3}

# len(d)：返回字典d中的项数
print(f"dict_a元素个数：{len(dict_a)}")

# d[key]：返回d中以key为键的项。如果映射中不存在key则会引发KeyError
print(f"key为three对应的value：{dict_a["three"]}")
# print(f"key为four对应的value：{dict_a["four"]}")  # KeyError: 'four'

# d[key] = value：将d[key]设为value，如果key已经存在，则是修改value，如果key没有存在，则是增加key-value
dict_a["one"] = "第一"
print(f"dict_a: {dict_a}")
dict_a["four"] = 4
print(f"dict_a: {dict_a}")

# del d[key]：将d[key]从d中移除。如果映射中不存在key，则会引发KeyError
del dict_a["four"]
print(f"dict_a: {dict_a}")
# del dict_a["five"]  # KeyError: 'five'

# pop(key[, default])：如果key存在于字典中则将其移除并返回其值，否则返回default。如果default未给出且key不存在于字典中，则会引发KeyError
val = dict_a.pop("one")
print(f"val: {val}")
print(f"dict_a: {dict_a}")
# val2 = dict_a.pop("four")  # KeyError: 'four'
val = dict_a.pop("four", "哈哈")
print(f"val: {val}")
print(f"dict_a: {dict_a}")

# keys()：返回字典所有的key
dict_a_keys = dict_a.keys()
print(f"dict_a_keys: {dict_a_keys} type: {type(dict_a_keys)}")
for k in dict_a_keys:
    print(f"k: {k}")

# key in d：如果d中存在键key则返回True，否则返回False
print("two" in dict_a)

# clear()：移除字典中的所有元素
dict_a.clear()
print(f"dict_a: {dict_a}")
