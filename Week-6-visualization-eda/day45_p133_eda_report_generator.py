# ============================================
# Day 45 - Program 133
# Topic: EDA Framework Steps 7-8 + Full Report
# Concepts: feature hypothesis, written conclusions,
#           a reusable function that runs all 8 steps
#           and prints a structured summary
# ============================================

import pandas as pd
import numpy as np
from day45_p131_eda_overview_univariate import build_cafe_dataset


def step7_feature_hypothesis(df: pd.DataFrame) -> list:
    # STEP 7: Before any model, I write down which features
    # I *expect* to matter, based on what I've seen so far.
    hypotheses = []
    if df.groupby("customer_type")["rating"].mean().diff().abs().iloc[-1] > 0.3:
        hypotheses.append("customer_type seems related to rating")
    if df.groupby("item")["price"].std().mean() > 5:
        hypotheses.append("item type strongly affects price")
    return hypotheses


def step8_written_conclusions(df: pd.DataFrame, outlier_count: int) -> list:
    # STEP 8: I turn every finding into a plain-English
    # conclusion — this is the step recruiters actually read.
    conclusions = []
    mean_p, median_p = df["price"].mean(), df["price"].median()
    skew_note = "right-skewed" if mean_p > median_p else "left-skewed"
    conclusions.append(
        f"Price is {skew_note} (mean={mean_p:.1f} vs median={median_p:.1f}), "
        f"likely due to {outlier_count} high-value outlier order(s)."
    )
    missing_pct = df["rating"].isna().mean() * 100
    conclusions.append(
        f"{missing_pct:.0f}% of ratings are missing — worth investigating "
        f"whether this correlates with order type before filling it."
    )
    return conclusions


def run_full_eda_report(df: pd.DataFrame) -> dict:
    # I combine every step into one function that returns a
    # complete, structured EDA summary — reusable for any dataset.
    q1, q3 = df["price"].quantile(0.25), df["price"].quantile(0.75)
    iqr = q3 - q1
    outliers = df[(df["price"] < q1 - 1.5*iqr) | (df["price"] > q3 + 1.5*iqr)]

    return {
        "shape": df.shape,
        "missing_total": int(df.isna().sum().sum()),
        "duplicate_count": int(df.duplicated().sum()),
        "outlier_count": len(outliers),
        "hypotheses": step7_feature_hypothesis(df),
        "conclusions": step8_written_conclusions(df, len(outliers)),
    }


# --- RUN ---

data = build_cafe_dataset()
report = run_full_eda_report(data)

print("=== FULL EDA REPORT ===")
for key, value in report.items():
    print(f"\n{key.upper()}:")
    print(value)
    