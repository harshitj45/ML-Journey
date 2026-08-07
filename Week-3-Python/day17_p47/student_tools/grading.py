# ============================================
# Day 17 - Program 47 (Package Module)
# Topic: Grading Functions
# Concepts: functions inside a package module
# ============================================


def get_grade(marks):
    # I convert numeric marks into a letter grade.
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"


def get_status(marks):
    # I check if the marks are a pass or a fail.
    return "Pass" if marks >= 50 else "Fail"

