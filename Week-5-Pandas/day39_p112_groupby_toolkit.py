# ============================================
# Day 39 - Program 112
# Topic: GroupBy Basics and Multiple Aggregations
# Concepts: groupby single/multi column, .agg()
#           with list, .agg() with dict per column
# ============================================

import pandas as pd


def build_dataset() -> pd.DataFrame:
    # I build a sales-style dataset with a category and region.
    return pd.DataFrame({
        "region":   ["North", "South", "North", "South", "North", "West"],
        "category": ["Electronics", "Clothing", "Clothing", "Electronics", "Electronics", "Clothing"],
        "revenue":  [5000, 3000, 2500, 4500, 6000, 2000],
        "units":    [10, 15, 8, 12, 14, 6],
    })


def average_revenue_by_region(df: pd.DataFrame) -> pd.Series:
    # I calculate the average revenue for each region.
    return df.groupby("region")["revenue"].mean()


def multiple_stats_by_region(df: pd.DataFrame) -> pd.DataFrame:
    # I calculate several statistics for revenue in one call.
    return df.groupby("region")["revenue"].agg(["mean", "sum", "max", "count"])


def different_agg_per_column(df: pd.DataFrame) -> pd.DataFrame:
    # I apply a different aggregation to each column.
    return df.groupby("region").agg({
        "revenue": "sum",
        "units": "mean",
    })


def group_by_two_columns(df: pd.DataFrame) -> pd.Series:
    # I group by two columns together for a more detailed breakdown.
    return df.groupby(["region", "category"])["revenue"].sum()


# --- TESTING ---

data = build_dataset()

print(f"Average revenue by region:\n{average_revenue_by_region(data)}")
print(f"\nMultiple stats by region:\n{multiple_stats_by_region(data)}")
print(f"\nDifferent agg per column:\n{different_agg_per_column(data)}")
print(f"\nRegion + Category breakdown:\n{group_by_two_columns(data)}")

