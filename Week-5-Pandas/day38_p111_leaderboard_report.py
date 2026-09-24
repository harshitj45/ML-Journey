# ============================================
# Day 38 - Program 111
# Topic: Combining Sorting, Ranking, and Frequency
# Concepts: full workflow — rank, sort, value_counts
#           together in one report
# ============================================

import pandas as pd


def build_dataset() -> pd.DataFrame:
    # I build a dataset of quiz scores across departments.
    return pd.DataFrame({
        "name":  ["Harshit", "Priya", "Rahul", "Neha", "Arjun", "Sneha", "Karan"],
        "score": [85, 92, 78, 92, 60, 88, 78],
        "dept":  ["CSE", "ECE", "CSE", "CSE", "ME", "ECE", "CSE"],
    })


def build_leaderboard(df: pd.DataFrame) -> pd.DataFrame:
    # I build a full leaderboard: ranked, sorted, with a
    # department frequency summary alongside it.
    df = df.copy()
    df["rank"] = df["score"].rank(ascending=False, method="min")
    return df.sort_values("rank")


def department_summary(df: pd.DataFrame) -> pd.DataFrame:
    # I summarize how many students come from each department.
    counts = df["dept"].value_counts()
    percentages = df["dept"].value_counts(normalize=True) * 100
    return pd.DataFrame({"count": counts, "percent": percentages.round(1)})


def top_scorer_per_dept(df: pd.DataFrame) -> pd.DataFrame:
    # I find the top scorer within each department using
    # sort_values plus drop_duplicates together.
    return df.sort_values("score", ascending=False).drop_duplicates(subset=["dept"], keep="first")


# --- TESTING ---

data = build_dataset()

leaderboard = build_leaderboard(data)
print(f"Leaderboard:\n{leaderboard}")

dept_stats = department_summary(data)
print(f"\nDepartment summary:\n{dept_stats}")

top_per_dept = top_scorer_per_dept(data)
print(f"\nTop scorer per department:\n{top_per_dept}")

