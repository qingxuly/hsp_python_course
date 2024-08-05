# 函数
def hi():
    print("hi, python")


# 定义类
class Person:
    age = None
    name = None

    def ok(self):
        pass


# 创建对象 p、p2
p = Person()
p2 = Person()

# 动态地给p对象添加方法m1，注意：只是针对p对象添加方法
# m1 是你新增加的方法的名称，由程序员指定名称
# 即 m1方法和函数hi关联起来，当调用m1方法时，会执行hi函数
p.m1 = hi

# 调用m1(即hi)
p.m1()

print(type(p.m1), type(hi))  # <class 'function'> <class 'function'>
print(type(p.ok))  # <class 'method'>


# 因为没有动态的给p2 添加方法，会报错
p2.m1()  # AttributeError: 'Person' object has no attribute 'm1'
