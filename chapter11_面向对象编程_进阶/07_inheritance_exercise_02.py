class Computer:
    cpu = None
    memory = None
    disk = None

    def __init__(self, cpu, memory, disk):
        self.cpu = cpu
        self.memory = memory
        self.disk = disk

    def get_details(self):
        return f"CPU: {self.cpu}, Memory: {self.memory}, Disk: {self.disk}"


class PC(Computer):
    brand = None

    def __init__(self, cpu, memory, disk, brand):
        # 初始化子类的属性——方式1
        # self.cpu = cpu
        # self.memory = memory
        # self.disk = disk
        # self.brand = brand

        # 初始化子类的属性——方式2
        # 通过super().xx 方式可以去调用父类方法，这里通过 super().__init__(cpu, memory, disk, brand) 去调用父类的构造器
        super().__init__(cpu, memory, disk)
        self.brand = brand

    def print_info(self):
        print(f"品牌：{self.brand}\t{self.get_details()}")


pc = PC("inter", 32, 1000, "戴尔")
pc.print_info()
