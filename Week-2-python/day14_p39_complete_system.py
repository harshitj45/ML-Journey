# ============================================
# Day 14 - Program 39
# Topic: Week 2 Mini Project — Complete System
# Concepts: Sab Week 2 concepts ek saath
#           Menu-driven CLI app
# ============================================

from day14_p37_core_classes import (
    Student, Teacher,
    InvalidMarksError, InvalidAgeError
)
from day14_p38_file_manager import RecordManager


def print_header():
    print("\n" + "=" * 40)
    print("   STUDENT RECORD SYSTEM")
    print("   Week 2 Mini Project")
    print("=" * 40)


def print_menu():
    print("\n1. Add Student")
    print("2. Add Teacher")
    print("3. Show All Students")
    print("4. Show All Teachers")
    print("5. Save Records")
    print("6. Load Records")
    print("0. Exit")
    print("-" * 40)


def get_student_input():
    # Input lena aur validate karna
    try:
        name  = input("Name: ").strip()
        age   = int(input("Age: "))
        dept  = input("Dept (CSE/ECE/ME): ").strip()
        marks = int(input("Marks (0-100): "))
        return name, age, dept, marks

    except ValueError:
        print("Invalid input! Numbers sahi daalo.")
        return None


def get_teacher_input():
    try:
        name  = input("Name: ").strip()
        age   = int(input("Age: "))
        subj  = input("Subject: ").strip()
        exp   = int(input("Experience (years): "))
        return name, age, subj, exp

    except ValueError:
        print("Invalid input! Numbers sahi daalo.")
        return None


def run_system():
    print_header()
    mgr = RecordManager()

    # Pehle load karo — agar file hai toh
    mgr.load_students()
    mgr.load_teachers()

    while True:
        print_menu()

        try:
            choice = input("Choice: ").strip()

        except KeyboardInterrupt:
            print("\nBye!")
            break

        if choice == "1":
            print("\n-- Add Student --")
            result = get_student_input()
            if result:
                mgr.add_student(*result)    # unpack tuple

        elif choice == "2":
            print("\n-- Add Teacher --")
            result = get_teacher_input()
            if result:
                mgr.add_teacher(*result)

        elif choice == "3":
            mgr.show_students()

        elif choice == "4":
            mgr.show_teachers()

        elif choice == "5":
            mgr.save_students()
            mgr.save_teachers()

        elif choice == "6":
            mgr.load_students()
            mgr.load_teachers()

        elif choice == "0":
            # Exit karne se pehle save karo
            mgr.save_students()
            mgr.save_teachers()
            print("Records saved. Goodbye!")
            break

        else:
            print("Invalid choice! 0-6 daalo.")


# --- RUN ---
run_system()


