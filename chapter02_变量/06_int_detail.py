# 讲解int类型的细节
import sys

n3 = 9 ** 8888
# print(n3)  # ValueError: Exceeds the limit (4300 digits) for integer string conversion;

# use sys.set_int_max_str_digits() to increase the limit
sys.set_int_max_str_digits(0)  # maxdigits must be 0 or larger than 640
print(n3)

print(10)  # 十进制
print(0x10)  # 十六进制
print(0o10)  # 八进制
print(0b10)  # 二进制

n1 = 0
n2 = 1
n3 = 2
n4 = 2 ** 15
n5 = 2 ** 30
n6 = 2 ** 128

# 在Python中，可以通过sys.getsizeof 返回对象（数据）的大小（按照字节单位返回）
print(n1, sys.getsizeof(n1), "类型", type(n1))
print(n2, sys.getsizeof(n2), "类型", type(n2))
print(n3, sys.getsizeof(n3), "类型", type(n3))
print(n4, sys.getsizeof(n4), "类型", type(n4))
print(n5, sys.getsizeof(n5), "类型", type(n5))
print(n6, sys.getsizeof(n6), "类型", type(n6))

print(sys.getsizeof(10))  # 28个字节
