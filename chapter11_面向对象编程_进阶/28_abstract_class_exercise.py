from abc import abstractmethod, ABC


class Employee(ABC):
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


class CommonEmployee(Employee):
    def work(self):
        print(f"普通员工 {self.name} 工作中")


class Manager(Employee):
    def __init__(self, name, id, salary, bonus):
        super().__init__(name, id, salary)
        self.bonus = bonus

    def work(self):
        print(f"经理 {self.name} 工作中")


manager = Manager("king", "1-111", 10000, 100000)
manager.work()

commonEmployee = CommonEmployee("time", "2-222", 5000)
commonEmployee.work()
