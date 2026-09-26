# ============================================
# Day 40 - Program 117
# Topic: concat() Vertical and Horizontal
# Concepts: axis=0, axis=1, ignore_index,
#           combining multiple monthly files
# ============================================

import pandas as pd


def build_monthly_sales() -> list:
    # I build three months of sales data with the same structure,
    # like separate files that need to be combined.
    jan = pd.DataFrame({"product": ["A", "B"], "sales": [100, 200]})
    feb = pd.DataFrame({"product": ["A", "B"], "sales": [150, 180]})
    mar = pd.DataFrame({"product": ["A", "B"], "sales": [120, 210]})
    return [jan, feb, mar]


def combine_vertically(dataframes: list) -> pd.DataFrame:
    # I stack multiple same-structure DataFrames on top of
    # each other, with a clean new index.
    return pd.concat(dataframes, axis=0, ignore_index=True)


def add_month_labels(dataframes: list, labels: list) -> pd.DataFrame:
    # I add a month label to each DataFrame before combining,
    # so I can tell which row came from which month.
    labeled = []
    for df, label in zip(dataframes, labels):
        df = df.copy()
        df["month"] = label
        labeled.append(df)
    return pd.concat(labeled, axis=0, ignore_index=True)


def combine_horizontally(names: pd.DataFrame, marks: pd.DataFrame) -> pd.DataFrame:
    # I combine two DataFrames side by side, matching by row position.
    return pd.concat([names, marks], axis=1)


# --- TESTING ---

monthly = build_monthly_sales()

stacked = combine_vertically(monthly)
print(f"Stacked (no labels):\n{stacked}")

labeled = add_month_labels(monthly, ["Jan", "Feb", "Mar"])
print(f"\nStacked with month labels:\n{labeled}")

names = pd.DataFrame({"name": ["Harshit", "Priya"]})
marks = pd.DataFrame({"marks": [85, 92]})
side_by_side = combine_horizontally(names, marks)
print(f"\nSide by side (axis=1):\n{side_by_side}")

# I total sales per product across all months using groupby,
# tying today's concat work back to Day 39's groupby.
total_by_product = labeled.groupby("product")["sales"].sum()
print(f"\nTotal sales per product across months:\n{total_by_product}")
