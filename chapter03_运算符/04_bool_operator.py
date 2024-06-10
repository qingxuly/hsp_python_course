# 布尔运算符的使用
a = 10
b = 20

print(a and b)
print(a or b)
print(not (a and b))

# and 使用细节
score = 70
if (score >= 60 and score <= 80):
    print("成绩还不错~")

a = 1
b = 99
print(a and b)
print((a > b) and b)
print((a < b) and b)

# or 使用细节
score = 70
if score <= 60 or score >= 80:
    print("hi~")

a = 1
b = 99
print(a or b)
print((a > b) or b)
print((a < b) or b)

# not 使用细节
a = 3
b = not (a > 3)
print(b)
print(not False)
print(not True)
print(not 0)
print(not "jack")
print(not 1.88)
print(not a)
