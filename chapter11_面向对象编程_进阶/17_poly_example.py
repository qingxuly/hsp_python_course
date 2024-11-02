class Animal:
    def cry(self):
        pass


class Cat(Animal):
    def cry(self):
        print("喵喵喵")


class Dog(Animal):
    def cry(self):
        print("汪汪汪")


class Pig(Animal):
    def cry(self):
        print("噜噜噜")


# 在Python面向对象编程中，子类对象可以传递给父类类型
def func(animal: Animal):
    print(f"animal类型：{type(animal)}")
    animal.cry()


cat = Cat()
dog = Dog()
pig = Pig()

func(cat)
func(dog)
func(pig)


class AA:
    def hi(self):
        print("AA-hi()...")


class BB:
    def hi(self):
        print("BB-hi()...")


def test(obj):
    obj.hi()


aa = AA()
bb = BB()
test(aa)
test(bb)
