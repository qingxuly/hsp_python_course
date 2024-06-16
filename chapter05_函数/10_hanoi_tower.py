def hanoi_tower(num, a, b, c):
    """
    输出指定num个盘子移动的顺序
    :param num: 指定盘子数
    :param a: A柱
    :param b: B柱
    :param c: C柱    """
    if num == 1:
        print(f"第1个盘从：{a}->{c}")
    else:
        # 有多个盘，我们认为只有两个，上面所有的盘和最下面的盘
        # 移动上面所有的盘到B柱子，这个过程会借助到C柱子
        hanoi_tower(num - 1, a, c, b)
        # 移动最下面的盘
        print(f"第{num}个盘从：{a}->{c}")
        # 把上面所有的盘从B柱子移动到C柱子，这个过程会使用到A柱子
        hanoi_tower(num - 1, b, a, c)


hanoi_tower(3, "A", "B", "C")
