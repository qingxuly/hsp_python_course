class Person:
    age = None
    name = None

    # 成员方法
    def hi(self):
        print("hi, python")

    def cal01(self):
        result = 0
        for i in range(1, 1001):
            result += i
        print(f"result: {result}")

    def cal02(self, n):
        result = 0
        for i in range(1, n + 1):
            result += i
        print(f"result: {result}")

    def get_sum(self, n1, n2):
        return n1 + n2


# 测试
p = Person()

p.hi()
p.cal01()
p.cal02(10)
print(p.get_sum(10, 20))
