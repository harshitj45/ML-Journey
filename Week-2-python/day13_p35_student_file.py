# ============================================
# Day 13 - Program 35
# Topic: Student File Manager
# Concepts: File write, read, append,
#           with statement, exception handling,
#           string split/strip
# ============================================


# File ka naam — ek jagah define karo
FILE_NAME = "students.txt"


def save_students(students):
    # students = list of dicts
    # File mein likhna — "w" mode
    try:
        with open(FILE_NAME, "w") as f:
            for s in students:
                # har student ek line — name,marks,dept
                line = f"{s['name']},{s['marks']},{s['dept']}\n"
                f.write(line)
        print(f"{len(students)} students saved!")

    except Exception as e:
        print(f"Save error: {e}")


def load_students():
    # File se padhna — "r" mode
    students = []
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                # har line ko split karo
                parts = line.strip().split(",")
                student = {
                    "name":  parts[0],
                    "marks": int(parts[1]),     # string to int
                    "dept":  parts[2]
                }
                students.append(student)
        print(f"{len(students)} students loaded!")

    except FileNotFoundError:
        print("File nahi mili! Pehle save karo.")

    except Exception as e:
        print(f"Load error: {e}")

    return students


def add_student(name, marks, dept):
    # File mein append karo — "a" mode
    try:
        with open(FILE_NAME, "a") as f:
            f.write(f"{name},{marks},{dept}\n")
        print(f"{name} added!")

    except Exception as e:
        print(f"Add error: {e}")


def show_all(students):
    if not students:
        print("Koi student nahi!")
        return
    print("\nSab students:")
    print("-" * 35)
    for s in students:
        print(f"  {s['name']:<10} {s['marks']:>5}  {s['dept']}")
    print("-" * 35)


# --- TESTING ---

# 1. Students banao
students = [
    {"name": "Harshit", "marks": 85, "dept": "CSE"},
    {"name": "Priya",   "marks": 92, "dept": "ECE"},
    {"name": "Rahul",   "marks": 67, "dept": "CSE"},
]

# 2. File mein save karo
save_students(students)

# 3. File se load karo
loaded = load_students()
show_all(loaded)

# 4. Ek aur add karo
add_student("Neha", 78, "ME")

# 5. Dobara load karo — Neha bhi hogi
loaded = load_students()
show_all(loaded)

# 6. File na mile toh:
import os
os.remove(FILE_NAME)        # file delete karo test ke liye
load_students()              # FileNotFoundError handle hoga