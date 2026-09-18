# ============================================
# Day 33 - Program 95
# Topic: Creating DataFrames Three Ways
# Concepts: dict-of-lists, list-of-lists,
#           NumPy array to DataFrame
# ============================================

import pandas as pd
import numpy as np


def create_from_dict(names: list, marks: list, cities: list) -> pd.DataFrame:
    # I create a DataFrame from a dictionary of lists,
    # the most common and readable way to build one.
    return pd.DataFrame({
        "name": names,
        "marks": marks,
        "city": cities,
    })


def create_from_list_of_lists(rows: list, column_names: list) -> pd.DataFrame:
    # I create a DataFrame from raw rows, supplying the
    # column names separately.
    return pd.DataFrame(rows, columns=column_names)


def create_from_numpy(array: np.ndarray, column_names: list) -> pd.DataFrame:
    # I create a DataFrame directly from a NumPy array,
    # reusing the array skills from Days 30-31.
    return pd.DataFrame(array, columns=column_names)


def get_column_as_series(df: pd.DataFrame, column: str) -> pd.Series:
    # I confirm that a single column pulled from a
    # DataFrame is a Series.
    return df[column]


# --- TESTING ---

df1 = create_from_dict(
    ["Harshit", "Priya", "Rahul"],
    [85, 92, 78],
    ["Delhi", "Mumbai", "Chennai"]
)
print(df1)

df2 = create_from_list_of_lists(
    [["Harshit", 85], ["Priya", 92], ["Rahul", 78]],
    ["name", "marks"]
)
print(df2)

scores_array = np.array([[85, 90], [92, 88], [78, 82]])
df3 = create_from_numpy(scores_array, ["test1", "test2"])
print(df3)

name_column = get_column_as_series(df1, "name")
print(type(name_column))
print(name_column)
