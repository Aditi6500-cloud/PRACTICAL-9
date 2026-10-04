# Student details using a simple class

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

student = Student("Aditi", 1)

print("Student Name:", student.name)
print("Roll Number:", student.roll_no)
