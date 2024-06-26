# 列表生成式
list_1 = [ele * 2 for ele in range(1, 5)]
print("list_1:", list_1)  # list_1: [2, 4, 6, 8]

list2 = [ele + ele for ele in "hsp"]
print("list2:", list2)  # list2: ['hh', 'ss', 'pp']

list3 = [ele * ele for ele in range(1, 11)]
print("list3:", list3)
