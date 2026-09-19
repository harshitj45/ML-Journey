# ============================================
# Day 34 - Program 97
# Topic: loc vs iloc Deep Dive
# Concepts: position vs label access, custom index,
#           index breaking after filtering, inclusive
#           vs exclusive slicing
# ============================================

import pandas as pd


def build_student_df() -> pd.DataFrame:
    # I build a small dataset with a default integer index.
    return pd.DataFrame({
        "name":  ["Harshit", "Priya", "Rahul", "Neha", "Arjun"],
        "marks": [85, 45, 92, 38, 78],
    })


def set_name_as_index(df: pd.DataFrame) -> pd.DataFrame:
    # I switch the index to the name column, so loc will
    # now use names instead of numbers.
    return df.set_index("name")


def compare_loc_iloc_after_filter(df: pd.DataFrame) -> dict:
    # I filter the dataset and then show how loc and iloc
    # diverge once the original row labels are no longer
    # in a simple 0,1,2... sequence.
    passed = df[df["marks"] >= 50]
    return {
        "passed_index": list(passed.index),
        "iloc_1": passed.iloc[1]["marks"],
        "loc_2": passed.loc[2]["marks"] if 2 in passed.index else None,
    }


def compare_slicing(df: pd.DataFrame) -> dict:
    # I compare how many rows iloc and loc slicing return
    # for the "same-looking" range.
    return {
        "iloc_1_to_3": len(df.iloc[1:3]),
        "loc_1_to_3": len(df.loc[1:3]),
    }


# --- TESTING ---

students = build_student_df()

by_name = set_name_as_index(students)
print(by_name.loc["Harshit"])
print(by_name.iloc[0])

comparison = compare_loc_iloc_after_filter(students)
print(comparison)

slice_comparison = compare_slicing(students)
print(slice_comparison)