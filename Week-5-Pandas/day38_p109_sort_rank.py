# ============================================
# Day 38 - Program 109
# Topic: Sorting and Ranking
# Concepts: sort_values, multi-column sort,
#           rank(), nlargest/nsmallest
# ============================================

import pandas as pd


def build_dataset() -> pd.DataFrame:
    # I build a small student dataset to sort and rank.
    return pd.DataFrame({
        "name":  ["Harshit", "Priya", "Rahul", "Neha", "Arjun", "Sneha"],
        "marks": [85, 92, 78, 92, 60, 88],
        "city":  ["Delhi", "Mumbai", "Delhi", "Delhi", "Chennai", "Mumbai"],
    })


def sort_by_marks(df: pd.DataFrame, descending: bool = True) -> pd.DataFrame:
    # I sort the whole dataset by one column.
    return df.sort_values("marks", ascending=not descending)


def sort_by_city_then_marks(df: pd.DataFrame) -> pd.DataFrame:
    # I sort by city first, then by marks within each city.
    return df.sort_values(["city", "marks"], ascending=[True, False])


def add_rank_column(df: pd.DataFrame) -> pd.DataFrame:
    # I add a rank column, highest marks getting rank 1.
    df = df.copy()
    df["rank"] = df["marks"].rank(ascending=False, method="min")
    return df


def get_top_n(df: pd.DataFrame, n: int) -> pd.DataFrame:
    # I get the top N rows without sorting the whole DataFrame first.
    return df.nlargest(n, "marks")


# --- TESTING ---

data = build_dataset()
print(f"Sorted by marks:\n{sort_by_marks(data)}")
print(f"\nSorted by city then marks:\n{sort_by_city_then_marks(data)}")
print(f"\nWith rank:\n{add_rank_column(data)}")
print(f"\nTop 3:\n{get_top_n(data, 3)}")