# ============================================
# Day 42 - Program 122 (Module)
# Topic: Cleaning Customers and Orders
# Concepts: str cleaning, drop_duplicates,
#           to_numeric/to_datetime with errors="coerce",
#           IQR outlier capping, dropna for unusable rows
# ============================================

import pandas as pd


def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    # I clean names and emails, then remove duplicate customers.
    df = df.copy()
    df["name"] = df["name"].str.strip().str.title()
    df["email"] = df["email"].str.lower()
    df = df.drop_duplicates(subset=["customer_id"], keep="first")
    return df


def fix_order_types(df: pd.DataFrame) -> pd.DataFrame:
    # I convert amount and date to real numeric/datetime types.
    # Invalid values become NaN/NaT instead of crashing.
    df = df.copy()
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    return df


def handle_missing_orders(df: pd.DataFrame) -> pd.DataFrame:
    # I fill a missing amount with the median (robust to outliers),
    # and drop rows with a missing date since I can't meaningfully
    # guess a date for time series analysis.
    df = df.copy()
    df["amount"] = df["amount"].fillna(df["amount"].median())
    df = df.dropna(subset=["order_date"])
    return df


def cap_outlier_amounts(df: pd.DataFrame) -> pd.DataFrame:
    # I cap extreme order amounts using the IQR method,
    # instead of deleting the row entirely.
    df = df.copy()
    q1 = df["amount"].quantile(0.25)
    q3 = df["amount"].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    df["amount"] = df["amount"].clip(lower=lower, upper=upper)
    return df


def full_clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    # I run every order-cleaning step in the correct sequence.
    df = fix_order_types(df)
    df = handle_missing_orders(df)
    df = cap_outlier_amounts(df)
    return df

