class Student:
    def __init__(self,name,branch,year):
        self.name=name
        self.branch=branch
        self.year=year
    def details(self):
        print(f"Name : {self.name}")
        print(f"Branch : {self.branch}")
        print(f"Year : {self.year}")
student1=Student("Bhashyavi","AI & ML",3)
student2=Student("Harshith","ECE",1)
student1.details()
student2.details()

        