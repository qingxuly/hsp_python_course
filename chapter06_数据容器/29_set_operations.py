basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
# len(集合)：集合元素个数
print("basket元素个数：", len(basket))

# x in s：检测x是否为s中的成员
print("apple" in basket)

# add(elem)：将元素elem添加到集合中
basket.add("grape")
print("basket:", basket)

# remove(elem)：从集合中移除元素elem。如果elem不存在于集合中则会引发KeyError
basket.remove("apple")
print("basket:", basket)
# basket.remove("aaa")  # KeyError: 'aaa'

# pop()：从集合中移除并返回任意一个元素。如果集合为空则会引发KeyError
ele = basket.pop()
print("ele:", ele, "type:", type(ele))
print("basket:", basket)

# clear()：从集合中移除所有元素
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print("basket:", basket)

# union(*others) <br />set | other | ... ：返回一个新集合，其中包含来自原集合以及others指定的所有集合中的元素
books = {"天龙八部", "笑傲江湖"}
books_2 = {"雪山飞狐", "神雕侠侣", "天龙八部"}
books_3 = books.union(books_2)
books_3 = books | books_2  # 等价于上一行代码
print("books_3:", books_3)

# intersection(*others) <br />set & other & ...：返回一个新集合，其中包含原集合以及others指定的所有集合中共有的元素
books_4 = books.intersection(books_2)
books_4 = books & books_2  # 等价于上一行代码
print("books_4:", books_4)

# difference(*others)<br />set - other - ... ：返回一个新集合，其中包含原集合以及others指定的其他结合中不存在的元素
books_5 = books.difference(books_2)
books_5 = books - books_2
print("books_5:", books_5)
books_6 = books_2 - books
print("books_6:", books_6)
