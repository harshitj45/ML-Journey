# ============================================
# Day 34 - Program 99
# Topic: Safe Editing with loc + Conditions
# Concepts: loc-based assignment, avoiding
#           SettingWithCopyWarning, combining
#           filtering with modification
# ============================================

import pandas as pd


def build_dataset() -> pd.DataFrame:
    # I build a small dataset to practice safe editing on.
    return pd.DataFrame({
        "name":  ["Harshit", "Priya", "Rahul", "Neha", "Arjun"],
        "marks": [85, 45, 92, 38, 78],
    })


def apply_bonus_safely(df: pd.DataFrame, threshold: int, bonus: int) -> pd.DataFrame:
    # I use loc with a condition to modify the original
    # DataFrame directly and safely, instead of editing
    # a filtered copy.
    df = df.copy()
    df.loc[df["marks"] >= threshold, "marks"] += bonus
    return df


def relabel_status(df: pd.DataFrame, passing_mark: int) -> pd.DataFrame:
    # I add a new column using loc-based conditional
    # assignment for two separate groups.
    df = df.copy()
    df.loc[df["marks"] >= passing_mark, "status"] = "Pass"
    df.loc[df["marks"] < passing_mark, "status"] = "Fail"
    return df


def cap_marks_safely(df: pd.DataFrame, max_marks: int) -> pd.DataFrame:
    # I cap any marks above a maximum, editing safely with loc.
    df = df.copy()
    df.loc[df["marks"] > max_marks, "marks"] = max_marks
    return df


# --- TESTING ---

students = build_dataset()

boosted = apply_bonus_safely(students, threshold=90, bonus=5)
print(f"After bonus:\n{boosted}")

labeled = relabel_status(students, passing_mark=50)
print(f"\nWith status:\n{labeled}")

capped = cap_marks_safely(students, max_marks=90)
print(f"\nCapped marks:\n{capped}")

# I confirm the original dataset was never accidentally changed.
print(f"\nOriginal untouched:\n{students}")

