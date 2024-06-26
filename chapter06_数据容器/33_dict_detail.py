dict_a = {
    "jack": [100, 200, 300],
    "mary": (10, 20, "hello"),
    "nono": {"apple", "pear"},
    "smith": "计算机老师",
    "周星驰": {
        "性别": "男",
        "age": 18,
        "地址": "香港"
    },
    "key1": 100,
    "key2": 9.8,
    "key3": True
}
print(f"dict_a = {dict_a} type(dict_a) = {type(dict_a)}")

# print(dict_a[0])  # KeyError: 0

dict_b = {"one": 1, "two": 2, "three": 3}
# 遍历方式1：依次取出key，再通过dict[key]取出对应的value
for key in dict_b:
    print(f"key: {key}, value: {dict_b[key]}")

# 遍历方式2：依次取出value
for value in dict_b.values():
    print(f"value: {value}")

# 遍历方式3：依次取出key-value
for key, value in dict_b.items():
    print(f"key: {key}, value: {value}")

dict_c = {}
dict_d = dict()
print(f"dict_c = {dict_c} dict_c.type = {type(dict_c)}")
print(f"dict_d = {dict_d} dict_d.type = {type(dict_d)}")

dict_e = {"one": 1, "two": 2, "three": 3, "two": 4}
print(f"dict_e = {dict_e} dict_e.type = {type(dict_e)}")
