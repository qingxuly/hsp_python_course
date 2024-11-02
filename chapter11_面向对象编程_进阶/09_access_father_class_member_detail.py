# class A:
#     n1 = 100
#     __n2 = 600
#
#     def run(self):
#         print("A-run()...")
#
#     def __jump(self):
#         print("A-jump()...")
#
#
# class B(A):
#     # 子类不能直接访问父类的私有成员
#     def say(self):
#         # print(A.__n2)  # AttributeError: type object 'A' has no attribute '_B__n2'. Did you mean: '_A__n2'?
#         # print(super().__n2)  # AttributeError: 'super' object has no attribute '_B__n2'
#
#         # A.__jump(self)
#         # super().jump()
#         print("B-say()...")
#
#
# b = B()
# b.say()


class Base:
    n3 = 800

    def fly(self):
        print("Base-fly()...")


class A(Base):
    n1 = 100
    __n2 = 600

    def run(self):
        print("A-run()...")

    def __jump(self):
        print("A-jump()...")


class B(A):
    # 访问不限于直接父类，而是建立从子类向上级父类的查找关系 B->A->Base...
    def say(self):
        print(Base.n3, A.n3, super().n3)

        Base.fly(self)
        A.fly(self)
        super().fly()
        self.fly()


b = B()
b.say()
