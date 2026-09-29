# ============================================
# Day 41 - Program 119
# Topic: rolling() and shift()
# Concepts: moving average, min_periods, lag
#           features with shift, day-over-day change
# ============================================

import pandas as pd


def build_daily_sales() -> pd.DataFrame:
    # I build a small daily sales series to smooth and lag.
    dates = pd.date_range("2026-01-01", periods=10, freq="D")
    sales = [100, 120, 90, 150, 200, 180, 90, 110, 130, 170]
    df = pd.DataFrame({"date": dates, "sales": sales})
    return df.set_index("date")


def add_rolling_average(df: pd.DataFrame, window: int) -> pd.DataFrame:
    # I add a rolling average column to smooth out day-to-day noise.
    df = df.copy()
    df[f"rolling_{window}day"] = df["sales"].rolling(window).mean()
    return df


def add_rolling_with_min_periods(df: pd.DataFrame, window: int) -> pd.DataFrame:
    # I use min_periods so the first few rows still get a
    # partial average instead of NaN.
    df = df.copy()
    df[f"rolling_{window}day_filled"] = df["sales"].rolling(window, min_periods=1).mean()
    return df


def add_lag_feature(df: pd.DataFrame, periods: int = 1) -> pd.DataFrame:
    # I add the previous day's value as a new feature column,
    # a very common pattern for time series models.
    df = df.copy()
    df["prev_day_sales"] = df["sales"].shift(periods)
    return df


def add_day_over_day_change(df: pd.DataFrame) -> pd.DataFrame:
    # I calculate how much sales changed from the previous day.
    df = df.copy()
    df["change"] = df["sales"] - df["sales"].shift(1)
    return df


# --- TESTING ---

data = build_daily_sales()

with_rolling = add_rolling_average(data, 3)
print(f"With 3-day rolling average:\n{with_rolling}")

with_filled = add_rolling_with_min_periods(with_rolling, 3)
print(f"\nWith min_periods=1 (no leading NaN):\n{with_filled}")

with_lag = add_lag_feature(data)
print(f"\nWith lag feature:\n{with_lag}")

with_change = add_day_over_day_change(with_lag)
print(f"\nWith day-over-day change:\n{with_change}")
