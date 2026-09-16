def student_marks():
    students = {}

    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks

    print("\nStudent Marks:")

    for name, marks in students.items():
        print(name, ":", marks)


student_marks()