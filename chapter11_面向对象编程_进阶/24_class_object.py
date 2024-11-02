class Monster:
    name = "蝎子精"
    age = 300

    def hi(self):
        print(f"hi() {self.name} {self.age}")


# 下一个断点，可以看到Monster的情况
print(Monster)

# 通过Class对象，可以引用属性（没有创建实例对象也可以引用/访问）
print(f"Monster.name is {Monster.name} Monster.age is {Monster.age}")

# 通过类名如何调用非静态成员方法
Monster.hi(Monster)
