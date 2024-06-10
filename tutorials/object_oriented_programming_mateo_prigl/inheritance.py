class Employee:
    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)


class Developer(Employee):
    __slots__ = ("framework")

    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percentage, bonus=0):
        super().increase_salary(percentage)
        self.salary += bonus


class Tester(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

    def run_tests(self):
        print(f"Tests were executed by {self.name}")
        print("Tests finished succussfully")


employee1 = Tester("Lauren", 44, 1000)
employee2 = Developer("Ji-Soo", 38, 1000, "Flask")
employee3 = Employee("Emp", 0, 0)

print(employee1.__slots__)
print(employee2.__slots__)
print(employee3.__slots__)

# employee2.increase_salary(20, 30)
# print(employee2.salary)
# print(employee2.name)
# print(employee2.framework)
