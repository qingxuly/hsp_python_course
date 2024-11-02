# 编写父类
class Student:
    name = None
    age = None
    __score = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"name={self.name}, age={self.age}, score={self.__score}")

    def set_score(self, score):
        self.__score = score


# 小学生类，继承Student
class Pupil(Student):
    def testing(self):
        print("小学生在考小学数学...")


# 大学生类，继承Student
class Graduate(Student):
    def testing(self):
        print("大学生在考高等数学...")


# 测试
student1 = Pupil("apple", 10)
student1.testing()
student1.set_score(70)
student1.show_info()

student2 = Graduate("grape", 22)
student2.testing()
student2.set_score(80)
student2.show_info()
