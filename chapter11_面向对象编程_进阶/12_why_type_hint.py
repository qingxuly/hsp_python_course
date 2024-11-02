# 对字符串进行遍历
# a: str 给形参a进行类型注解，标注a的类型是str。
def fun1(a: str):
    for ele in a:
        print(ele)


# Ctrl + P 提示参数时，没有类型提示
# 如果类型传错了，就会出现异常
fun1(100)  # TypeError: 'int' object is not iterable

