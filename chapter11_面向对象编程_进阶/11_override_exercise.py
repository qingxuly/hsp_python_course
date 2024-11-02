class Person:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f"名字：{self.name} 年龄：{self.age}"


class Student(Person):
    id = None
    score = None

    def __init__(self, id, score, name, age):
        # 调用父类的构造器完成继承父类的属性和属性的初始化
        super().__init__(name, age)
        # 子类的特有的属性，我们自己完成初始化
        self.id = id
        self.score = score

    def say(self):
        return f"id:{self.id} score:{self.score} {super().say()}"


person = Person("tom", 12)
print(person.say())

student = Student("tom", 14, "tom", 18)
print(student.say())
