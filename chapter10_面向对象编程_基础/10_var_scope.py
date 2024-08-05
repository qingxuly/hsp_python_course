class Cat:
    # 属性
    name = None
    age = None

    #     # n1, n2, result 就是局部变量
    #     def cal(self, n1, n2):
    #         result = n1 + n2
    #         print(f"cal() 使用属性name {self.name}")
    #
    #     def cry(self):
    #         print(f"cry() 使用属性name {self.name}")
    #
    #     def eat(self):
    #         print(f"eat() 使用属性name {self.name}")
    #
    #
    # cat = Cat()
    # cat.cal(10, 20)
    # cat.cry()
    # cat.eat()

    def hi(self):
        name = "皮皮"
        print(f"name is {name}")
        print(f"self.name is {self.name}")


cat = Cat()
cat.name = "小咪"
cat.hi()
