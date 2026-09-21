# ============================================
# Day 35 - Program 101
# Topic: apply() on a Series
# Concepts: lambda with apply, named functions
#           with apply, chaining multiple apply calls
# ============================================

import pandas as pd


def build_dataset() -> pd.DataFrame:
    # I build a dataset of students to categorize.
    return pd.DataFrame({
        "name":  ["Harshit", "Priya", "Rahul", "Neha", "Arjun"],
        "marks": [85, 45, 92, 68, 55],
    })


def double_marks(df: pd.DataFrame) -> pd.DataFrame:
    # I apply a simple lambda to every value in the column.
    df = df.copy()
    df["doubled"] = df["marks"].apply(lambda x: x * 2)
    return df


def get_grade(marks: int) -> str:
    # I define this as a named function because the logic
    # has multiple branches, which would be awkward in a lambda.
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 50:
        return "B"
    else:
        return "F"


def add_grades(df: pd.DataFrame) -> pd.DataFrame:
    # I apply the named function to the marks column.
    df = df.copy()
    df["grade"] = df["marks"].apply(get_grade)
    return df


def clean_names(df: pd.DataFrame) -> pd.DataFrame:
    # I apply a string method through apply, to show it
    # works on text columns too, not just numbers.
    df = df.copy()
    df["name_upper"] = df["name"].apply(lambda x: x.upper())
    return df


# --- TESTING ---

students = build_dataset()

step1 = double_marks(students)
print(f"With doubled marks:\n{step1}")

step2 = add_grades(step1)
print(f"\nWith grades:\n{step2}")

step3 = clean_names(step2)
print(f"\nWith uppercase names:\n{step3}")
