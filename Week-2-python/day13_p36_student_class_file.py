# ============================================
# Day 13 - Program 36
# Topic: Student Class with File + Exceptions
# Concepts: OOP + File I/O + Exception Handling
#           sab ek saath — integration
# ============================================


# Custom exceptions
class InvalidMarksError(Exception):
    pass

class StudentNotFoundError(Exception):
    pass


class Student:

    def __init__(self, name, marks, dept):
        self.name = name
        self.dept = dept
        self._marks = None          # property use karenge
        self.marks = marks          # setter call hoga

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        # validation — @property se seekha
        if value < 0 or value > 100:
            raise InvalidMarksError(
                f"Marks {value} invalid! 0-100 hone chahiye."
            )
        self._marks = value

    @property
    def grade(self):
        # computed property
        if self._marks >= 90:   return "A+"
        elif self._marks >= 80: return "A"
        elif self._marks >= 70: return "B"
        elif self._marks >= 60: return "C"
        else:                   return "F"

    def __str__(self):
        return f"{self.name},{self._marks},{self.dept}"


class StudentManager:

    FILE = "student_data.txt"

    def __init__(self):
        self.students = []

    def add(self, name, marks, dept):
        try:
            s = Student(name, marks, dept)  # InvalidMarksError aa sakti hai
            self.students.append(s)
            print(f"Added: {name}")

        except InvalidMarksError as e:
            print(f"Error adding {name}: {e}")

    def save(self):
        try:
            with open(self.FILE, "w") as f:
                for s in self.students:
                    f.write(str(s) + "\n")   # __str__ use hoga
            print(f"Saved {len(self.students)} students")

        except Exception as e:
            print(f"Save failed: {e}")

    def load(self):
        self.students = []
        try:
            with open(self.FILE, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    name  = parts[0]
                    marks = int(parts[1])
                    dept  = parts[2]
                    self.add(name, marks, dept)

        except FileNotFoundError:
            print("File nahi mili!")

        except Exception as e:
            print(f"Load failed: {e}")

    def show_all(self):
        if not self.students:
            print("Koi student nahi!")
            return
        print("\n--- All Students ---")
        for s in self.students:
            print(f"  {s.name:<10} {s.marks:>5}  "
                  f"{s.dept:<5}  Grade: {s.grade}")


# --- TESTING ---

mgr = StudentManager()

# Add students — valid:
mgr.add("Harshit", 85, "CSE")
mgr.add("Priya",   92, "ECE")
mgr.add("Rahul",   67, "CSE")

# Add student — invalid marks:
mgr.add("Error",  150, "CSE")   # InvalidMarksError handle hoga

# Show:
mgr.show_all()

# Save to file:
mgr.save()

# Load from file:
mgr2 = StudentManager()
mgr2.load()
mgr2.show_all()