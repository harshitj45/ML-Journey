# ============================================
# Day 36 - Program 105
# Topic: fillna() Strategies and Sentinel Values
# Concepts: fill with constant/mean/median/mode,
#           ffill/bfill, dict-based filling,
#           converting sentinel values to NaN
# ============================================

import pandas as pd
import numpy as np


def build_dataset() -> pd.DataFrame:
    # I build a dataset with missing values in both
    # numeric and text columns.
    return pd.DataFrame({
        "age":    [21, np.nan, 22, np.nan, 25, 23],
        "marks":  [85, 92, np.nan, 78, np.nan, 88],
        "city":   ["Delhi", None, "Mumbai", None, "Delhi", "Delhi"],
    })


def build_sentinel_dataset() -> pd.DataFrame:
    # I build a dataset where missing values are hidden
    # behind fake placeholder values instead of real NaN.
    return pd.DataFrame({
        "age":   [21, -1, 22, 999, 25],
        "city":  ["Delhi", "", "Mumbai", "N/A", "Delhi"],
    })


def fill_with_constant(df: pd.DataFrame, column: str, value) -> pd.DataFrame:
    # I fill missing values in one column with a fixed value.
    df = df.copy()
    df[column] = df[column].fillna(value)
    return df


def fill_with_mean(df: pd.DataFrame, column: str) -> pd.DataFrame:
    # I fill missing values with the column's mean.
    # I avoid this when the column has strong outliers.
    df = df.copy()
    df[column] = df[column].fillna(df[column].mean())
    return df


def fill_with_median(df: pd.DataFrame, column: str) -> pd.DataFrame:
    # I fill missing values with the median, which is
    # more robust to outliers than the mean.
    df = df.copy()
    df[column] = df[column].fillna(df[column].median())
    return df


def fill_with_mode(df: pd.DataFrame, column: str) -> pd.DataFrame:
    # I fill missing text values with the most frequent value.
    df = df.copy()
    df[column] = df[column].fillna(df[column].mode()[0])
    return df


def fill_multiple_columns(df: pd.DataFrame, fill_map: dict) -> pd.DataFrame:
    # I fill several columns at once, each with its own value.
    return df.fillna(fill_map)


def forward_then_backward_fill(series: pd.Series) -> pd.Series:
    # I carry the previous value forward, then chain a backward
    # fill so any leading missing values also get filled.
    return series.ffill().bfill()


def convert_sentinels_to_nan(df: pd.DataFrame) -> pd.DataFrame:
    # I convert fake placeholder values into real NaN, so
    # isna() can actually detect them.
    df = df.copy()
    df["age"] = df["age"].replace([-1, 999], np.nan)
    df["city"] = df["city"].replace(["", "N/A"], np.nan)
    return df


# --- TESTING ---

data = build_dataset()
print(f"Original:\n{data}")

print(f"\nMean-filled age:\n{fill_with_mean(data, 'age')}")
print(f"\nMedian-filled marks:\n{fill_with_median(data, 'marks')}")
print(f"\nMode-filled city:\n{fill_with_mode(data, 'city')}")

multi_filled = fill_multiple_columns(data, {"age": 0, "marks": 0, "city": "Unknown"})
print(f"\nMultiple columns filled:\n{multi_filled}")

series = pd.Series([np.nan, 1, np.nan, np.nan, 4])
print(f"\nOriginal series: {list(series)}")
print(f"ffill then bfill: {list(forward_then_backward_fill(series))}")

# I show how sentinel values hide missing data.
sentinel_data = build_sentinel_dataset()
print(f"\nSentinel dataset:\n{sentinel_data}")
print(f"isna() sees: {sentinel_data.isna().sum().sum()} missing values")

cleaned = convert_sentinels_to_nan(sentinel_data)
print(f"\nAfter converting sentinels:\n{cleaned}")
print(f"isna() now sees: {cleaned.isna().sum().sum()} missing values")