# ============================================
# Day 37 - Program 108
# Topic: Fixing Data Types in Messy Data
# Concepts: astype, string cleaning, to_numeric
#           with errors="coerce", to_datetime with
#           errors="coerce", extracting date parts
# ============================================

import pandas as pd


def build_messy_dataset() -> pd.DataFrame:
    # I build a dataset with realistic messy formatting:
    # numbers stored as text, commas in numbers, and one
    # genuinely invalid value in each column.
    return pd.DataFrame({
        "marks":  ["85", "92", "78", "invalid"],
        "salary": ["25,000", "30,000", "abc", "40,000"],
        "date":   ["2026-01-15", "2026-02-20", "2026-03-10", "not a date"],
    })


def clean_numeric_column(series: pd.Series) -> pd.Series:
    # I remove commas from numbers stored as text, then
    # convert to a real numeric type. Invalid values become
    # NaN instead of crashing the whole conversion.
    cleaned = series.str.replace(",", "", regex=False)
    return pd.to_numeric(cleaned, errors="coerce")


def clean_date_column(series: pd.Series) -> pd.Series:
    # I convert a text column into real datetime values,
    # turning anything invalid into NaT instead of crashing.
    return pd.to_datetime(series, errors="coerce")


def safe_convert_marks(series: pd.Series) -> pd.Series:
    # I convert a numeric-looking text column, letting
    # invalid entries become NaN rather than raising an error.
    return pd.to_numeric(series, errors="coerce")


def extract_date_parts(df: pd.DataFrame, date_column: str) -> pd.DataFrame:
    # I pull the year and month out of a cleaned datetime column.
    df = df.copy()
    df["year"] = df[date_column].dt.year
    df["month"] = df[date_column].dt.month
    return df


# --- TESTING ---

data = build_messy_dataset()
print(f"Original dtypes:\n{data.dtypes}")
print(f"\nOriginal data:\n{data}")

data["marks_clean"] = safe_convert_marks(data["marks"])
data["salary_clean"] = clean_numeric_column(data["salary"])
data["date_clean"] = clean_date_column(data["date"])

print(f"\nCleaned data:\n{data}")
print(f"\nNew dtypes:\n{data[['marks_clean', 'salary_clean', 'date_clean']].dtypes}")

with_parts = extract_date_parts(data, "date_clean")
print(f"\nWith year/month extracted:\n{with_parts[['date_clean', 'year', 'month']]}")

# I confirm how many values became missing due to bad data.
print(f"\nInvalid entries converted to missing: "
      f"marks={data['marks_clean'].isna().sum()}, "
      f"salary={data['salary_clean'].isna().sum()}, "
      f"date={data['date_clean'].isna().sum()}")

