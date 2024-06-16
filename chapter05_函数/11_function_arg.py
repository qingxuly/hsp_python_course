# 定义一个函数，可以返回两个数的最大值
def get_max_val(num1, num2):
    max_val = num1 if num1 > num2 else num2
    return max_val


def f1(fun, num1, num2):
    """
    功能：调用fun返回num1和num2的最大值
    :param fun: 表示接收一个函数
    :param num1: 传入一个数
    :param num2: 传入一个数
    :return: 返回最大值
    """
    return fun(num1, num2)


def f2(fun, num1, num2):
    """
    功能：调用fun返回num1和num2的最大值，同时返回两个数的和
    :param fun:
    :param num1:
    :param num2:
    :return:
    """
    return num1 + num2, fun(num1, num2)


print(f1(get_max_val, 10, 20))
print(f2(get_max_val, 10, 20))
x, y = f2(get_max_val, 10, 20)
print(f"x: {x}, y: {y}")
