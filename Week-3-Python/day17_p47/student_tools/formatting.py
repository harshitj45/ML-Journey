# ============================================
# Day 17 - Program 47 (Package Module)
# Topic: Formatting Functions
# Concepts: functions inside a package module
# ============================================


def format_name(name):
    # I format a name in title case.
    return name.strip().title()


def format_report_line(name, marks, grade):
    # I build one formatted line for a report.
    return f"{name:<12} {marks:>5} {grade:>4}"

