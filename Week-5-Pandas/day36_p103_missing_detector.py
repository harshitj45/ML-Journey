# ============================================
# Day 36 - Program 103
# Topic: Detecting Missing Values
# Concepts: isna/notna, counting and percentage
#           of missing values, row-wise detection,
#           building a missing-value audit report
# ============================================

import pandas as pd
import numpy as np


def build_messy_dataset() -> pd.DataFrame:
    # I build a dataset with missing values scattered
    # across different columns, like real raw data.
    return pd.DataFrame({
        "name":   ["Harshit", "Priya", None, "Neha", "Arjun", None],
        "age":    [21, np.nan, 22, 20, np.nan, 23],
        "marks":  [85, 92, np.nan, np.nan, 78, np.nan],
        "city":   ["Delhi", "Mumbai", "Delhi", None, "Chennai", "Delhi"],
    })


def count_missing_per_column(df: pd.DataFrame) -> pd.Series:
    # I count how many values are missing in each column.
    return df.isna().sum()


def percent_missing_per_column(df: pd.DataFrame) -> pd.Series:
    # I calculate what percentage of each column is missing,
    # which is what I actually use to decide drop vs fill.
    return (df.isna().mean() * 100).round(2)


def build_audit_report(df: pd.DataFrame) -> pd.DataFrame:
    # I combine count and percentage into one audit table.
    # This is always my first step before cleaning anything.
    return pd.DataFrame({
        "missing_count": count_missing_per_column(df),
        "missing_pct": percent_missing_per_column(df),
    })


def rows_with_any_missing(df: pd.DataFrame) -> pd.DataFrame:
    # I find every row that has at least one missing value.
    return df[df.isna().any(axis=1)]


def rows_fully_complete(df: pd.DataFrame) -> pd.DataFrame:
    # I find rows where nothing is missing at all.
    return df[df.notna().all(axis=1)]


def demonstrate_nan_comparison(df: pd.DataFrame) -> dict:
    # I show why == np.nan never works, and why isna()
    # is the only reliable way to detect missing values.
    wrong_way = len(df[df["age"] == np.nan])
    right_way = len(df[df["age"].isna()])
    return {"using_equals": wrong_way, "using_isna": right_way}


# --- TESTING ---

data = build_messy_dataset()
print(f"Raw dataset:\n{data}")

print(f"\nMissing per column:\n{count_missing_per_column(data)}")
print(f"\nTotal missing values: {data.isna().sum().sum()}")

audit = build_audit_report(data)
print(f"\nAudit report:\n{audit}")

incomplete = rows_with_any_missing(data)
print(f"\nRows with missing data:\n{incomplete}")

complete = rows_fully_complete(data)
print(f"\nFully complete rows:\n{complete}")

comparison = demonstrate_nan_comparison(data)
print(f"\nNaN comparison test: {comparison}")

