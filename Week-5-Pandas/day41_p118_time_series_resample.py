# ============================================
# Day 41 - Program 118
# Topic: Datetime Index and resample()
# Concepts: setting datetime as index, resample
#           for different frequencies, comparing
#           daily vs weekly vs monthly views
# ============================================

import pandas as pd


def build_daily_sales() -> pd.DataFrame:
    # I build 30 days of daily sales data.
    dates = pd.date_range("2026-01-01", periods=30, freq="D")
    sales = [100, 120, 90, 150, 200, 180, 90, 110, 130, 170,
             140, 160, 95, 175, 210, 190, 85, 115, 125, 165,
             145, 155, 100, 180, 220, 200, 90, 120, 135, 175]
    return pd.DataFrame({"date": dates, "sales": sales})


def set_date_index(df: pd.DataFrame) -> pd.DataFrame:
    # I convert the date column into a real DatetimeIndex,
    # which every time-based operation depends on.
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    return df.set_index("date")


def weekly_total(df: pd.DataFrame) -> pd.Series:
    # I convert daily data into weekly totals.
    return df.resample("W")["sales"].sum()


def monthly_average(df: pd.DataFrame) -> pd.Series:
    # I convert daily data into a monthly average.
    return df.resample("M")["sales"].mean()


def best_week(df: pd.DataFrame) -> tuple:
    # I find which week had the highest total sales.
    weekly = weekly_total(df)
    best_date = weekly.idxmax()
    return best_date, weekly.max()


# --- TESTING ---

raw = build_daily_sales()
indexed = set_date_index(raw)

print(f"Index type: {type(indexed.index)}")

weekly = weekly_total(indexed)
print(f"\nWeekly totals:\n{weekly}")

monthly = monthly_average(indexed)
print(f"\nMonthly average:\n{monthly}")

best_date, best_value = best_week(indexed)
print(f"\nBest week: {best_date} with sales {best_value}")
