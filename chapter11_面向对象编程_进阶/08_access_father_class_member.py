class A:
    n1 = 100

    def run(self):
        print("A-run()...")


class B(A):
    n1 = 200

    def run(self):
        print("B-run()...")

    # 通过父类名去访问父类的成员
    def say(self):
        print(f"父类的n1={A.n1} 本类的n1={self.n1}")
        # 调用父类的run
        A.run(self)

        # 调用本类的run()
        self.run()

    # 通过super()方式去访问父类对象
    def hi(self):
        print(f"父类的n1={super().n1}")


b = B()
b.say()
b.hi()
