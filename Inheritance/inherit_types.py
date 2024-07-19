# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Single inheritance
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

# Multiple inheritance
class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")

class Kitten(Cat, Dog):
    def purr(self):
        print(f"{self.name} is purring.")

# Multilevel inheritance
class Lion(Dog):
    def roar(self):
        print(f"{self.name} is roaring.")

# Hierarchical inheritance
class Tiger(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

# Creating objects
dog = Dog("Buddy")
dog.eat()
dog.bark()

cat = Cat("Whiskers")
cat.eat()
cat.meow()

kitten = Kitten("Fluffy")
kitten.eat()
kitten.meow()
kitten.bark()
kitten.purr()

lion = Lion("Simba")
lion.eat()
lion.bark()
lion.roar()

tiger = Tiger("Stripe")
tiger.eat()
tiger.hunt()