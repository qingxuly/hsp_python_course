# 创建职员类（Clerk），属性：name, job, salary
# 1、不能随便查看职员 Clerk的职位和工资等隐私，比如职员 ("tiger", "python工程师", 20000)
# 2、提供公共方法，可以对职员和工资进行操作

class Clerk:
    # 公共属性
    name = None
    # 私有属性
    __job = None
    __salary = None

    # 构造方法
    def __init__(self, name, job, salary):
        self.name = name
        self.__job = job
        self.__salary = salary

    # 提供公共的方法，对私有属性操作（根据实际的业务编写即可）
    def set_job(self, job):
        self.__job = job

    def get_job(self):
        return self.__job

    # 私有方法
    def __hi(self):
        print("hi()")

    # 提供公共方法，操作私有方法
    def f1(self):
        self.__hi()


clerk = Clerk("tiger", "python工程师", 20000)
print(clerk.name)

# print(clerk.__job)  # AttributeError: 'Clerk' object has no attribute '__job'
print(clerk.get_job())
clerk.set_job("Java工程师")
print(clerk.get_job())

# 私有方法不能在类的外部直接调用
# clerk.hi()  # AttributeError: 'Clerk' object has no attribute 'hi'

# 通过公共方法，调用私有方法
clerk.f1()
