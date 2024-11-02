class A:
    n1 = 300
    n2 = 500
    n3 = 600

    def fly(self):
        print("A-fly()...")


class B(A):
    n1 = 200
    n2 = 400

    def fly(self):
        print("B-fly()...")


class C(B):
    n1 = 100

    def fly(self):
        print("C-fly()...")

    def say(self):
        print(self.n1)  # 100
        print(self.n2)  # 400
        print(self.n3)  # 600
        print(super().n1)  # 200
        print(B.n1)  # 200
        print(C.n1)  # 100

        # 针对上面的程序，想在C的say()中，调用C的fly()和A的fly()，应该如何调用？
        self.fly()  # C-fly()...
        A.fly(self)  # A-fly()...



c = C()
c.say()
