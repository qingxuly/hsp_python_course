# # 子类继承了所有的属性和方法，非私有的属性和方法可以在子类直接访问，但是私有属性和方法在子类不能在子类直接访问，要通过父类提供公共的方法去访问。
# class Base:
#     # 公共属性
#     n1 = 100
#     # 私有属性
#     __n2 = 200
#
#     def __init__(self):
#         print("Base 构造方法")
#
#     def hi(self):
#         print("hi() 公共方法")
#
#     def __hello(self):
#         print("__hello() 私有方法")
#
#     # 提供公共方法，访问私有属性和私有方法
#     def test(self):
#         print("属性：", self.n1, self.__n2)
#         self.__hello()
#
#
# class Sub(Base):
#
#     def __init__(self):
#         print("Sub 构造方法")
#
#     def say_ok(self):
#         print("say_ok() ", self.n1)
#         self.hi()
#
#         # print(self.__n2)  # AttributeError: 'Sub' object has no attribute '_Sub__n2'
#         # self.__hello()  # AttributeError: 'Sub' object has no attribute '_Sub__n2'
#
#
# # 测试
# sub = Sub()
# sub.say_ok()
#
# # 调用子类继承父类的公共方法，去实现访问父类的私有成员的效果
# sub.test()

# Python支持多继承
class A:
    n1 = 100

    def sing(self):
        print("A sing()...", self.n1)


class B:
    n1 = 300
    n2 = 200

    def dance(self):
        print("B dance()...", self.n2)

    def sing(self):
        print("B sing()...", self.n2)


# 在多重继承中，如果有同名的成员，遵守从左到右的继承优先级（即：写在左边的父类优先级高，写在右边的父类优先级低）。
class C(A, B):
    # Python pass 是空语句，是为了保持程序结构的完整；pass 不做任何事情，一般用作站位语句。
    pass


c = C()
# 继承的属性信息
print(f"属性信息：{c.n1} {c.n2}")
# 调用继承的方法
c.dance()
c.sing()  # A sing()... 100
