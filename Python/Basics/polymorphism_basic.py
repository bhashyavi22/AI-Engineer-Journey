#program 1-Basic Polymorphism
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
print("\n---------------------------\n")

#program 2-Polymorphism using a Common Function
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
def animal_sound(animal):
    animal.sound()

dog=Dog()
cat=Cat()

animal_sound(dog)
animal_sound(cat)
