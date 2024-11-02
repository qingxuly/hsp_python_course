# 使用传统的方式
class Food:
    name = None

    def __init__(self, name):
        self.name = name


class Fish(Food):
    pass


class Bone(Food):
    pass


class Animal:
    name = None

    def __init__(self, name):
        self.name = name


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Master:
    name = None

    def __init__(self, name):
        self.name = name

    # 给猫喂鱼
    def feed_cat(self, cat: Cat, fish: Fish):
        print(f"主任{self.name} 给动物{cat.name} 喂{fish.name}")

    # 给狗喂骨头
    def feed_dog(self, dog: Dog, bone: Bone):
        print(f"主人{self.name} 给动物{dog.name} 喂{bone.name}")


master = Master("老韩")
cat = Cat("小花猫")
fish = Fish("黄花鱼")
dog = Dog("大黄狗")
bone = Bone("大棒骨")

master.feed_cat(cat, fish)
master.feed_dog(dog, bone)
