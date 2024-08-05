class Person:
    age = None
    name = None


# p1 = Person()
# p1.age = 10
# p1.name = "小明"
#
# p2 = p1
# print(p2.age)
# print(f"id(p1.name): {id(p1.name)}, id(p2.name): {id(p2.name)}")

a = Person()
a.age = 10
a.name = "jack"

b = a
print(b.name)
b.age = 200
b = None
print(a.age)
print(b.age)  # AttributeError: 'NoneType' object has no attribute 'age'

