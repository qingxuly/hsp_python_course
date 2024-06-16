# 字符串和数值类型传参机制
def f1(a):
    print(f"f1() a的值：{a} 地址是：{id(a)}")
    a += 1
    print(f"f1() a的值：{a} 地址是：{id(a)}")


a = 10
print(f"调用f1()前 a的值：{a} 地址是：{id(a)}")
f1(a)
print(f"调用f1()后 a的值：{a} 地址是：{id(a)}")


def f2(name):
    print(f"f2() name：{name} 地址是：{id(name)}")
    name += "hi"
    print(f"f2() name的值：{name} 地址是：{id(name)}")


name = "tom"
print(f"调用f2()前 name的值：{name} 地址是：{id(name)}")
f2(name)
print(f"调用f2()后 name的值：{name} 地址是：{id(name)}")
