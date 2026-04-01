# Mini Project — 
# Author: Harshit
# Topics used: Variables, Strings, Lists, Dicts, Sets, Comprehensions, Loops,Functions (preview of Week 2)

import os

# =====================
# DATA
# =====================

students = {
    "Harshit": {
        "marks": [85, 92, 78, 95, 60],
        "city": "Delhi",
        "dept": "CSE"
    },
    "Priya": {
        "marks": [90, 88, 95, 92, 97],
        "city": "Mumbai",
        "dept": "ECE"
    },
    "Rahul": {
        "marks": [45, 55, 40, 60, 50],
        "city": "Chennai",
        "dept": "CSE"
    },
    "Neha": {
        "marks": [78, 82, 88, 75, 80],
        "city": "Delhi",
        "dept": "ME"
    },
    "Arjun": {
        "marks": [62, 70, 58, 74, 66],
        "city": "Mumbai",
        "dept": "CSE"
    },
    "Sneha": {
        "marks": [95, 98, 92, 96, 99],
        "city": "Delhi",
        "dept": "CSE"
    },
}

SUBJECTS = ["Maths", "Python",
            "DSA", "OS", "CN"]

PASSING_MARKS = 50
TOTAL_MARKS   = 100



# =====================
# CORE FUNCTIONS
# =====================

def calculate_average(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)


def get_grade(average):
    """
    Return grade based on average.
    A+ = 90+, A = 80+, B = 70+,
    C = 60+, D = 50+, F = below 50
    """
    if average >= 90:   return "A+"
    elif average >= 80: return "A"
    elif average >= 70: return "B"
    elif average >= 60: return "C"
    elif average >= 50: return "D"
    else:               return "F"


def get_status(average):
    """Pass if average >= passing marks."""
    return "PASS" if average >= PASSING_MARKS \
           else "FAIL"


def get_highest_subject(marks):
    """Return subject name with highest marks."""
    highest_idx = 0
    for i in range(1, len(marks)):
        if marks[i] > marks[highest_idx]:
            highest_idx = i
    return SUBJECTS[highest_idx], marks[highest_idx]


def get_lowest_subject(marks):
    """Return subject name with lowest marks."""
    lowest_idx = 0
    for i in range(1, len(marks)):
        if marks[i] < marks[lowest_idx]:
            lowest_idx = i
    return SUBJECTS[lowest_idx], marks[lowest_idx]


def calculate_percentage(average):
    """Convert average to percentage."""
    return (average / TOTAL_MARKS) * 100



# =====================
# DISPLAY FUNCTIONS
# =====================

def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_divider(char="=", length=55):
    """Print a divider line."""
    print(char * length)


def print_report_card(name, data):
    """
    Print detailed report card for one student.
    Uses: f-strings, loops, conditions.
    """
    marks   = data["marks"]
    avg     = calculate_average(marks)
    grade   = get_grade(avg)
    status  = get_status(avg)
    percent = calculate_percentage(avg)
    high_sub, high_mark = get_highest_subject(marks)
    low_sub,  low_mark  = get_lowest_subject(marks)

    print_divider()
    print(f"{'REPORT CARD':^55}")
    print_divider()
    print(f"  Student Name : {name}")
    print(f"  Department   : {data['dept']}")
    print(f"  City         : {data['city']}")
    print_divider("-")
    print(f"  {'Subject':<12} {'Marks':>6} "
          f"{'Out Of':>8} {'Status':>8}")
    print_divider("-")

    for subject, mark in zip(SUBJECTS, marks):
        sub_status = "Pass" if mark >= PASSING_MARKS \
                     else "FAIL"
        # Highlight failing subjects
        flag = " ⚠" if mark < PASSING_MARKS else ""
        print(f"  {subject:<12} {mark:>6} "
              f"{TOTAL_MARKS:>8} "
              f"{sub_status:>8}{flag}")

    print_divider("-")
    print(f"  {'Total':<12} "
          f"{sum(marks):>6} "
          f"{TOTAL_MARKS * len(marks):>8}")
    print(f"  {'Average':<12} {avg:>6.1f}")
    print(f"  {'Percentage':<12} {percent:>5.1f}%")
    print(f"  {'Grade':<12} {grade:>6}")
    print(f"  {'Result':<12} {status:>6}")
    print_divider("-")
    print(f"  Best Subject : "
          f"{high_sub} ({high_mark})")
    print(f"  Weak Subject : "
          f"{low_sub} ({low_mark})")
    print_divider()


def print_all_students(students):
    """
    Print summary table of all students.
    Uses: loops, f-strings, sorting.
    """
    print_divider()
    print(f"{'ALL STUDENTS SUMMARY':^55}")
    print_divider()
    print(f"  {'Name':<10} {'Avg':>6} "
          f"{'Grade':>6} {'%':>7} "
          f"{'Status':>6} {'Dept':<5}")
    print_divider("-")

    for name, data in students.items():
        avg     = calculate_average(data["marks"])
        grade   = get_grade(avg)
        status  = get_status(avg)
        percent = calculate_percentage(avg)

        print(f"  {name:<10} {avg:>6.1f} "
              f"{grade:>6} {percent:>6.1f}% "
              f"{status:>6} {data['dept']:<5}")

    print_divider()
    print(f"  Total Students: {len(students)}")
    passed = sum(
        1 for d in students.values()
        if get_status(
            calculate_average(d["marks"])
        ) == "PASS"
    )
    print(f"  Passed: {passed} | "
          f"Failed: {len(students) - passed}")
    print_divider()




# =====================
# ANALYSIS FUNCTIONS
# =====================

def get_rankings(students):
    """
    Rank students by average — descending.
    Uses: loops, sorting logic.
    """
    # Build list of (name, average) tuples
    student_avgs = []
    for name, data in students.items():
        avg = calculate_average(data["marks"])
        student_avgs.append((name, avg))

    # Sort by average descending (manual)
    for i in range(len(student_avgs)):
        for j in range(i+1, len(student_avgs)):
            if student_avgs[j][1] > \
               student_avgs[i][1]:
                student_avgs[i], \
                student_avgs[j] = \
                student_avgs[j], \
                student_avgs[i]

    return student_avgs


def print_rankings(students):
    """Print ranked leaderboard."""
    rankings = get_rankings(students)

    print_divider()
    print(f"{'CLASS RANKINGS':^55}")
    print_divider()
    print(f"  {'Rank':<6} {'Name':<12} "
          f"{'Average':>8} {'Grade':>6}")
    print_divider("-")

    medals = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th"}

    for rank, (name, avg) in \
            enumerate(rankings, 1):
        grade  = get_grade(avg)
        medal  = medals.get(rank, f"  {rank}.")
        print(f"  {medal:<6} {name:<12} "
              f"{avg:>8.1f} {grade:>6}")

    print_divider()


def get_class_stats(students):
    """
    Calculate class-wide statistics.
    Uses: loops, conditions, dicts.
    """
    all_avgs = []
    for name, data in students.items():
        avg = calculate_average(data["marks"])
        all_avgs.append(avg)

    # Manual statistics
    class_avg = sum(all_avgs) / len(all_avgs)

    # Max and min
    class_max = all_avgs[0]
    class_min = all_avgs[0]
    for avg in all_avgs:
        if avg > class_max: class_max = avg
        if avg < class_min: class_min = avg

    # Pass/Fail count
    passed = sum(1 for a in all_avgs
                 if a >= PASSING_MARKS)
    failed = len(all_avgs) - passed

    # Grade distribution
    grade_dist = {}
    for avg in all_avgs:
        grade = get_grade(avg)
        grade_dist[grade] = \
            grade_dist.get(grade, 0) + 1

    return {
        "class_avg": class_avg,
        "highest":   class_max,
        "lowest":    class_min,
        "passed":    passed,
        "failed":    failed,
        "grade_dist": grade_dist,
        "total":     len(all_avgs)
    }


def print_class_stats(students):
    """Print class statistics report."""
    stats = get_class_stats(students)

    print_divider()
    print(f"{'CLASS STATISTICS':^55}")
    print_divider()
    print(f"  Total Students : {stats['total']}")
    print(f"  Class Average  : "
          f"{stats['class_avg']:.2f}")
    print(f"  Highest Average: "
          f"{stats['highest']:.2f}")
    print(f"  Lowest Average : "
          f"{stats['lowest']:.2f}")
    print(f"  Passed         : "
          f"{stats['passed']}")
    print(f"  Failed         : "
          f"{stats['failed']}")
    print(f"  Pass Rate      : "
          f"{stats['passed']/stats['total']*100:.1f}%")

    print_divider("-")
    print(f"  Grade Distribution:")
    for grade in ["A+","A","B","C","D","F"]:
        count = stats["grade_dist"].get(grade, 0)
        bar   = "█" * count
        print(f"    {grade:>3}: {bar} ({count})")
    print_divider()


def subject_analysis(students):
    """
    Analyze performance per subject.
    Uses: nested loops, dicts, comprehensions.
    """
    # Collect all marks per subject
    subject_marks = {sub: [] for sub in SUBJECTS}

    for name, data in students.items():
        for i, mark in enumerate(data["marks"]):
            subject_marks[SUBJECTS[i]].append(mark)

    print_divider()
    print(f"{'SUBJECT-WISE ANALYSIS':^55}")
    print_divider()
    print(f"  {'Subject':<12} {'Avg':>6} "
          f"{'Max':>5} {'Min':>5} "
          f"{'Pass%':>7}")
    print_divider("-")

    for subject, marks in subject_marks.items():
        avg    = sum(marks) / len(marks)
        high   = max(marks)
        low    = min(marks)
        passed = sum(1 for m in marks
                     if m >= PASSING_MARKS)
        pass_pct = passed / len(marks) * 100

        print(f"  {subject:<12} {avg:>6.1f} "
              f"{high:>5} {low:>5} "
              f"{pass_pct:>6.1f}%")

    print_divider()

    # Hardest subject (lowest avg)
    hardest = min(subject_marks,
                  key=lambda s:
                  sum(subject_marks[s]) /
                  len(subject_marks[s]))
    print(f"  Hardest Subject: {hardest}")

    # Easiest subject (highest avg)
    easiest = max(subject_marks,
                  key=lambda s:
                  sum(subject_marks[s]) /
                  len(subject_marks[s]))
    print(f"  Easiest Subject: {easiest}")
    print_divider()




# =====================
# MENU + MAIN
# =====================

def search_student(students, name):
    """Search student by name."""
    # Case-insensitive search
    for student_name in students:
        if student_name.lower() == name.lower():
            return student_name
    return None


def print_menu():
    """Print main menu."""
    print_divider()
    print(f"{'STUDENT GRADE MANAGEMENT SYSTEM v1.0':^55}")
    print(f"{'by Harshit':^55}")
    print_divider()
    print("  1. View All Students")
    print("  2. View Report Card")
    print("  3. Class Rankings")
    print("  4. Class Statistics")
    print("  5. Subject Analysis")
    print("  6. Find Topper")
    print("  0. Exit")
    print_divider()


def main():
    """
    Main function — menu-driven CLI app.
    Uses: while loop, conditions, all functions.
    """
    while True:
        print_menu()
        choice = input("  Enter choice (0-6): ").strip()

        if choice == "0":
            print("\n")
            print("=" * 70)
            print("      Thank you for using the Student Grade Management System!")
            print("\n                      HAVE A NICE DAY!")
            print("=" * 70)
            break

        elif choice == "1":
            print_all_students(students)

        elif choice == "2":
            name = input(
                "\n  Enter student name: "
            ).strip()
            found = search_student(students, name)

            if found:
                print_report_card(
                    found, students[found]
                )
            else:
                print(f"\n  ❌ '{name}' not found!")
                print("  Available students:")
                for n in students:
                    print(f"    - {n}")

        elif choice == "3":
            print_rankings(students)

        elif choice == "4":
            print_class_stats(students)

        elif choice == "5":
            subject_analysis(students)

        elif choice == "6":
            rankings = get_rankings(students)
            topper_name, topper_avg = rankings[0]
            print_divider()
            print(f"{'CLASS TOPPER':^55}")
            print_divider()
            print(f"  Name    : {topper_name}")
            print(f"  Average : {topper_avg:.2f}")
            print(f"  Grade   : "
                  f"{get_grade(topper_avg)}")
            print(f"  Dept    : "
                  f"{students[topper_name]['dept']}")
            print_divider()

        else:
            print("\n  ❌ Invalid choice! Enter 0-6.")
        
        
        input("\n  Press Enter to continue...")
            



# =====================
# RUN
# =====================
if __name__ == "__main__":
    main()


