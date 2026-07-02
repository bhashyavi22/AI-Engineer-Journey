#program 1-Basic Inhertance
class Animal:
    def sound(self):
        print("Animals make sounds")
class Dog(Animal):
    pass
dog=Dog()
dog.sound()
print("---------------------------")
#program 2-Vehicle Inheritance
class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    pass
car=Car()
car.start()
print("---------------------------")
#program 3-Child Class Own Method
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
dog=Dog()
dog.eat()
dog.bark()
print("---------------------------")
#program 4-Method Overriding
class Animal:
    def sound(self):
        print("Animals make sounds")
class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog=Dog()
dog.sound()
print("---------------------------")
# Program 5 - Using super() with constructors
class Animal:
    def __init__(self):
        print("Animal constructor")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog constructor")

dog=Dog()
print("--------------------------")
# Program 6 - Practice using super()
class Person:
    def __init__(self):
        print("Person constructor")
class Student(Person):
    def __init__(self):
        super().__init__()
        print("Student constructor")

student=Student()