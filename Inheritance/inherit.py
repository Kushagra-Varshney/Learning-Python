class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}')

class Manager(Employee):
    def __init__(self, name, age, salary, team):
        super().__init__(name, age, salary)
        self.team = team

    def display(self):
        super().display()
        print(f'Team: {self.team}')

emp1 = Manager("Purshottam", 30, 50000, "Engineering")