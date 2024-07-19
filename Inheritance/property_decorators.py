class Person:
    def __init__(self, name):
        self._name = name

    @property # getter
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

# Usage
person = Person("John")
print(person.name)  # Output: John

person.name = "Mike"
print(person.name)  # Output: Mike