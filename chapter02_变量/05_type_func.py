# 演示type() 使用

age = 80
score = 77.5
gender = '男'
name = "贾宝玉"
is_pass = True

# 查看变量的类型（本质是查看变量指向的数据的类型）
print(type(age))
print(type(score))
print(type(gender))
print(type(name))
print(type(is_pass))

# type() 可以直接查看具体的值（字面量） 的类型
print(f"hello 的类型是{type('hello')}")
print(f"1.1 的类型是{type(1.1)}")
