"""
定义一个元组：("大话西游", "周星驰", 80, ["周星驰", "小甜甜"])
信息为：(片名, 导演, 票价, 演员列表)
"""

tuple_move = ("大话西游", "周星驰", 80, ["周星驰", "小甜甜"])
print("票价对应的索引：", tuple_move.index(80))
# 遍历所有演员
for ele in tuple_move[3]:
    print(ele)

# 删除 "小甜甜"， 增加演员 "牛魔王"，“猪八戒”
del tuple_move[3][1]
tuple_move[3].append("牛魔王")
tuple_move[3].append("猪八戒")
print(tuple_move)
