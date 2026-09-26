# ============================================
# Day 40 - Program 116
# Topic: Merging with Different Column Names
# Concepts: left_on/right_on, indicator=True,
#           finding unmatched rows on either side
# ============================================

import pandas as pd


def build_users() -> pd.DataFrame:
    # I build a users table with its own id column name.
    return pd.DataFrame({
        "uid": [1, 2, 3],
        "name": ["Harshit", "Priya", "Rahul"],
    })


def build_scores() -> pd.DataFrame:
    # I build a scores table with a DIFFERENTLY named id column,
    # and one score for a user that doesn't exist above.
    return pd.DataFrame({
        "user_id": [1, 2, 5],
        "marks": [85, 92, 70],
    })


def merge_different_key_names(users: pd.DataFrame, scores: pd.DataFrame) -> pd.DataFrame:
    # I merge two tables where the key column has a different
    # name in each one.
    return pd.merge(users, scores, left_on="uid", right_on="user_id", how="outer")


def find_unmatched_rows(users: pd.DataFrame, scores: pd.DataFrame) -> pd.DataFrame:
    # I use the indicator column to find rows that only
    # exist on one side of the merge.
    merged = pd.merge(
        users, scores, left_on="uid", right_on="user_id",
        how="outer", indicator=True
    )
    return merged[merged["_merge"] != "both"]


# --- TESTING ---

users = build_users()
scores = build_scores()

merged = merge_different_key_names(users, scores)
print(f"Merged on different key names:\n{merged}")

unmatched = find_unmatched_rows(users, scores)
print(f"\nUnmatched rows (only on one side):\n{unmatched}")

