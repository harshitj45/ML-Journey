# ============================================
# Day 37 - Program 107
# Topic: Detecting and Removing Duplicates
# Concepts: duplicated(), drop_duplicates(),
#           keep parameter, subset-based dedup,
#           keeping the latest record per group
# ============================================

import pandas as pd


def build_dataset() -> pd.DataFrame:
    # I build a dataset with repeated user records at
    # different dates, similar to a real activity log.
    return pd.DataFrame({
        "user":   ["Harshit", "Priya", "Harshit", "Rahul", "Priya", "Harshit"],
        "date":   ["2026-01-01", "2026-01-05", "2026-02-10",
                   "2026-01-08", "2026-03-01", "2026-03-15"],
        "status": ["Active", "Active", "Active", "Active", "Active", "Active"],
    })


def count_duplicates(df: pd.DataFrame, subset: list = None) -> int:
    # I count how many duplicate rows exist, optionally
    # only checking specific columns.
    return df.duplicated(subset=subset).sum()


def show_duplicate_rows(df: pd.DataFrame, subset: list = None) -> pd.DataFrame:
    # I return only the rows that are marked as duplicates.
    return df[df.duplicated(subset=subset)]


def keep_first_occurrence(df: pd.DataFrame, subset: list = None) -> pd.DataFrame:
    # I drop duplicates, keeping the first time each value appeared.
    return df.drop_duplicates(subset=subset, keep="first")


def keep_latest_record(df: pd.DataFrame, group_column: str, date_column: str) -> pd.DataFrame:
    # I sort by date, then keep only the most recent row
    # for each unique value in the group column.
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column])
    sorted_df = df.sort_values(date_column)
    return sorted_df.drop_duplicates(subset=[group_column], keep="last")


# --- TESTING ---

data = build_dataset()
print(f"Original ({len(data)} rows):\n{data}")

dup_count = count_duplicates(data, subset=["user"])
print(f"\nDuplicate users (by name only): {dup_count}")

dup_rows = show_duplicate_rows(data, subset=["user"])
print(f"\nDuplicate rows:\n{dup_rows}")

first_only = keep_first_occurrence(data, subset=["user"])
print(f"\nKeeping first occurrence:\n{first_only}")

latest_only = keep_latest_record(data, "user", "date")
print(f"\nKeeping latest record per user:\n{latest_only}")

