# program 1- Public Member
class Student:
    def __init__(self):
        self.name="Bhashyavi"
student=Student()
print(student.name)
print("---------------------------")
# program 2 - Protected Member
class Student:
    def __init__(self):
        self._name="Bhashyavi"
student=Student()
print(student._name)
print("---------------------------")
# program 3 - Protected Member with Inheritance
class Student:
    def __init__(self):
        self._name="Bhashyavi"
class CollegeStudent(Student):
    def display(self):
        print(self._name)
student=CollegeStudent()
student.display()
print("---------------------------")
# program 4 - Private variable
class Student:
    def __init__(self):
        self.__name="Bhashyavi"
student=Student()
# print(student.__name)
# this gives AttributeError

# Name mangling (for learning only)
print(student._Student__name)
print("----------------------------")
# Program 5- by using getter method
class Student:
    def __init__(self):
        self.__name="Bhashyavi"
    def get_name(self):
        return self.__name
student=Student()
print(student.get_name())
print("----------------------------")
# Program 6 - Setter method
class Student:
    def __init__(self):
        self.__name="Bhashyavi"
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name

student=Student()
print(student.get_name())
student.set_name("Nitish")
print(student.get_name())
print("------------------------------")
# Program 7 - Setter Method with Validation

class Student:
    def __init__(self):
        self.__name = "Bhashyavi"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) >= 3:
            self.__name = name
        else:
            print("Invalid name")

student = Student()

print(student.get_name())

student.set_name("Nitish")
print(student.get_name())

student.set_name("r")
print(student.get_name())
print("-----------------------------")
