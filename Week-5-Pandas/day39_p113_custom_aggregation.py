# ============================================
# Day 39 - Program 113
# Topic: Custom Aggregation Functions and reset_index()
# Concepts: passing a custom function to agg(),
#           reset_index() to flatten grouped results,
#           chaining groupby with further filtering
# ============================================

import pandas as pd


def build_dataset() -> pd.DataFrame:
    # I build a dataset to test a custom aggregation on.
    return pd.DataFrame({
        "dept":  ["CSE", "CSE", "ECE", "ECE", "ME", "ME"],
        "marks": [85, 60, 92, 90, 70, 40],
    })


def score_range(marks: pd.Series) -> float:
    # I define a custom aggregation: the spread between the
    # highest and lowest score in each group.
    return marks.max() - marks.min()


def get_score_range_per_dept(df: pd.DataFrame) -> pd.Series:
    # I apply my custom function through agg().
    return df.groupby("dept")["marks"].agg(score_range)


def get_grouped_as_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    # I convert a grouped Series back into a normal DataFrame
    # using reset_index(), so I can filter or merge it later.
    grouped = df.groupby("dept")["marks"].mean()
    return grouped.reset_index()


def departments_above_average(df: pd.DataFrame) -> pd.DataFrame:
    # I combine groupby, reset_index, and filtering together —
    # this only works smoothly once the group column is
    # a normal column again, not an index.
    grouped_df = get_grouped_as_dataframe(df)
    overall_avg = df["marks"].mean()
    return grouped_df[grouped_df["marks"] > overall_avg]


# --- TESTING ---

data = build_dataset()

ranges = get_score_range_per_dept(data)
print(f"Score range per dept:\n{ranges}")

grouped_df = get_grouped_as_dataframe(data)
print(f"\nGrouped as DataFrame:\n{grouped_df}")
print(f"Columns: {list(grouped_df.columns)}")

above_avg_depts = departments_above_average(data)
print(f"\nDepartments above overall average:\n{above_avg_depts}")

