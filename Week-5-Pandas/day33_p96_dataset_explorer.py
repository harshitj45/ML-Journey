# ============================================
# Day 33 - Program 96
# Topic: Exploring a DataFrame
# Concepts: head, tail, shape, dtypes, info,
#           describe, column selection
# ============================================

import pandas as pd


def build_student_dataset() -> pd.DataFrame:
    # I build a small student dataset to explore.
    return pd.DataFrame({
        "name":       ["Harshit", "Priya", "Rahul", "Neha", "Arjun", "Sneha"],
        "age":        [21, 20, 22, 21, 23, 20],
        "marks":      [85, 92, 78, 88, 60, 95],
        "city":       ["Delhi", "Mumbai", "Chennai", "Delhi", "Mumbai", "Delhi"],
        "dept":       ["CSE", "ECE", "CSE", "ME", "CSE", "ECE"],
    })


def quick_overview(df: pd.DataFrame) -> None:
    # I print the standard first-look exploration steps.
    print("First 3 rows:")
    print(df.head(3))
    print(f"\nShape: {df.shape}")
    print(f"\nColumn types:\n{df.dtypes}")


def numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    # I get statistics for every numeric column at once.
    return df.describe()


def select_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    # I select multiple columns at once using double brackets.
    return df[columns]


def get_single_column_stats(df: pd.DataFrame, column: str) -> dict:
    # I calculate stats for one column using Series methods.
    col = df[column]
    return {
        "mean": col.mean(),
        "std": col.std(),
        "max": col.max(),
        "min": col.min(),
    }


# --- TESTING ---

students = build_student_dataset()

quick_overview(students)

print("\nFull info:")
students.info()

print("\nDescribe (numeric columns only):")
print(numeric_summary(students))

subset = select_columns(students, ["name", "marks", "dept"])
print(f"\nSelected columns:\n{subset}")

marks_stats = get_single_column_stats(students, "marks")
print(f"\nMarks statistics: {marks_stats}")
