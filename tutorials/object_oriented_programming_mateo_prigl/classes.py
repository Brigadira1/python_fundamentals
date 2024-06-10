class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary = self.salary + self.salary * (percent / 100)

    def __str__(self):
        return (f"{self.name} is {self.age} years old. Employee is a "
                f"{self.position} with the salary of ${self.salary}")

    def __repr__(self):
        return f'''Employee("{self.name}", {self.age}, "{self.position}", {self.salary})'''

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) is not str:
            raise TypeError(f"{name} should be of type string")
        self._name = name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary
    @property
    def annual_salary(self):
        return self.salary * 12


employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)
employee3 = Employee("Yavor Stoimenov", 34, "manager", 10000)

print(employee1.annual_salary)
employee1.salary = 5000
print(employee1.annual_salary)


# employee2.increase_salary(20)
# print(employee2)
# print(repr(employee2))
#
