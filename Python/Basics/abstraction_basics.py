# Program 1 - Basic Abstract class
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog=Dog()
dog.sound()
print("--------------------------------")

# Program 2 - Multiple Child Classes
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")
dog = Dog()
cat = Cat()
dog.sound()
cat.sound()

# Program 3 - Shape Area

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(3.14 * self.radius * self.radius)


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(self.length * self.breadth)


circle = Circle(5)
rectangle = Rectangle(4, 6)

circle.area()
rectangle.area()
print("--------------------------------")

# Program 4 - Payment System

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class CreditCard(Payment):

    def pay(self):
        print("Payment made using Credit Card")


class UPI(Payment):

    def pay(self):
        print("Payment made using UPI")


credit = CreditCard()
upi = UPI()

credit.pay()
upi.pay()