# ============================================
# Day 14 - Program 38
# Topic: Week 2 Mini Project — File Manager
# Concepts: File I/O, with statement,
#           exception handling, try/except/finally
# ============================================

# Note: day14_p37_core_classes.py se classes import karte hain
from day14_p37_core_classes import (
    Student, Teacher,
    InvalidMarksError, InvalidAgeError
)


class RecordManager:
    # File names — class variables
    STUDENT_FILE = "students.txt"
    TEACHER_FILE = "teachers.txt"

    def __init__(self):
        self.students = []
        self.teachers = []

    # ── STUDENT METHODS ──

    def add_student(self, name, age, dept, marks):
        try:
            s = Student(name, age, dept, marks)
            self.students.append(s)
            print(f"Added student: {name}")

        except InvalidMarksError as e:
            print(f"Student add failed: {e}")

        except InvalidAgeError as e:
            print(f"Student add failed: {e}")

    def save_students(self):
        # File mein write — Day 13
        try:
            with open(self.STUDENT_FILE, "w") as f:
                for s in self.students:
                    f.write(str(s) + "\n")  # __str__ use hoga
            print(f"Saved {len(self.students)} students")

        except Exception as e:
            print(f"Save failed: {e}")

        finally:
            print("Save attempt complete")   # hamesha chalega

    def load_students(self):
        # File se read — Day 13
        self.students = []
        try:
            with open(self.STUDENT_FILE, "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    # format: Student|name|age|dept|marks
                    if parts[0] == "Student":
                        self.add_student(
                            parts[1],           # name
                            int(parts[2]),      # age
                            parts[3],           # dept
                            int(parts[4])       # marks
                        )
            print(f"Loaded {len(self.students)} students")

        except FileNotFoundError:
            print(f"File nahi mili: {self.STUDENT_FILE}")

        except Exception as e:
            print(f"Load failed: {e}")

    # ── TEACHER METHODS ──

    def add_teacher(self, name, age, subject, experience):
        try:
            t = Teacher(name, age, subject, experience)
            self.teachers.append(t)
            print(f"Added teacher: {name}")

        except InvalidAgeError as e:
            print(f"Teacher add failed: {e}")

    def save_teachers(self):
        try:
            with open(self.TEACHER_FILE, "w") as f:
                for t in self.teachers:
                    f.write(str(t) + "\n")
            print(f"Saved {len(self.teachers)} teachers")

        except Exception as e:
            print(f"Save failed: {e}")

    def load_teachers(self):
        self.teachers = []
        try:
            with open(self.TEACHER_FILE, "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if parts[0] == "Teacher":
                        self.add_teacher(
                            parts[1],           # name
                            int(parts[2]),      # age
                            parts[3],           # subject
                            int(parts[4])       # experience
                        )
            print(f"Loaded {len(self.teachers)} teachers")

        except FileNotFoundError:
            print(f"File nahi mili: {self.TEACHER_FILE}")

        except Exception as e:
            print(f"Load failed: {e}")

    # ── DISPLAY METHODS ──

    def show_students(self):
        if not self.students:
            print("Koi student nahi!")
            return
        print("\n--- Students ---")
        print(f"{'Name':<12} {'Age':>4} {'Dept':<6} "
              f"{'Marks':>6} {'Grade':>6}")
        print("-" * 40)
        for s in sorted(self.students, reverse=True):
            print(f"  {s.name:<10} {s.age:>4} {s.dept:<6} "
                  f"{s.marks:>6} {s.grade:>6}")

    def show_teachers(self):
        if not self.teachers:
            print("Koi teacher nahi!")
            return
        print("\n--- Teachers ---")
        for t in self.teachers:
            print(f"  {t.name} | {t.subject} | {t.experience}yrs")


# --- TESTING ---

mgr = RecordManager()

# Students add karo
print("=== Adding Students ===")
mgr.add_student("Harshit", 21, "CSE", 85)
mgr.add_student("Priya",   20, "ECE", 92)
mgr.add_student("Rahul",   22, "CSE", 67)
mgr.add_student("Neha",    21, "ME",  78)
mgr.add_student("Invalid", 21, "CSE", 150)  # Error handle hoga

# Teachers add karo
print("\n=== Adding Teachers ===")
mgr.add_teacher("Dr. Sharma", 45, "Python", 15)
mgr.add_teacher("Prof. Gupta", 38, "ML", 10)

# Show karo
mgr.show_students()
mgr.show_teachers()

# File mein save karo
print("\n=== Saving ===")
mgr.save_students()
mgr.save_teachers()

# Nayi object mein load karo
print("\n=== Loading in new manager ===")
mgr2 = RecordManager()
mgr2.load_students()
mgr2.load_teachers()
mgr2.show_students()
mgr2.show_teachers()


