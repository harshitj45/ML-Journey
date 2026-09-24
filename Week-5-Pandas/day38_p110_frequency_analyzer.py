# ============================================
# Day 38 - Program 110
# Topic: value_counts and unique Analysis
# Concepts: value_counts, normalize=True,
#           unique vs nunique, class imbalance check
# ============================================

import pandas as pd


def build_dataset() -> pd.DataFrame:
    # I build a dataset with an imbalanced label column,
    # similar to a real fraud-detection style dataset.
    return pd.DataFrame({
        "transaction_id": range(1, 21),
        "label": ["Not Fraud"] * 18 + ["Fraud"] * 2,
        "city": ["Delhi", "Mumbai", "Delhi", "Chennai"] * 5,
    })


def get_frequency(df: pd.DataFrame, column: str) -> pd.Series:
    # I count how often each value appears.
    return df[column].value_counts()


def get_percentage(df: pd.DataFrame, column: str) -> pd.Series:
    # I get the same counts as percentages instead of raw numbers.
    return (df[column].value_counts(normalize=True) * 100).round(2)


def count_distinct_values(df: pd.DataFrame, column: str) -> int:
    # I count how many distinct values exist in a column.
    return df[column].nunique()


def list_distinct_values(df: pd.DataFrame, column: str):
    # I list the actual distinct values themselves.
    return df[column].unique()


def check_imbalance(df: pd.DataFrame, column: str, threshold: float = 90.0) -> bool:
    # I flag a column as imbalanced if any single class makes up
    # more than the given threshold percentage of the data.
    percentages = get_percentage(df, column)
    return percentages.max() > threshold


# --- TESTING ---

data = build_dataset()

print(f"City frequency:\n{get_frequency(data, 'city')}")
print(f"\nLabel frequency:\n{get_frequency(data, 'label')}")
print(f"\nLabel percentage:\n{get_percentage(data, 'label')}")

print(f"\nDistinct cities: {count_distinct_values(data, 'city')}")
print(f"City values: {list_distinct_values(data, 'city')}")

is_imbalanced = check_imbalance(data, "label")
print(f"\nIs 'label' imbalanced (>90%)? {is_imbalanced}")