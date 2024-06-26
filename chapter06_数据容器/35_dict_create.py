books = ["红楼梦", "三国演义", "西游记", "水浒传"]
author = ["曹雪芹", "罗贯中", "吴承恩", "施耐庵"]
dict_book = {book: author for book, author in zip(books, author)}
print(dict_book)

str1 = "hsp"
dict_str1 = {k: v * 2 for k, v in zip(str1, str1)}
print(dict_str1)

english_list = ["red", "black", "yellow", 'white']
chinese_list = ["红色", "黑色", "黄色", '白色']
dict_color = {chinese: english.upper() for chinese, english in zip(chinese_list, english_list)}
print(dict_color)
