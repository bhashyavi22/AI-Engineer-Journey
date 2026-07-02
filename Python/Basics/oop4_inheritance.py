#program 1
class Animal:
    def sound(self):
        print("Animals make sounds")
class Dog(Animal):
    pass
dog=Dog()
dog.sound()
print("---------------------------")
#program 2
class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    pass
car=Car()
car.start()
print("---------------------------")
#program 3
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
#program 4
class Animal:
    def sound(self):
        print("Animals make sounds")
class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog=Dog()
dog.sound()