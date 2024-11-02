# # 抽象类需要继承`ABC`，并且需要至少一个抽象方法。
# from abc import ABC, abstractmethod
#
#
# class AAA(ABC):
#     name = "tim"
#
#     # @abstractmethod
#     # def f1(self):
#     #     pass
#
#
# # 如果没有一个抽象方法，能实例化。
# obj1 = AAA()

# # 抽象类中可以有普通方法。
# from abc import ABC, abstractmethod
#
#
# class AAA(ABC):
#     name = "tim"
#
#     @abstractmethod
#     def f1(self):
#         pass
#
#     def hi(self):
#         print("hi()")
#
#     def ok(self):
#         pass
#
#
# class BBB(AAA):
#     # 实现父类的f1抽象方法
#     def f1(self):
#         print("BBB-f1")
#
#
# obj2 = BBB()
# obj2.f1()
# obj2.hi()
# obj2.ok()


# 如果一个类继承了抽象类，则它必须实现抽象类的所有抽象方法，否则它仍然是一个抽象类。
from abc import ABC, abstractmethod


class AAA(ABC):
    name = "tim"

    @abstractmethod
    def f1(self):
        pass

    @abstractmethod
    def f2(self):
        pass

    def hi(self):
        print("hi()")

    def ok(self):
        pass


class BBB(AAA):
    # 实现父类的f1抽象方法
    def f1(self):
        print("BBB-f1")

    # 如果没有完全实现AAA的抽象方法
    # TypeError: Can't instantiate abstract class BBB without an implementation for abstract method 'f2'
    def f2(BBB):
        print("BBB-f2")


obj2 = BBB()
obj2.f1()
obj2.hi()
obj2.ok()
