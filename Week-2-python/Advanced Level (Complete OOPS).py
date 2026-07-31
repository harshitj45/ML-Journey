from abc import ABC, abstractmethod


# ---------------- Abstract Class ---------------- #

class Person(ABC):

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.__age = age          # Encapsulation (Private Variable)

    def show_basic_info(self):
        print("ID :", self.id)
        print("Name :", self.name)
        print("Age :", self.__age)

    @abstractmethod
    def role(self):
        pass


# ---------------- Student ---------------- #

class Student(Person):

    def __init__(self, id, name, age, course, cgpa):
        super().__init__(id, name, age)
        self.course = course
        self.cgpa = cgpa

    def role(self):
        print("Role : Student")

    def display(self):
        self.show_basic_info()
        print("Course :", self.course)
        print("CGPA :", self.cgpa)


# ---------------- Teacher ---------------- #

class Teacher(Person):

    def __init__(self, id, name, age, subject, salary):
        super().__init__(id, name, age)
        self.subject = subject
        self.salary = salary

    def role(self):
        print("Role : Teacher")

    def display(self):
        self.show_basic_info()
        print("Subject :", self.subject)
        print("Salary :", self.salary)


# ---------------- Polymorphism ---------------- #

people = [

    Student(101, "Harshit", 22, "B.Tech CSE", 8.7),

    Teacher(201, "Anil", 40, "Python", 60000)

]

for person in people:

    print("=" * 30)

    person.role()

    person.display()





# ==============================
# Role : Student
# ID : 101
# Name : Harshit
# Age : 22
# Course : B.Tech CSE
# CGPA : 8.7

# ==============================
# Role : Teacher
# ID : 201
# Name : Anil
# Age : 40
# Subject : Python
# Salary : 60000