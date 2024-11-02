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

    # 提供公共的方法，对私有属性操作
    def get_job(self):
        return self.__job


clerk = Clerk("apple", "python工程师", 20000)

# 如果这样使用，因为python语言的动态特性，会动态的创建属性 __job，但是这个属性和我们在类中定义的私有属性 __job不是同一个变量，我们在类中定义的__job私有属性完整的名字是 _Clerk__job，而并不是
# 可以通过debug的“Evaluate Expression”来观察。
clerk.__job = "Go工程师"
print(f"job = {clerk.__job}")  # job = Go工程师

# 获取真正的私有属性__job
print(f"{clerk.get_job()}")
