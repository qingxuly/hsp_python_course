# 定义一个圆类Circle，定义属性：半径，提供显示圆周长功能的方法，提供显示圆面积的方法。

"""
    思路分析：
    类名：Circle
    属性：radius
    构造器：__init_(self, radius)
    方法：len(self) 显示圆周长
    方法：area(self) 显示圆面积
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def len(self):
        len = 2 * math.pi * self.radius
        print("周长：", round(len, 2))

    def area(self):
        area = math.pi * (self.radius ** 2)
        print("面积：", round(area, 2))


# 测试
circle = Circle(5)
circle.len()
circle.area()
