def hi():
    n = 10
    print("n:", n)


hi()


# 函数内部定义的n，在函数外部不能使用
# print("n:", n)


def cry():
    print("hi")


def cry():
    print("ok")


# 这个ry会默认就近原则，即第二个cry()，输出OK。
cry()


def car_info(name, price, color):
    print(f"name: {name}, price: {price}, color: {color}")


# 传递的实参和定义的形参顺序和个数必须一致，否则报 TypeError 错误
# car_info("宝马", 500000, "red", 1)  # TypeError: car_info() takes 3 positional arguments but 4 were given
car_info("宝马", 500000, "red")


def f2(n1, n2):
    return n1 + n2, n1 - n2


r1, r2 = f2(10, 20)
print(f"r1: {r1}, r2: {r2}")


def book_info(name, price, author, amount):
    print(f"name: {name}, price: {price}, author: {author}, amount: {amount}")


# 通常调用方式，一一对应
book_info("红楼梦", 60, "曹雪芹", 30000)
# 关键字参数
book_info(name="红楼梦", price=60, amount=60000, author="曹雪芹")
book_info("红楼梦", 60, amount=90000, author="曹雪芹")


# 定义函数时，可以给参数提供默认值，调用函数时，指定了实参，则以指定为准，没有指定，则以默认值为准
def book_info2(name="<<thinking in python", price=66.8, author="龟叔", amount=1000):
    print(f"name: {name}, price: {price}, author: {author}, amount: {amount}")


book_info2()
book_info2("<<study python>>")


# 默认参数，需要放在参数列表后
def book_info3(name, price, author="龟叔", amount=1000):
    print(f"name: {name}, price: {price}, author: {author}, amount: {amount}")


book_info3("<<python 揭秘>>", 999)


# 计算多个数的和，不是不确定是几个数，*表示[0到多]，使用可变参数/不定长参数(*args)
def sum(*args):
    print(f"args: {args} 类型：{type(args)}")
    total = 0
    for els in args:
        total += els
    return total


result1 = sum()
print(result1)
result2 = sum(1, 3, 5)
print(result2)


# 接收一个人的信息，但是有哪些信息是不确定的，就可以使用关键字可变参数(**kwargs)
def person_info(**kwargs):
    print(f"kwargs: {kwargs} 类型：{type(kwargs)}")
    for kwargs_name in kwargs:
        print(f"参数名：{kwargs_name} 参数值：{kwargs[kwargs_name]}")


person_info(name="hsp", age=18, email="hsp@qq.com")
person_info(name="hsp", age=18, email="hsp@qq.com", sex="男", address="北京")
person_info()
