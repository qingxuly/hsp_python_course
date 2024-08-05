# 在初始化对象时，会自动执行__init__方法
class Person:
    name = None
    age = None

    # 构造方法/构造器
    # 构造方法是完成对象的初始化任务
    def __init__(self, name, age):
        print(f"__init__ 执行了 {name} {age}")
        # 把接收到的name和age 赋给属性(name, age)
        # self就是你当前创建的对象
        print(f"self id: {id(self)}")
        self.name = name
        self.age = age


# 创建对象
p1 = Person("kobe", 20)
print(f"p1 id: {id(p1)}")
print(f"p1的信息： {p1.name} {p1.age}")

p2 = Person("tim", 30)
print(f"p2 id: {id(p2)}")
print(f"p2的信息： {p2.name} {p2.age}")
