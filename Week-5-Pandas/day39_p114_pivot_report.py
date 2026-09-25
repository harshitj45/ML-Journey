# ============================================
# Day 39 - Program 114
# Topic: pivot_table and GroupBy vs Pivot Comparison
# Concepts: pivot_table with index/columns/values/aggfunc,
#           fill_value, comparing groupby output shape
#           vs pivot_table output shape
# ============================================

import pandas as pd


def build_dataset() -> pd.DataFrame:
    # I build a dataset with two categorical dimensions,
    # which is exactly when pivot_table becomes useful.
    return pd.DataFrame({
        "city":  ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Mumbai"],
        "dept":  ["CSE", "ECE", "CSE", "ECE", "CSE", "CSE"],
        "marks": [85, 78, 92, 88, 90, 65],
    })


def groupby_summary(df: pd.DataFrame) -> pd.Series:
    # I get a 1-dimensional summary: average marks per city only.
    return df.groupby("city")["marks"].mean()


def pivot_summary(df: pd.DataFrame) -> pd.DataFrame:
    # I get a 2-dimensional grid: city vs dept, both at once.
    return pd.pivot_table(
        df, values="marks", index="city",
        columns="dept", aggfunc="mean", fill_value=0
    )


def pivot_with_counts(df: pd.DataFrame) -> pd.DataFrame:
    # I build a pivot table showing how many students fall
    # into each city-dept combination, not just their average.
    return pd.pivot_table(
        df, values="marks", index="city",
        columns="dept", aggfunc="count", fill_value=0
    )


# --- TESTING ---

data = build_dataset()

groupby_result = groupby_summary(data)
print(f"GroupBy (1D summary):\n{groupby_result}")
print(f"Shape: {groupby_result.shape}")

pivot_result = pivot_summary(data)
print(f"\npivot_table (2D grid):\n{pivot_result}")
print(f"Shape: {pivot_result.shape}")

counts = pivot_with_counts(data)
print(f"\nStudent counts per city-dept:\n{counts}")

