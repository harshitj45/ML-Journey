# ============================================
# Day 34 - Program 98
# Topic: Multi-Condition Filtering
# Concepts: combining conditions with & | ~,
#           isin(), loc with column selection
# ============================================

import pandas as pd


def build_dataset() -> pd.DataFrame:
    # I build a dataset to practice filtering on.
    return pd.DataFrame({
        "name":  ["Harshit", "Priya", "Rahul", "Neha", "Arjun", "Sneha"],
        "marks": [85, 45, 92, 38, 78, 95],
        "city":  ["Delhi", "Mumbai", "Delhi", "Chennai", "Mumbai", "Delhi"],
        "dept":  ["CSE", "ECE", "CSE", "ME", "CSE", "ECE"],
    })


def filter_and(df: pd.DataFrame, min_marks: int, city: str) -> pd.DataFrame:
    # I combine two conditions using & — both must be true.
    return df[(df["marks"] >= min_marks) & (df["city"] == city)]


def filter_or(df: pd.DataFrame, low: int, high: int) -> pd.DataFrame:
    # I combine two conditions using | — either can be true.
    return df[(df["marks"] < low) | (df["marks"] > high)]


def filter_not(df: pd.DataFrame, city: str) -> pd.DataFrame:
    # I invert a condition using ~.
    return df[~(df["city"] == city)]


def filter_multiple_values(df: pd.DataFrame, cities: list) -> pd.DataFrame:
    # I check membership in a list of values using isin().
    return df[df["city"].isin(cities)]


def get_names_of_passed(df: pd.DataFrame, passing_mark: int) -> pd.Series:
    # I select just one column, only for rows matching a condition.
    return df.loc[df["marks"] >= passing_mark, "name"]


# --- TESTING ---

data = build_dataset()

delhi_cse = filter_and(data, 50, "Delhi")
print(f"Delhi + passed:\n{delhi_cse}")

extremes = filter_or(data, 50, 90)
print(f"\nExtreme scores:\n{extremes}")

not_delhi = filter_not(data, "Delhi")
print(f"\nNot Delhi:\n{not_delhi}")

metro_students = filter_multiple_values(data, ["Delhi", "Mumbai"])
print(f"\nMetro cities:\n{metro_students}")

passed_names = get_names_of_passed(data, 50)
print(f"\nPassed names:\n{passed_names}")

