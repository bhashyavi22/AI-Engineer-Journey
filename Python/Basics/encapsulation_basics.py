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
