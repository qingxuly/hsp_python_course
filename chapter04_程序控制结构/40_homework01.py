"""
某人有100000元，没经过一次路口，需要交费，规则如下：
当现金>50000时，每次交5%；当现金<=50000时，每次交1000.
"""
money = 100000
count = 0
while True:
    if money > 50000:
        money *= 0.95
        count += 1
    elif money >= 1000:
        money -= 1000
        count += 1
    else:
        break

print("count =", count, "money =", money)
