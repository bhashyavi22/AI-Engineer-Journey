class Student:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
        
    def introduce(self):
        print(f"Hi, my name is {self.name}.")
        print(f"I am studying {self.branch}")

student1=Student("Bhashyavi","AI & ML")
    
student1.introduce()