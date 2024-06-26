str_a = "hello,hspjy"
str_slice01 = str_a[:5:1]
print("str_slice01", str_slice01)
str_slice02 = str_a[1::1]
print("str_slice02", str_slice02)
str_slice03 = str_a[::1]
print("str_slice03", str_slice03)
str_slice04 = str_a[2:5:]
print("str_slice04", str_slice04)

str_b = "123456"
str_slice05 = str_b[-1::-1]
print("str_slice05", str_slice05)

str_slice06 = str_b[-1:-6:-1]
print("str_slice06", str_slice06)

str_c = "ABCD"
str_slice07 = str_c[1:3:1]
print("str_slice07", str_slice07)
print("str_c", str_c)