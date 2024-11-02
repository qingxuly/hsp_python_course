# 基础数据类型注解
n1: int = 10  # 对n1进行类型注解，标注n1的类型为int；如果给出的类型与标注的类型类型不一致，则Pycharm会给出黄色警告
n2: float = 10.1
is_pass: bool = True
name: str = "Tom"


class Cat:
    pass


# 实例对象类型注解
cat: Cat = Cat()  # 对cat进行类型注解，标注cat类型是Cat

# 容器类型注解
my_list: list = [1, 2, 3]  # 对my_list进行类型注解，标注my_list类型为list。
my_tuple: tuple = ("run", "sing", "fly")
my_set: set = {1, 2, 3}
my_dict: dict = {"name": "Tom", "age": 22}

# 容器详细类型注解
my_list1: list[int] = [1, 2, 3]  # 对my_list1进行类型注解，标注my_list1类型是list，而且该list元素是int。
# 元组类型设置详细类型注解，需要把每个元素类型都标注一下
my_tuple1: tuple[str, str, str, float] = ("run", "sing", "fly", 1.1)
my_set1: set[int] = {1, 2, 3}
# 字典类型设置详细类型注解，需要设置两个类型，即[key类型, value类型]
# 对my_dict1进行类型注解，标注my_dict1类型是dict，而且key的类型是str，values的类型是int。
my_dict1: dict[str, int] = {"score": 100, "score2": 80}

# 注释中使用注解
# # type: float 用于标注变量n3的类型是float。
n3 = 89.9  # type: float
my_list3 = [100, 200, 300]  # type: list[int]
email = "hsp@sohu.com"  # type: str
