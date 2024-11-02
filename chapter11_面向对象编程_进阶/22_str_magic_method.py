class Monster:
    name = None
    age = None
    gender = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 请输出 Monster[name, job, sal] 对象的属性信息
    """
        1. 在默认情况下，调用的是父类。Monster的父类object的__str__
        2. 父类object的__str__ 返回的就是类型+地址
        3. 可以根据需要重写__str__
    """
    def __str__(self):
        # return super().__str__()
        return f"{self.name} {self.age} {self.gender}"


m = Monster("青牛怪", 500, "n男")
print(m)  # 默认输出类型+对象的地址
print(m, hex(id(m)))
