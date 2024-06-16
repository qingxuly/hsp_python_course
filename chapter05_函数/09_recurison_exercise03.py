# f(n)
def f(n):
    if n == 1:
        return 3
    else:
        return 2 * f(n - 1) + 1


print(f(10))
