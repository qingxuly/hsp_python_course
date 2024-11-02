class Employee:
    __name = None
    __salary = None

    # 构造器
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_annual(self):
        return self.__salary * 12

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary


class Worker(Employee):
    def work(self):
        print(f"普通工人 {self.get_name()} 正在工作中")


class Manager(Employee):
    __bonus = None

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.__bonus = bonus

    def manage(self):
        print(f"经理 {self.get_name()} 正在工作中")

    def get_annual(self):
        return super().get_annual() + self.__bonus


def show_emp_annual(e: Employee):
    print(f"{e.get_name()} 年工资： {e.get_annual()}")


worker = Worker("king", 10000)
show_emp_annual(worker)

manager = Manager("tim", 20000, 100000)
show_emp_annual(manager)


def working(e: Employee):
    if isinstance(e, Worker):
        e.work()
    elif isinstance(e, Manager):
        e.manage()
    else:
        print("无法确定工作状态")


working(worker)
working(manager)
