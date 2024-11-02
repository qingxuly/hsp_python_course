class Doctor:
    def __init__(self, name, age, gender, sal):
        self.name = name
        self.age = age
        self.gender = gender
        self.sal = sal

    def __eq__(self, other):
        if not isinstance(other, Doctor):
            return False
        return self.name == other.name and self.age == other.age and self.sal == other.sal


doctor1 = Doctor('tom', 24, 1, 'male')
doctor2 = Doctor('tom', 24, 1, 'male')
doctor3 = Doctor('tom', 25, 1, 'male')

print(doctor1 == doctor2)
print(doctor1 == doctor3)
