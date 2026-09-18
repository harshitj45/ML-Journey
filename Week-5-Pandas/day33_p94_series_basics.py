# ============================================
# Day 33 - Program 94
# Topic: Pandas Series Basics
# Concepts: Series creation, custom index,
#           dict-to-Series, boolean indexing on Series
# ============================================

import pandas as pd


def create_marks_series(values: list) -> pd.Series:
    # I create a basic Series from a list of numbers.
    return pd.Series(values)


def create_labeled_series(values: list, labels: list) -> pd.Series:
    # I create a Series where I control the index labels,
    # so I can access values by name instead of position.
    return pd.Series(values, index=labels)


def series_from_dict(data: dict) -> pd.Series:
    # I create a Series directly from a dictionary.
    # The dict keys automatically become the index.
    return pd.Series(data)


def get_above_average(series: pd.Series) -> pd.Series:
    # I filter the Series using boolean indexing,
    # the same technique I used on NumPy arrays.
    return series[series > series.mean()]


def series_summary(series: pd.Series) -> dict:
    # I build a small summary using Series methods.
    return {
        "mean": series.mean(),
        "max": series.max(),
        "min": series.min(),
        "count": series.count(),
    }


# --- TESTING ---

marks = create_marks_series([85, 92, 78, 95, 60])
print(marks)

student_marks = create_labeled_series(
    [85, 92, 78],
    ["Harshit", "Priya", "Rahul"]
)
print(student_marks["Harshit"])

grade_counts = series_from_dict({"A": 5, "B": 12, "C": 8})
print(grade_counts)

above_avg = get_above_average(marks)
print(f"Above average marks: {above_avg.values}")

summary = series_summary(marks)
print(summary)

