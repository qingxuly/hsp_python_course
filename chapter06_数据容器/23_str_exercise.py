"""
定义一个字符串，str_names="tom jack mary nono smith hsp"
统计一共有多个人名；如果有"hsp"则替换成"老韩";如果人名是英文，则把首字母改为大写
str.capitalize()：字符串首字符改为大写
"""

str_names = str("tom jack mary nono smith")

str_names_list = str_names.split(" ")
print(f"人名的个数：{len(str_names_list)}")
str_names_re = str_names.replace("hsp", "韩顺平")
print(str_names_re)

str_names_upper = ""
for ele in str_names_list:
    if ele.isalpha():
        str_names_upper += ele.capitalize() + " "

# 去掉两边的" "
str_names_upper = str_names_upper.strip(" ")
print(str_names_upper)
