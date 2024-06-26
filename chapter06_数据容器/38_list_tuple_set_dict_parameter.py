def f1(my_list):
    print(f"②f1() my_list: {my_list} 地址：{id(my_list)}")
    my_list[0] = "jack"
    print(f"③f1() my_list: {my_list} 地址：{id(my_list)}")


print("-" * 30 + "list" + "-" * 30)
my_list = ["tom", "mary", "hsp"]
print(f"①my_list: {my_list} 地址：{id(my_list)}")
f1(my_list)
print(f"④my_list: {my_list} 地址：{id(my_list)}")


def f2(my_tuple):
    print(f"②f2() my_tuple: {my_tuple} 地址：{id(my_tuple)}")
    print(f"③f2() my_tuple: {my_tuple} 地址：{id(my_tuple)}")


print("-" * 30 + "tuple" + "-" * 30)
my_tuple = ("hi", "ok", "hello")
print(f"①my_tuple: {my_tuple} 地址：{id(my_tuple)}")
f2(my_tuple)
print(f"④my_tuple: {my_tuple} 地址：{id(my_tuple)}")


def f3(my_set):
    print(f"②f3() my_set: {my_set} 地址：{id(my_set)}")
    my_set.add("红楼")
    print(f"③f3() my_set: {my_set} 地址：{id(my_set)}")


print("-" * 30 + "set" + "-" * 30)
my_set = {"水浒", "西游", "三国"}
print(f"①my_set: {my_set} 地址：{id(my_set)}")
f3(my_set)
print(f"④my_set: {my_set} 地址：{id(my_set)}")


def f4(my_dict):
    print(f"②f4() my_dict: {my_dict} 地址：{id(my_dict)}")
    my_dict['address'] = "兰若寺"
    print(f"③f4() my_dict: {my_dict} 地址：{id(my_dict)}")


print("-" * 30 + "dict" + "-" * 30)
my_dict = {"name": "小倩", "age": 18}
print(f"①my_dict: {my_dict} 地址：{id(my_dict)}")
f4(my_dict)
print(f"④my_dict: {my_dict} 地址：{id(my_dict)}")
