# class Cat:
#     name = "波斯猫"
#     age = 2
#
#     def info(self, name):
#         print(f"name: {name}")  # 加菲猫
#         # 通过self.属性名 可以访问对象的属性/成员变量
#         print(f"属性name：{self.name}")  # 波斯猫
#
#
# cat = Cat()
# cat.info("加菲猫")


# class Dog:
#     name = "藏獒"
#     age = 2
#
#     def info(self, name):
#         print(f"name: {name}")
#
#     # @staticmethod可以将普通方法转换为静态方法。
#     # 如果是一个静态方法，可以不带 self
#     # 静态方法的调用形式有两种：通过对象调用、通过类名调用
#     @staticmethod
#     def ok():
#         print("ok()...")
#
#
# dog = Dog()
# dog.info("德牧")
#
# # 通过对象调用
# dog.ok()
# # 通过类名调用
# Dog.ok()


# # self 表示当前对象本身，简单的说，哪个对象调用，self 就代表哪个对象。
# class Dog:
#     name = "藏獒"
#     age = 2
#
#     def hi(self):
#         print(f"hi self: {id(self)}")
#
#
# dog2 = Dog()
# print(f"dog2: {id(dog2)}")
# dog2.hi()
#
# dog3 = Dog()
# print(f"dog3: {id(dog3)}")
# dog3.hi()

# 在方法内部，要访问成员变量和成员方法，需要使用 self。
class Dog:
    name = "藏獒"
    age = 2

    def eat(self):
        print(f"{self.name} 饿了...")

    def cry(self, name):
        print(f"{name} is crying")
        print(f"{self.name} is crying")
        self.eat()
        # 不能直接调用
        # eat()


dog = Dog()
# 修改 dog对象的属性name
dog.name = "中华田园犬"
dog.cry("金毛")
