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