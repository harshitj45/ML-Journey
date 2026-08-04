# ============================================
# Day 14 - Program 37
# Topic: Week 2 Mini Project — Core Classes
# Concepts: Abstract class, Inheritance,
#           super(), @property, dunder methods
# ============================================

from abc import ABC, abstractmethod


# Custom exceptions — Day 13
class InvalidMarksError(Exception):
    pass

class InvalidAgeError(Exception):
    pass


# Abstract base class — Day 12
class Person(ABC):

    # Class variable — Day 10
    institution = "TMU Moradabad"

    def __init__(self, name, age):
        self.name  = name
        self._age  = None       # private — @property use karenge
        self.age   = age        # setter call hoga

    @property
    def age(self):
        # Getter — Day 12
        return self._age

    @age.setter
    def age(self, value):
        # Setter with validation — Day 12
        if value < 5 or value > 100:
            raise InvalidAgeError(
                f"Age {value} invalid! 5-100 hona chahiye."
            )
        self._age = value

    @abstractmethod
    def details(self):
        # Child ZAROOR implement kare — Day 12
        pass

    @abstractmethod
    def __str__(self):
        # Child ZAROOR implement kare
        pass

    def introduce(self):
        # Normal method — child override karna zaroor nahi
        print(f"Hi! Main {self.name} hoon.")
        print(f"Institution: {self.institution}")


# Child class 1 — Day 11
class Student(Person):

    def __init__(self, name, age, dept, marks):
        super().__init__(name, age)     # Parent ka __init__
        self.dept   = dept
        self._marks = None              # private
        self.marks  = marks             # setter call

    @property
    def marks(self):
        # Getter
        return self._marks

    @marks.setter
    def marks(self, value):
        # Validation
        if value < 0 or value > 100:
            raise InvalidMarksError(
                f"Marks {value} invalid! 0-100 hone chahiye."
            )
        self._marks = value

    @property
    def grade(self):
        # Computed property — no setter
        if self._marks >= 90:   return "A+"
        elif self._marks >= 80: return "A"
        elif self._marks >= 70: return "B"
        elif self._marks >= 60: return "C"
        else:                   return "F"

    def details(self):
        # abstractmethod implement kiya
        print(f"Name  : {self.name}")
        print(f"Age   : {self.age}")
        print(f"Dept  : {self.dept}")
        print(f"Marks : {self.marks}")
        print(f"Grade : {self.grade}")

    def __str__(self):
        # abstractmethod implement kiya
        return f"Student|{self.name}|{self.age}|{self.dept}|{self.marks}"

    def __gt__(self, other):
        # Dunder — marks compare — Day 10
        return self.marks > other.marks


# Child class 2 — Day 11
class Teacher(Person):

    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)     # Parent ka __init__
        self.subject    = subject
        self.experience = experience

    def details(self):
        # abstractmethod implement kiya
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Subject    : {self.subject}")
        print(f"Experience : {self.experience} years")

    def __str__(self):
        # abstractmethod implement kiya
        return f"Teacher|{self.name}|{self.age}|{self.subject}|{self.experience}"


# --- TESTING ---

print("=== Students ===")
s1 = Student("Harshit", 21, "CSE", 85)
s2 = Student("Priya",   20, "ECE", 92)
s3 = Student("Rahul",   22, "CSE", 67)

s1.details()
print()
s2.details()

# Dunder comparison
print(f"\nPriya > Harshit: {s2 > s1}")  # True

# sorted() — __gt__ se kaam chalega
students = [s1, s2, s3]
print("\nMarks descending:")
for s in sorted(students, reverse=True):
    print(f"  {s.name}: {s.marks} ({s.grade})")

print("\n=== Teachers ===")
t1 = Teacher("Dr. Sharma", 45, "Python", 15)
t1.details()

# introduce() — Person se mila
print()
s1.introduce()

# isinstance — Day 11
print(f"\nHarshit is Student: {isinstance(s1, Student)}")   # True
print(f"Harshit is Person : {isinstance(s1, Person)}")    # True

# Invalid input — exception handle hoga
print("\n=== Invalid Input Tests ===")
try:
    bad = Student("Error", 21, "CSE", 150)  # marks 150 invalid
except InvalidMarksError as e:
    print(f"Caught: {e}")

try:
    bad = Student("Error", 200, "CSE", 85)  # age 200 invalid
except InvalidAgeError as e:
    print(f"Caught: {e}")



