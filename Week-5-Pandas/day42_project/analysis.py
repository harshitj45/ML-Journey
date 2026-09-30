# ============================================
# Day 42 - Program 123 (Module)
# Topic: Merge, GroupBy, and Time Series Analysis
# Concepts: merge with indicator, groupby aggregation,
#           resample, rolling, rank-based top customers
# ============================================

import pandas as pd


def merge_customers_orders(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # I merge with an outer join and an indicator, so I can
    # see customers with no orders AND orders with no customer.
    return pd.merge(
        customers, orders, on="customer_id",
        how="outer", indicator=True
    )


def find_unmatched(merged: pd.DataFrame) -> pd.DataFrame:
    # I use the indicator column to isolate rows that didn't
    # match on both sides of the merge.
    return merged[merged["_merge"] != "both"]


def revenue_by_city(merged: pd.DataFrame) -> pd.Series:
    # I total up revenue for each city using groupby.
    valid = merged[merged["_merge"] == "both"]
    return valid.groupby("city")["amount"].sum().sort_values(ascending=False)


def top_customers(merged: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    # I find the top N customers by total spending.
    valid = merged[merged["_merge"] == "both"]
    totals = valid.groupby("name")["amount"].sum().reset_index()
    totals["rank"] = totals["amount"].rank(ascending=False, method="min")
    return totals.sort_values("amount", ascending=False).head(n)


def weekly_revenue_trend(merged: pd.DataFrame) -> pd.Series:
    # I build a weekly revenue trend using resample, which
    # requires a datetime index first.
    valid = merged[merged["_merge"] == "both"].copy()
    valid = valid.set_index("order_date")
    return valid.resample("W")["amount"].sum()


def rolling_revenue(weekly: pd.Series, window: int = 2) -> pd.Series:
    # I smooth the weekly trend with a rolling average.
    return weekly.rolling(window, min_periods=1).mean()


def week_over_week_change(weekly: pd.Series) -> pd.Series:
    # I calculate how revenue changed from the previous week.
    return weekly - weekly.shift(1)

