# ============================================
# Day 35 - Program 102
# Topic: Row-wise apply() and Performance Comparison
# Concepts: apply(axis=1), combining multiple columns,
#           apply() vs direct vectorized operations
# ============================================

import pandas as pd
import numpy as np
import time


def build_dataset() -> pd.DataFrame:
    # I build a dataset where the final score depends
    # on more than one column.
    return pd.DataFrame({
        "name":       ["Harshit", "Priya", "Rahul", "Neha"],
        "marks":      [85, 45, 92, 68],
        "attendance": [90, 60, 95, 80],
    })


def combined_score_row(row: pd.Series) -> float:
    # I calculate a weighted score using two columns from
    # the same row. This needs axis=1, since it reads
    # more than one column at once.
    return (row["marks"] * 0.7) + (row["attendance"] * 0.3)


def add_combined_score(df: pd.DataFrame) -> pd.DataFrame:
    # I apply my row-wise function across the whole DataFrame.
    df = df.copy()
    df["final_score"] = df.apply(combined_score_row, axis=1)
    return df


def add_combined_score_vectorized(df: pd.DataFrame) -> pd.DataFrame:
    # I calculate the exact same result without apply(),
    # using direct vectorized column operations instead.
    df = df.copy()
    df["final_score_v2"] = (df["marks"] * 0.7) + (df["attendance"] * 0.3)
    return df


def compare_speed(n_rows: int) -> dict:
    # I compare how long apply() takes versus a vectorized
    # operation on a larger dataset.
    big_df = pd.DataFrame({"marks": np.arange(n_rows)})

    start = time.time()
    big_df["apply_result"] = big_df["marks"].apply(lambda x: x * 2)
    apply_time = time.time() - start

    start = time.time()
    big_df["vectorized_result"] = big_df["marks"] * 2
    vectorized_time = time.time() - start

    return {"apply_time": apply_time, "vectorized_time": vectorized_time}


# --- TESTING ---

students = build_dataset()

with_row_apply = add_combined_score(students)
print(f"Using apply(axis=1):\n{with_row_apply}")

with_vectorized = add_combined_score_vectorized(with_row_apply)
print(f"\nUsing vectorized (same result):\n{with_vectorized}")

# I confirm both approaches give the same answer.
match = (with_vectorized["final_score"] == with_vectorized["final_score_v2"]).all()
print(f"\nBoth methods match: {match}")

speed = compare_speed(100000)
print(f"\nSpeed comparison on 100,000 rows: {speed}")
