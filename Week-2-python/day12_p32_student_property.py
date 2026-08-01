# ============================================
# Day 12 - Program 32
# Topic: Student class with @property
# Concepts: @property, @setter,
#           computed property, validation
# ============================================


class Student:

    def __init__(self, name, marks):
        self.name    = name
        self._marks  = marks        # _ = private convention

    @property
    def marks(self):
        # Getter — value return karo
        return self._marks

    @marks.setter
    def marks(self, value):
        # Setter — validation ke saath
        if value < 0 or value > 100:
            print(f"Invalid! Marks 0-100 hone chahiye. Got: {value}")
            return
        self._marks = value

    @property
    def grade(self):
        # Computed property — marks se calculate
        if self._marks >= 90:   return "A+"
        elif self._marks >= 80: return "A"
        elif self._marks >= 70: return "B"
        elif self._marks >= 60: return "C"
        elif self._marks >= 50: return "D"
        else:                   return "F"

    @property
    def status(self):
        # Computed property — pass ya fail
        return "Pass" if self._marks >= 50 else "Fail"

    def __str__(self):
        return (f"{self.name} | "
                f"Marks: {self._marks} | "
                f"Grade: {self.grade} | "
                f"{self.status}")


# --- TESTING ---

s1 = Student("Harshit", 85)
s2 = Student("Priya",   92)
s3 = Student("Rahul",   45)

# Getter:
print(s1.marks)         # 85

# Computed properties:
print(s1.grade)         # A
print(s1.status)        # Pass
print(s3.status)        # Fail

# __str__:
print(s1)
print(s2)
print(s3)

# Setter — valid:
s1.marks = 95
print(s1)               # Grade bhi change ho gaya!

# Setter — invalid:
s1.marks = 150          # Invalid! message aayega
s1.marks = -10          # Invalid! message aayega
print(s1.marks)         # 95 — change nahi hua

# List mein sab students:
students = [s1, s2, s3]
print("\nSab students:")
for s in students:
    print(f"  {s}")