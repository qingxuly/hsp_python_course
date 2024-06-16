def f1(fun, num1, num2):
    """
    功能：调用fun返回num1和num2的最大值
    :param fun: 接收函数（匿名的）
    :param num1:
    :param num2:
    :return:
    """
    print(f"fun类型：{type(fun)}")
    return fun(num1, num2)


"""
1. lambda a, b: a if a > b else b
2. 不需要return， 运算结果就是返回值
"""
max_value = f1(lambda a, b: a if a > b else b, 1, 2)
print(max_value)
