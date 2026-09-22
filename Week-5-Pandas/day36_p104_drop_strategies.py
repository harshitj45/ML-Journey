# ============================================
# Day 36 - Program 104
# Topic: dropna() Strategies
# Concepts: dropna default, subset, how="all",
#           thresh, axis=1, comparing data loss
# ============================================

import pandas as pd
import numpy as np


def build_dataset() -> pd.DataFrame:
    # I build a dataset where different rows have
    # different amounts of missing data.
    return pd.DataFrame({
        "name":   ["Harshit", "Priya", None, "Neha", None],
        "age":    [21, np.nan, 22, 20, np.nan],
        "marks":  [85, 92, np.nan, 78, np.nan],
        "city":   ["Delhi", "Mumbai", None, "Chennai", None],
    })


def drop_any_missing(df: pd.DataFrame) -> pd.DataFrame:
    # I drop any row that has even one missing value.
    # This is the most aggressive option and usually
    # loses too much data.
    return df.dropna()


def drop_by_subset(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    # I only drop rows where the columns I actually care
    # about are missing. This is the option I use most often.
    return df.dropna(subset=columns)


def drop_fully_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    # I drop only rows where every single value is missing.
    return df.dropna(how="all")


def drop_by_threshold(df: pd.DataFrame, min_valid: int) -> pd.DataFrame:
    # I keep only rows that have at least min_valid
    # non-missing values.
    return df.dropna(thresh=min_valid)


def drop_missing_columns(df: pd.DataFrame) -> pd.DataFrame:
    # I drop entire columns that contain any missing values.
    return df.dropna(axis=1)


def compare_all_strategies(df: pd.DataFrame) -> pd.DataFrame:
    # I compare how many rows survive each strategy, so I can
    # see the data-loss tradeoff before choosing one.
    return pd.DataFrame({
        "strategy": [
            "original",
            "dropna() - any missing",
            "dropna(subset=['marks'])",
            "dropna(how='all')",
            "dropna(thresh=3)",
        ],
        "rows_remaining": [
            len(df),
            len(drop_any_missing(df)),
            len(drop_by_subset(df, ["marks"])),
            len(drop_fully_empty_rows(df)),
            len(drop_by_threshold(df, 3)),
        ],
    })


# --- TESTING ---

data = build_dataset()
print(f"Original ({len(data)} rows):\n{data}")

print(f"\nAfter dropna():\n{drop_any_missing(data)}")
print(f"\nAfter dropna(subset=['marks']):\n{drop_by_subset(data, ['marks'])}")
print(f"\nAfter dropna(thresh=3):\n{drop_by_threshold(data, 3)}")
print(f"\nAfter dropna(axis=1):\n{drop_missing_columns(data)}")

comparison = compare_all_strategies(data)
print(f"\nStrategy comparison:\n{comparison}")