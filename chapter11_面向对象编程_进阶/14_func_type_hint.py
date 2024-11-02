# 对字符串进行遍历
# name: str 对形参name进行类型注解：标注name类型是str；在调用方法/函数时，传入的实参类型不是一样的，则给出黄色的警告。
def fun1(name: str):
    for ele in name:
        print(ele)


fun1("hsp")


# 接收两个整数，返回整数
# a: int, b: int 对形参a、b进行类型注解，标注a、b的类型为int； -> int 对返回值进行类型注解，标注返回值的类型为int。
def fun2(a: int, b: int) -> int:
    return a + b


print(f"结果是：{fun2(1, 2)}")
