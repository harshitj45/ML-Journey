# ============================================
# Day 35 - Program 100
# Topic: Adding, Renaming, and Dropping Columns
# Concepts: computed columns, np.where on Series,
#           rename(), drop(), inplace behavior
# ============================================

import pandas as pd
import numpy as np


def build_dataset() -> pd.DataFrame:
    # I build a small dataset with a column I'll clean up later.
    return pd.DataFrame({
        "nm":       ["Harshit", "Priya", "Rahul", "Neha"],
        "marks":    [85, 45, 92, 68],
        "temp_col": [1, 1, 1, 1],
    })


def add_computed_columns(df: pd.DataFrame) -> pd.DataFrame:
    # I add a bonus column and a computed total from it.
    df = df.copy()
    df["bonus"] = 5
    df["total"] = df["marks"] + df["bonus"]
    return df


def add_status_column(df: pd.DataFrame) -> pd.DataFrame:
    # I use np.where to add a Pass/Fail column, the same
    # way I used np.where on plain NumPy arrays in Day 31.
    df = df.copy()
    df["status"] = np.where(df["marks"] >= 50, "Pass", "Fail")
    return df


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    # I rename columns using a dictionary mapping.
    return df.rename(columns={"nm": "name"})


def drop_unwanted_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    # I drop one or more columns I no longer need.
    return df.drop(columns=columns)


def drop_failing_rows(df: pd.DataFrame) -> pd.DataFrame:
    # I drop rows where a student failed, using boolean
    # indexing to find the row labels first.
    failing_index = df[df["marks"] < 50].index
    return df.drop(index=failing_index)


# --- TESTING ---

data = build_dataset()
print(f"Original:\n{data}")

with_bonus = add_computed_columns(data)
print(f"\nWith bonus + total:\n{with_bonus}")

with_status = add_status_column(with_bonus)
print(f"\nWith status:\n{with_status}")

renamed = rename_columns(with_status)
print(f"\nRenamed:\n{renamed}")

cleaned = drop_unwanted_columns(renamed, ["temp_col"])
print(f"\nDropped temp_col:\n{cleaned}")

passed_only = drop_failing_rows(cleaned)
print(f"\nOnly passed rows:\n{passed_only}")

