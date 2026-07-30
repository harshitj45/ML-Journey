# ---------------- Base Class ---------------- #

class Person:
    """Base class for all people in the college."""

    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age

    def display_details(self):
        print(f"ID   : {self.person_id}")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


# ---------------- Derived Class: Student ---------------- #

class Student(Person):

    def __init__(self, person_id, name, age, course, semester):
        super().__init__(person_id, name, age)
        self.course = course
        self.semester = semester

    def display_details(self):
        super().display_details()
        print(f"Course     : {self.course}")
        print(f"Semester   : {self.semester}")

    def study(self):
        print(f"{self.name} is studying.")


# ---------------- Derived Class: Teacher ---------------- #

class Teacher(Person):

    def __init__(self, person_id, name, age, subject, salary):
        super().__init__(person_id, name, age)
        self.subject = subject
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"Subject    : {self.subject}")
        print(f"Salary     : ₹{self.salary}")

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")


# ---------------- Main Program ---------------- #

student = Student(
    person_id=101,
    name="Harshit Jain",
    age=22,
    course="B.Tech CSE",
    semester=6
)

teacher = Teacher(
    person_id=201,
    name="Anil Kumar",
    age=40,
    subject="Python Programming",
    salary=80000
)

print("=" * 40)
print("STUDENT DETAILS")
print("=" * 40)
student.display_details()
student.study()

print("\n" + "=" * 40)
print("TEACHER DETAILS")
print("=" * 40)
teacher.display_details()
teacher.teach()




# ========================================
# STUDENT DETAILS
# ========================================
# ID   : 101
# Name : Harshit Jain
# Age  : 22
# Course     : B.Tech CSE
# Semester   : 6
# Harshit Jain is studying.

# ========================================
# TEACHER DETAILS
# ========================================
# ID   : 201
# Name : Anil Kumar
# Age  : 40
# Subject    : Python Programming
# Salary     : ₹80000
# Anil Kumar is teaching Python Programming.