# class Person:
#     name = None
#     age = None
#
#     def __init__(self, name, age):
#         print(f"__init__执行了... 得到了{name} {age}")
#         self.name = name
#         self.age = age
#
#     def __init__(self, name):
#         print(f"__init__执行了~~ 得到了{name}")
#         self.name = name
#
#
# # TypeError: Person.__init__() takes 2 positional arguments but 3 were given
# # p1 = Person("tim", 20)
#
# # 后面的__init__()生效
# p1 = Person("tim")
# print(f"p1的 name={p1.name} age={p1.age}")

# 为了代码简洁，我们也可以通过__init__动态的生成对象属性
# python可以动态的生成对象属性。
class Person:
    def __init__(self, name, age):
        print(f"__init__执行了... 得到了{name} {age}")
        # 将接收到的name和age 赋给当前对象的name和age属性
        # python 支持动态生成对象属性
        self.name = name
        self.age = age
        return "hello"  # TypeError: __init__() should return None, not 'str'



p1 = Person("tim", 30)
print(f"p1的 name={p1.name} age={p1.age}")
