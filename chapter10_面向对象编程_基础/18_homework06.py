class Demo:
    i = 100

    def m(self):
        self.i += 1
        j = self.i
        print("i =", self.i)
        print("j =", j)


d1 = Demo()
d2 = d1
d2.m()

print(d1.i)
print(d2.i)
