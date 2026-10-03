# ============================================
# Day 45 - Program 132
# Topic: EDA Framework Steps 4-6
# Concepts: multivariate correlation, IQR outlier
#           confirmation, missing value pattern check
# ============================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from day45_p131_eda_overview_univariate import build_cafe_dataset


def step4_multivariate(df: pd.DataFrame, filename: str) -> pd.DataFrame:
    # STEP 4: I look at relationships across all numeric
    # features at once using a correlation heatmap.
    print("--- STEP 4: Multivariate Analysis ---")
    numeric_df = df.select_dtypes(include=[np.number])
    corr = numeric_df.corr()
    print(f"Correlation matrix:\n{corr}")

    plt.figure()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Feature Correlation")
    plt.savefig(filename)
    plt.close()
    return corr


def step5_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    # STEP 5: I confirm outliers using the IQR method,
    # following up on what the boxplot in Step 2 hinted at.
    print(f"\n--- STEP 5: Outlier Analysis ({column}) ---")
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    outliers = df[(df[column] < lower) | (df[column] > upper)]
    print(f"Outliers found: {len(outliers)}")
    print(outliers)
    return outliers


def step6_missing_patterns(df: pd.DataFrame) -> None:
    # STEP 6: I check WHY values might be missing, not just
    # how many — missingness itself can be a signal.
    print("\n--- STEP 6: Missing Value Patterns ---")
    audit = pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_pct": (df.isna().mean() * 100).round(1),
    })
    print(audit)

    # I check if missing ratings correlate with a different price.
    has_rating = df["rating"].notna()
    avg_price_by_rating_presence = df.groupby(has_rating)["price"].mean()
    print(f"\nAvg price by whether rating exists:\n{avg_price_by_rating_presence}")


# --- RUN ---

data = build_cafe_dataset()
step4_multivariate(data, "day45_correlation.png")
step5_outliers(data, "price")
step6_missing_patterns(data)
