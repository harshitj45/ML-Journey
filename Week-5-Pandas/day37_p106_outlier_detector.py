# ============================================
# Day 37 - Program 106
# Topic: IQR-Based Outlier Detection and Capping
# Concepts: quantile, IQR calculation, bounds,
#           boolean filtering, clip() for capping
# ============================================

import pandas as pd


def build_dataset() -> pd.DataFrame:
    # I build a dataset with a few obvious outliers planted in it.
    return pd.DataFrame({
        "name":  ["Harshit", "Priya", "Rahul", "Neha", "Arjun", "Sneha", "Karan"],
        "marks": [85, 88, 90, 82, 250, 86, -5],
    })


def get_outlier_bounds(series: pd.Series) -> tuple:
    # I calculate the lower and upper bounds using the
    # standard IQR method (1.5 times the interquartile range).
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return lower, upper


def find_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    # I return only the rows that fall outside the IQR bounds.
    lower, upper = get_outlier_bounds(df[column])
    return df[(df[column] < lower) | (df[column] > upper)]


def remove_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    # I remove rows outside the bounds entirely.
    lower, upper = get_outlier_bounds(df[column])
    return df[(df[column] >= lower) & (df[column] <= upper)]


def cap_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    # I keep every row, but limit extreme values to the
    # nearest bound instead of deleting them.
    df = df.copy()
    lower, upper = get_outlier_bounds(df[column])
    df[column] = df[column].clip(lower=lower, upper=upper)
    return df


# --- TESTING ---

data = build_dataset()
print(f"Original:\n{data}")

lower, upper = get_outlier_bounds(data["marks"])
print(f"\nNormal range: {lower:.1f} to {upper:.1f}")

outliers = find_outliers(data, "marks")
print(f"\nOutliers found:\n{outliers}")

removed = remove_outliers(data, "marks")
print(f"\nAfter removing ({len(removed)} rows):\n{removed}")

capped = cap_outliers(data, "marks")
print(f"\nAfter capping (still {len(capped)} rows):\n{capped}")

