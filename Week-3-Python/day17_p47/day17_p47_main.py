# ============================================
# Day 17 - Program 47 (Main File)
# Topic: Using a Custom Package
# Concepts: package imports, dot notation,
#           from-package-module import
# ============================================

# I import specific modules from my package.
from student_tools import grading
from student_tools import formatting

# I also import functions directly from a module
# inside the package.
from student_tools.grading import get_status


# --- TESTING ---

students = [
    ("Harshit", 85),
    ("Priya", 92),
    ("Rahul", 45),
]

print("Student Report")
print("-" * 25)

for name, marks in students:
    clean_name = formatting.format_name(name)
    grade = grading.get_grade(marks)
    status = get_status(marks)
    line = formatting.format_report_line(clean_name, marks, grade)
    print(f"{line}  {status}")



    