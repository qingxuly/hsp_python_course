from abc import ABC, abstractmethod


# 将 Animal 做成抽象类，并让子类 Tiger 实现。

# Animal 是抽象类
class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # cry() 是抽象方法
    @abstractmethod
    def cry(self):
        pass


# 注意：抽象类（含有抽象方法），不能实例化。
# TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'cry'
# animal = Animal("动物", 3)


# 编写子类 Tiger，继承 Animal 并实现抽象方法。
class Tiger(Animal):
    def cry(self):
        print('Tiger is crying')


tiger = Tiger('Tiger', 20)
tiger.cry()
