# 编程创建一个Cal计算类，在其中定义2个成员变量表示两个操作数，定义四个方法实现求和、差、乘、商（要求除数为0的话，要提示）并创建对象，分别测试
"""
    思路分析：
    类名：Cal
    属性：num1, num2
    构造器/构造方法：__init__(self, num1, num2)
    定义四个方法实现求和 def sum(), 求差 def minus(), 求积 def mul(), 求商 def div()
    商（要求除数为0的话，要提示）
"""


class Cal:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 == 0:
            print("num2 不能为0")
        else:
            return self.num1 / self.num2


cal = Cal(1, 0)
print("和=", cal.sum())
print("差=", cal.minus())
print("积=", cal.mul())
print("商=", cal.div())
