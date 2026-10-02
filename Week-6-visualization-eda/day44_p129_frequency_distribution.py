# ============================================
# Day 44 - Program 129
# Topic: countplot and histplot with KDE
# Concepts: sns.countplot vs value_counts,
#           sns.histplot with kde=True, comparing
#           a normal vs skewed distribution
# ============================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def build_city_dataset() -> pd.DataFrame:
    # I build a dataset with an uneven distribution of cities.
    return pd.DataFrame({
        "city": ["Delhi"] * 6 + ["Mumbai"] * 4 + ["Chennai"] * 2,
    })


def plot_countplot(df: pd.DataFrame, column: str, filename: str) -> pd.Series:
    # I visualize category frequency, and return the same
    # numbers from value_counts() to confirm they match.
    plt.figure()
    sns.countplot(data=df, x=column)
    plt.title(f"{column} Frequency")
    plt.savefig(filename)
    plt.close()
    return df[column].value_counts()


def plot_distribution_with_kde(data: np.ndarray, title: str, filename: str) -> None:
    # I plot a histogram with a smooth density curve overlaid.
    df = pd.DataFrame({"value": data})
    plt.figure()
    sns.histplot(data=df, x="value", kde=True)
    plt.title(title)
    plt.savefig(filename)
    plt.close()


# --- TESTING ---

city_data = build_city_dataset()
counts = plot_countplot(city_data, "city", "day44_countplot.png")
print(f"value_counts() result:\n{counts}")

np.random.seed(1)
normal_data = np.random.normal(70, 10, 500)
plot_distribution_with_kde(normal_data, "Normal Distribution", "day44_hist_normal.png")

skewed_data = np.random.exponential(scale=2, size=500)
plot_distribution_with_kde(skewed_data, "Right-Skewed Distribution", "day44_hist_skewed.png")

print("\nAll plots saved successfully.")

