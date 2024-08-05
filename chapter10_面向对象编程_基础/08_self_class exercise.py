class Person:
    name = None
    age = None

    def compare_to(self, other):
        # 名字和年龄都一样，就返回True，否则返回False
        return self.name == other.name and self.age == other.age


p1 = Person()
p1.name = "jack"
p1.age = 3
p2 = Person()
p2.name = "jack"
p2.age = 3

print(p1.compare_to(p2))
