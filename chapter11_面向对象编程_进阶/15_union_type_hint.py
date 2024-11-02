from typing import Union

# 联合类型注解， a可以是int或str
a: Union[int, str] = 100

# my_list是str类型，元素可以是int或str
my_list: list[Union[int, str]] = [1, 2, 3, "tom"]


# 函数/方法使用联合函数注解
# 接收两个数（可以是int/float），返回数（int/float）
def cal(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 + num2


print(cal(1, 2.1))
