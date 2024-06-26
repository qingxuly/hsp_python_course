# 演示字符串常用操作
str_names = " jack tom mary hsp nono tom "

# len(str)：字符串的长度，也就是包含多少个字符
print(f"{str_names}有{len(str_names)}个字符")

# str.replace(old, new[, count])：返回字符串的副本，其中出现的所有子字符串 old 都将被替换为 new。如果给出了可选参数 count，则只替换前 count 次出现。
# 说明：返回字符串的副本：表示原来的字符串不变，而是返回一个新的字符串。
str_names_new = str_names.replace("tom", "汤姆", 1)
print("str_names_new:", str_names_new)
print("str_names:", str_names)

# str.split(sep=None, maxaplit=-1)：返回一个由字符串内单词组成的列表，使用 seq 作为分隔字符串。如果给出了 maxsplit，则最多进行 maxsplit 次拆分（因此，列表最多会有
# maxsplit + 1个元素）。如果 maxsplit 未指定或为 -1，则不限制拆分次数（进行所有可能的拆分）
str_names_split = str_names.split(" ")
print("str_names_ww2split:", str_names_split, type(str_names_split))

# str.count(sub)：统计指定字符串在字符串中出现的次数
print("tom出现的次数：", str_names.count("tom"))

# str.index(sub)：从字符串中找出指定字符串第一个匹配项的索引位置
print(f"tom出现的索引：{str_names.index('tom')}")

# str.strip([chars])：返回原字符串的副本，移除其中的前导和末尾字符。chars 为指定要移除字符的字符串
# 说明：这个方法通常用于除去前后的空格，或者去掉制定的某些字符
str_names_strip = str_names.strip()
print("str_names_strip:", str_names_strip)
print("123t2om13".strip("123"))

# str.lower()：返回原字符串小写的副本
str_names = "hspHaHa"
str_names_lower = str_names.lower()
print("str_names_lower:", str_names_lower)

# str.upper()：返回原字符串大写的副本
str_names_upper = str_names.upper()
print("str_names_upper:", str_names_upper)
