class Person:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print("ID :", self.id)
        print("Name :", self.name)


class Student(Person):

    def __init__(self, id, name, course):
        super().__init__(id, name)
        self.course = course

    def display(self):
        super().display()
        print("Course :", self.course)


class Teacher(Person):

    def __init__(self, id, name, subject):
        super().__init__(id, name)
        self.subject = subject

    def display(self):
        super().display()
        print("Subject :", self.subject)


student = Student(101, "Harshit", "B.Tech")
teacher = Teacher(201, "Anil", "Python")

print("Student Details")
student.display()

print()

print("Teacher Details")
teacher.display()


# Student Details
# ID : 101
# Name : Harshit
# Course : B.Tech

# Teacher Details
# ID : 201
# Name : Anil
# Subject : Python