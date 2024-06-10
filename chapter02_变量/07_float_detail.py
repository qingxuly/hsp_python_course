import sys

n3 = 5.12
n4 = .512
print("n4 = ", n4)

n5 = 5.12e2  # 5.12乘以10的2次方
print("n5 = ", n5)

n6 = 5.12e-2  # 5.12除以10的2次方
print("n6 = ", n6)

# float_info 是一个具名元组，存有浮点型的相关信息
print(sys.float_info.max)
print(sys.float_info.min)

# 浮点类型计算后，存在精度的缺失，可以使用 Decimal 类进行精确计算
# 1. 为了避免浮点数的精度问题，可以使用Decimal类进行精确计算
# 2. 如果使用Decimal类，需要导入Decimal类
# b = 8.1 / 3  # b = 2.6999999999999997

from decimal import Decimal
b = Decimal("8.1") / Decimal("3")
print("b = ", b)  # b =  2.7
