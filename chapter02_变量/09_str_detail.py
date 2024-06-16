# 字符串使用注意事项
# 使用引号`'`或`"`包括起来，创建字符串
str1 = "tom说：\"hello\""
str2 = 'jack说："hello"'
print(str1)
print(str2)

print(f"st2的类型:{type(str2)}")

# 通过加号可以连接字符串
print("hi" + " tom")

# Python中不支持单字符类型，单字符在Python中也是作为一个字符串使用
str3 = "A"
print("str3类型", type(str3))

# 用三个单引号'''内容'''或三个双引号"""内容"""可以使字符串内容保持原样输出，在输出格式复杂的内容是比较有用的。
content = """ Hi，我是你的百度翻译AI助手，我可以提供一站式翻译服务，'''f''
目前仅支持中文和英语，其它语种正在努力学习中；
所有内容均由AI提供，仅供参考，如有错误请反馈，我们将持续改进！"""
print(content)

# 在字符串前面加`r`可以使整个字符串不会被转义
str4 = "jack\ntom\tking"
print(str4)
str5 = r"jack\ntom\tking"
print(str5)

# 字符串驻留机制
str1 = "hello"
str2 = "hello"
str3 = "hello"

# id()函数是可以返回对象/数据的内存地址
print("str1的地址：", id(str1))
print("str2的地址：", id(str2))
print("str3的地址：", id(str3))

# pycharm进行了优化处理
str6 = "abc123#"
str7 = "abc123#"
print(id(str6), id(str7))

num1 = -100
num2 = -100
print(id(num1), id(num2))
