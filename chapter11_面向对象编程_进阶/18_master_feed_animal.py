# 使用多态的方式
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


# 扩展 Horse、Grass，体会多态的机制带来的好处
class Horse(Animal):
    pass


class Grass(Food):
    pass


class Master:
    name = None

    def __init__(self, name):
        self.name = name

    def feed(self, animal: Animal, food: Food):
        print(f"主人{self.name} 给动物{animal.name} 喂{food.name}")


master = Master("老韩")
cat = Cat("小花猫")
fish = Fish("黄花鱼")
dog = Dog("大黄狗")
bone = Bone("大棒骨")
horse = Horse("枣红马")
grass = Grass("嫩草")

master.feed(cat, fish)
master.feed(dog, bone)
master.feed(horse, grass)
