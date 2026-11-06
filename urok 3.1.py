class Human:
    height = 170

class Student(Human):
    satiety = 0
class Worker(Human):
    satiety = 100

var1 = Human()
var2 = Student()
var3 = Worker()

print(var1.height)
print(var2.height)
print(var3.height)

print(var2.satiety)
print(var3.satiety)

class Grandparent:
    height = 170
    satiety = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 150
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)
