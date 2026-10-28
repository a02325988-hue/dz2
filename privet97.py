def func1():
    pass

class Student:
    print("hi")
    amount_of_students = 0
    def __init__(self, height = 160): 
        self.height = height
        print("hello")
        Student.amount_of_students += 1
    def grow(self,height = 1):
        self.height += height

print(Student.amount_of_students)
first_student = Student()
print(Student.amount_of_students)
second_student = Student(height=360)
print(first_student.height)
print(second_student.height)
print(Student.amount_of_students)
print(f"Amount of students in second student: {second_student.amount_of_students}")
print(f"Amount of students in second student: {second_student.amount_of_students}")
print("lets grow")
first_student.grow(250)
second_student.grow(-50)
print(f"First student: {first_student.height}")
print(f"Second student: {second_student.height}")