# 斐波那契数
def fbn(n):
    """
    功能：返回n对应的斐波那契数
    :param n: 接收一个整数 n>=1.
    :return: 返回斐波那契数
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fbn(n - 1) + fbn(n - 2)


print(fbn(7))
