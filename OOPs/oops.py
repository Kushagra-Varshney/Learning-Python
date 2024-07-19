class Employee :
    def __init__(self, name, age, salary) :
        self.name = name
        self.age = age
        self.salary = salary

    # we need to accept self as the first argument to access the instance variables else it will throw an error
    def display(self) :
        print(f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}')

    @staticmethod
    def greet() :
        print('Hello')

emp1 = Employee('John', 30, 50000)
emp1.display() # this gets converted into Employee.display(emp1)