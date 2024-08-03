def f2(num):
    res = 0
    for i in range(1, num + 1):
        res += i
    return res


def f1(name):
    print(f"name={name} 1")
    print(f"name={name} 2")
    print(f"name={name} 3")
    r = f2(3)
    print(f"r={r}")
    print(f"name={name} 4")


f1("hsp")
print("end...")
